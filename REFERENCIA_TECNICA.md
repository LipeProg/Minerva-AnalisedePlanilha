# 📚 REFERÊNCIA TÉCNICA - DataDash

## Mapeamento de Rotas

| Rota | View | Template | Função |
|------|------|----------|--------|
| `/` | `dashboard()` | `dashboard.html` | Exibe indicadores e gráficos |
| `/upload/` | `upload()` | `upload.html` | Faz upload de planilha |
| `/dados/` | `dados()` | `dados.html` | Visualiza dados importados |
| `/limpar/` | `confirmar_limpeza()` | `confirmar_limpeza.html` | Limpa todos os dados |
| `/admin/` | Django Admin | - | Gerencia dados |

---

## Modelos de Dados

### Model: Venda
```python
- id (PK)
- data (DateField)
- produto (CharField, 100)
- categoria (CharField, 100)
- quantidade (IntegerField)
- preco_unitario (DecimalField, 10,2)
- faturamento (DecimalField, 12,2) [calculado]
- data_importacao (DateTimeField, auto_now_add)
```

**Índices:** Por categoria, data, data_importacao

### Model: ArquivoImportado
```python
- id (PK)
- nome_arquivo (CharField, 255)
- data_upload (DateTimeField, auto_now_add)
- total_linhas (IntegerField)
```

---

## Lógica de Upload

```
1. Recebe arquivo (CSV ou XLSX)
2. Lê com pandas
3. Verifica colunas obrigatórias:
   - data, produto, categoria, quantidade, preco_unitario
4. Para cada linha:
   - Converte data para Date
   - Valida dados
   - Calcula: faturamento = quantidade * preco_unitario
   - Salva em Venda
5. Registra em ArquivoImportado
6. Retorna mensagem sucesso/erro
```

---

## Cálculos do Dashboard

### Indicadores (Cards)
```python
total_faturamento = SUM(venda.faturamento)
total_vendas = COUNT(venda)
total_itens = SUM(venda.quantidade)
ticket_medio = total_faturamento / total_vendas
produto_mais_vendido = MAX(SUM(venda.quantidade) GROUP BY produto)
```

### Gráfico 1: Faturamento por Categoria
```python
Data: 
  X: categoria (agrupado)
  Y: SUM(faturamento) por categoria
Tipo: Bar Chart
```

### Gráfico 2: Quantidade por Produto
```python
Data:
  X: produto (top 10)
  Y: SUM(quantidade) por produto
Tipo: Doughnut Chart
```

### Gráfico 3: Faturamento por Mês
```python
Data:
  X: mês/ano
  Y: SUM(faturamento) por mês
Tipo: Line Chart
```

---

## Dependências do Projeto

```
Django>=4.2              # Framework web
pandas>=1.5.0            # Processamento de dados
openpyxl>=3.9.0          # Leitura de XLSX
mysqlclient>=2.1.0       # Driver MySQL (ou PyMySQL)
Chart.js                 # Gráficos (CDN)
```

---

## Configurações Importantes

### settings.py
```python
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
DATABASE = MySQL (datadash_db)
DEBUG = True (desenvolvimento)
```

### Base de dados
```sql
CREATE DATABASE datadash_db 
  CHARACTER SET utf8mb4 
  COLLATE utf8mb4_unicode_ci;
```

---

## Fluxo de Dados

```
Usuário
    ↓
[Upload de Arquivo]
    ↓
Validação (Pandas + Python)
    ↓
Banco de Dados (MySQL)
    ↓
[Dashboard View]
    ↓
Agregação (Django ORM)
    ↓
Template + Chart.js
    ↓
Navegador (Gráficos)
```

---

## Estrutura de Arquivos com Tipos

