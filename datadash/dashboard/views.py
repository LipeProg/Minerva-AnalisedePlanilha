from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum, F
from io import BytesIO, StringIO
import pandas as pd
import json

from .models import Venda, ArquivoImportado
from .forms import UploadPlanilhaForm


def ler_planilha(arquivo):
    """Ler CSV/XLSX com opções mais tolerantes para arquivos comuns."""
    nome = arquivo.name.lower()
    conteudo = arquivo.read()

    if nome.endswith('.csv'):
        ultimo_erro = None

        for encoding in ('utf-8', 'latin1'):
            try:
                texto = conteudo.decode(encoding)
                return pd.read_csv(StringIO(texto), sep=None, engine='python')
            except Exception as exc:
                ultimo_erro = exc

        raise ultimo_erro

    if nome.endswith('.xlsx'):
        return pd.read_excel(BytesIO(conteudo))

    raise ValueError('Formato de arquivo não suportado. Use CSV ou XLSX.')


def dashboard(request):
    """Página inicial com dashboard e indicadores."""
    vendas = Venda.objects.all()
    
    # Calcular indicadores
    total_faturamento = vendas.aggregate(total=Sum('faturamento'))['total'] or 0
    total_vendas = vendas.count()
    total_itens = vendas.aggregate(total=Sum('quantidade'))['total'] or 0
    ticket_medio = total_faturamento / total_vendas if total_vendas > 0 else 0
    
    # Produto mais vendido
    produto_mais_vendido = vendas.values('produto').annotate(
        total_qtd=Sum('quantidade')
    ).order_by('-total_qtd').first()
    
    # Últimas vendas
    ultimas_vendas = vendas[:10]
    
    # Gráfico 1: Faturamento por categoria
    faturamento_categoria = vendas.values('categoria').annotate(
        total=Sum('faturamento')
    ).order_by('-total')
    
    categorias = [item['categoria'] for item in faturamento_categoria]
    valores_categoria = [float(item['total']) for item in faturamento_categoria]
    
    # Gráfico 2: Quantidade vendida por produto (top 10)
    quantidade_produto = vendas.values('produto').annotate(
        total_qtd=Sum('quantidade')
    ).order_by('-total_qtd')[:10]
    
    produtos = [item['produto'] for item in quantidade_produto]
    valores_produto = [item['total_qtd'] for item in quantidade_produto]
    
    # Gráfico 3: Faturamento por mês
    vendas_com_mes = vendas.annotate(
        mes=F('data__month'),
        ano=F('data__year')
    ).values('ano', 'mes').annotate(
        total=Sum('faturamento')
    ).order_by('ano', 'mes')
    
    meses_nomes = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
                   'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    
    meses_labels = []
    valores_mes = []
    for item in vendas_com_mes:
        mes_num = item['mes'] - 1
        meses_labels.append(meses_nomes[mes_num] if mes_num < 12 else 'Desconhecido')
        valores_mes.append(float(item['total']))
    
    # Converter para JSON para o Chart.js
    dados_categoria_json = json.dumps({
        'labels': categorias,
        'valores': valores_categoria
    })
    
    dados_produto_json = json.dumps({
        'labels': produtos,
        'valores': valores_produto
    })
    
    dados_mes_json = json.dumps({
        'labels': meses_labels,
        'valores': valores_mes
    })
    
    contexto = {
        'total_faturamento': f"{total_faturamento:.2f}",
        'total_vendas': total_vendas,
        'total_itens': total_itens,
        'ticket_medio': f"{ticket_medio:.2f}",
        'produto_mais_vendido': produto_mais_vendido['produto'] if produto_mais_vendido else 'N/A',
        'ultimas_vendas': ultimas_vendas,
        'dados_categoria': dados_categoria_json,
        'dados_produto': dados_produto_json,
        'dados_mes': dados_mes_json,
    }
    
    return render(request, 'dashboard/dashboard.html', contexto)


def upload(request):
    """Página para fazer upload de planilha."""
    if request.method == 'POST':
        form = UploadPlanilhaForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = request.FILES['arquivo']
            try:
                # Determinar tipo de arquivo
                df = ler_planilha(arquivo)
                
                # Verificar colunas obrigatórias
                colunas_obrigatorias = ['data', 'produto', 'categoria', 'quantidade', 'preco_unitario']
                df.columns = [col.lower().strip() for col in df.columns]
                colunas_df = list(df.columns)
                
                for coluna in colunas_obrigatorias:
                    if coluna not in colunas_df:
                        messages.error(request, f'A coluna "{coluna}" não foi encontrada no arquivo.')
                        return redirect('dashboard:upload')
                
                # Processar dados
                vendas_criadas = 0
                erros = 0
                
                for _, row in df.iterrows():
                    try:
                        data = pd.to_datetime(row['data'], dayfirst=True, errors='raise').date()
                        produto = str(row['produto']).strip()
                        categoria = str(row['categoria']).strip()
                        quantidade = int(row['quantidade'])
                        preco_unitario = float(row['preco_unitario'])
                        faturamento = quantidade * preco_unitario
                        
                        Venda.objects.create(
                            data=data,
                            produto=produto,
                            categoria=categoria,
                            quantidade=quantidade,
                            preco_unitario=preco_unitario,
                            faturamento=faturamento
                        )
                        vendas_criadas += 1
                    except Exception:
                        erros += 1
                        continue
                
                # Registrar arquivo importado
                ArquivoImportado.objects.create(
                    nome_arquivo=arquivo.name,
                    total_linhas=vendas_criadas
                )
                
                messages.success(request, f'{vendas_criadas} vendas importadas com sucesso!')
                if erros > 0:
                    messages.warning(request, f'{erros} linhas não foram importadas por erro.')
                
                return redirect('dashboard:upload')
            
            except Exception as e:
                messages.error(request, f'Erro ao processar arquivo: {str(e)}')
                return redirect('dashboard:upload')
    else:
        form = UploadPlanilhaForm()
    
    return render(request, 'dashboard/upload.html', {'form': form})


def dados(request):
    """Página para visualizar dados importados."""
    vendas = Venda.objects.all().order_by('-data')
    arquivos = ArquivoImportado.objects.all()
    
    contexto = {
        'vendas': vendas,
        'arquivos': arquivos,
        'total_vendas': vendas.count(),
    }
    
    return render(request, 'dashboard/dados.html', contexto)


def confirmar_limpeza(request):
    """Página de confirmação para limpar dados."""
    if request.method == 'POST':
        if 'confirmar' in request.POST:
            Venda.objects.all().delete()
            ArquivoImportado.objects.all().delete()
            messages.success(request, 'Todos os dados foram removidos com sucesso!')
        
        return redirect('dashboard:dashboard')
    
    return render(request, 'dashboard/confirmar_limpeza.html')