```
datadash/
├── datadash/
│   ├── settings.py           [CONFIG]
│   ├── urls.py               [ROUTING]
│   ├── wsgi.py               [SERVER]
│   └── __init__.py
│
├── dashboard/
│   ├── models.py             [MODELS] - Venda, ArquivoImportado
│   ├── views.py              [LOGIC] - 4 views principais
│   ├── forms.py              [FORM] - UploadPlanilhaForm
│   ├── urls.py               [ROUTING]
│   ├── admin.py              [ADMIN] - VendaAdmin, ArquivoImportadoAdmin
│   ├── apps.py               [CONFIG]
│   ├── migrations/           [MIGRATIONS]
│   └── templates/dashboard/
│       ├── base.html         [LAYOUT] - CSS incluído
│       ├── dashboard.html    [VIEW] + Chart.js
│       ├── upload.html       [VIEW]
│       ├── dados.html        [VIEW]
│       └── confirmar_limpeza.html [VIEW]
│
├── manage.py                 [ENTRY POINT]
├── requirements.txt          [DEPS]
├── README.md                 [DOC]
├── QUICKSTART.md             [DOC]
├── TROUBLESHOOTING.md        [DOC]
├── APRESENTACAO.md           [DOC]
├── exemplo_vendas.csv        [DATA]
└── .gitignore                [GIT]
```

---

## Padrões Utilizados

### Function-Based Views
```python
def dashboard(request):
    # Lógica aqui
    return render(request, 'template.html', contexto)
```

### Django ORM (Aggregations)
```python
Venda.objects.values('categoria').annotate(
    total=Sum('faturamento')
).order_by('-total')
```

### JSON para Frontend
```python
import json
dados_json = json.dumps({
    'labels': lista,
    'valores': valores
})
# Template: {{ dados_json|safe }}
```

### Pandas para CSV/XLSX
```python
if arquivo.endswith('.csv'):
    df = pd.read_csv(arquivo)
elif arquivo.endswith('.xlsx'):
    df = pd.read_excel(arquivo)
```

---

## Variáveis de Template Principais

### dashboard.html
```django
{{ total_faturamento }}      # String formatada
{{ total_vendas }}            # Inteiro
{{ total_itens }}             # Inteiro
{{ ticket_medio }}            # String formatada
{{ produto_mais_vendido }}    # String
{{ ultimas_vendas }}          # QuerySet
{{ dados_categoria|safe }}    # JSON para Chart
{{ dados_produto|safe }}      # JSON para Chart
{{ dados_mes|safe }}          # JSON para Chart
```

---

## Segurança (Básica)

✅ **Implementado:**
- CSRF Token em formulários
- SQL Injection prevenido (Django ORM)
- Validação de tipos de arquivo
- DEBUG=True (apenas dev, mudar para False em produção)

⚠️ **Não implementado (projeto acadêmico):**
- Login/Autenticação
- HTTPS
- Rate limiting
- Testes de segurança
- Permissões avançadas

---

## Performance

- Queries otimizadas com `.values()` e `.annotate()`
- Limite de 10 últimas vendas no dashboard
- Top 10 produtos nos gráficos
- Chart.js renderiza no cliente (não no servidor)

---

## Como Estender o Projeto

### 1. Adicionar Nova Coluna
```python
# models.py
class Venda(models.Model):
    cliente = models.CharField(max_length=100, blank=True)

# views.py
# Validar na upload
if 'cliente' in colunas_df:
    cliente = row['cliente']
```

### 2. Novo Gráfico
```python
# views.py - dashboard()
novo_dado = Venda.objects.aggregate(...)
contexto['novo_dado'] = json.dumps(...)

# dashboard.html
<canvas id="novoGrafico"></canvas>
<script>
  const ctx = document.getElementById('novoGrafico');
  new Chart(ctx, {...});
</script>
```

### 3. Novo Modelo
```python
# models.py
class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)

# admin.py
admin.site.register(Cliente)
```

---

## Comandos Django Úteis

```bash
# Criar migrations após alterar models
python manage.py makemigrations

# Aplicar migrations
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Abrir shell interativo
python manage.py shell

# Resetar banco completamente
python manage.py flush

# Runserver em porta diferente
python manage.py runserver 8001
```

---

## Checklist de Teste

- [ ] Upload com CSV válido funciona
- [ ] Upload com XLSX válido funciona
- [ ] Erro se faltam colunas
- [ ] Faturamento calculado corretamente
- [ ] Dashboard mostra indicadores corretos
- [ ] Gráficos renderizam
- [ ] Dados podem ser visualizados
- [ ] Dados podem ser apagados
- [ ] Admin funciona
- [ ] Mensagens de sucesso/erro aparecem

---

**Referência Técnica Completa | DataDash 2024**
