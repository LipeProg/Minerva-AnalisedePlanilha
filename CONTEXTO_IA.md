# CONTEXTO DO PROJETO PARA INTELIGÊNCIA ARTIFICIAL
## DataDash - Dashboard de Planilhas

---

## INSTRUÇÃO INICIAL

Cole o texto abaixo em uma conversa com ChatGPT ou outro assistente de IA quando precisar de ajuda com o projeto:

---

## 📋 CONTEXTO COMPLETO DO PROJETO

Estou trabalhando em um **projeto Django acadêmico chamado DataDash** - um dashboard para análise de dados de vendas. 

### Objetivo Geral
Criar um sistema web que permita usuários fazer upload de planilhas CSV/XLSX com dados de vendas e visualizar um dashboard interativo com gráficos e indicadores.

### Stack Tecnológico
- **Backend:** Django 4.2+, Python 3.8+
- **Banco de Dados:** MySQL 5.7+
- **Frontend:** HTML5, CSS3, JavaScript puro
- **Processamento de Dados:** Pandas, OpenPyXL
- **Gráficos:** Chart.js (CDN)

### Arquitetura
- **Padrão:** MVT (Model-View-Template) Django
- **Tipo:** Function-Based Views (não Class-Based Views)
- **ORM:** Django ORM com queries agregadas
- **Admin:** Painel administrativo Django automático

---

## 📊 ESTRUTURA DO PROJETO

```
datadash/
├── datadash/
│   ├── settings.py          # MySQL configurado
│   ├── urls.py              # Rotas principais
│   └── wsgi.py
├── dashboard/
│   ├── models.py            # Venda, ArquivoImportado
│   ├── views.py             # 4 views principais
│   ├── forms.py             # UploadPlanilhaForm
│   ├── urls.py              # Rotas do app
│   ├── admin.py             # Admin config
│   └── templates/dashboard/
│       ├── base.html        # Layout + CSS
│       ├── dashboard.html   # Dashboard
│       ├── upload.html      # Upload
│       ├── dados.html       # Dados
│       └── confirmar_limpeza.html
├── requirements.txt
└── exemplo_vendas.csv
```

---

## 🗄️ MODELOS DE DADOS

### Modelo 1: Venda
```python
class Venda(models.Model):
    data = models.DateField()                          # Data da venda
    produto = models.CharField(max_length=100)         # Nome do produto
    categoria = models.CharField(max_length=100)       # Categoria
    quantidade = models.IntegerField()                 # Quantidade vendida
    preco_unitario = models.DecimalField(10,2)         # Preço por unidade
    faturamento = models.DecimalField(12,2)            # Calculado: qtd × preço
    data_importacao = models.DateTimeField(auto_now_add=True)  # Auto
```

### Modelo 2: ArquivoImportado
```python
class ArquivoImportado(models.Model):
    nome_arquivo = models.CharField(max_length=255)    # Nome do arquivo
    data_upload = models.DateTimeField(auto_now_add=True)  # Quando foi
    total_linhas = models.IntegerField()                # Quantidade processada
```

---

## 🎯 FUNCIONALIDADES

### 1. Dashboard (GET /)
- 5 Cards com indicadores:
  - Faturamento total (SUM)
  - Total de vendas (COUNT)
  - Total de itens (SUM quantidade)
  - Ticket médio (AVG)
  - Produto mais vendido
  
- 3 Gráficos Chart.js:
  - Bar: Faturamento por categoria
  - Doughnut: Top 10 produtos
  - Line: Faturamento por mês
  
- Tabela com últimas 10 vendas

### 2. Upload (POST /upload/)
- Recebe arquivo CSV ou XLSX
- Validação de colunas obrigatórias:
  - data, produto, categoria, quantidade, preco_unitario
- Processamento com Pandas:
  - Lê arquivo
  - Converte tipos
  - Calcula faturamento = quantidade × preco_unitario
  - Salva em banco
- Cria registro em ArquivoImportado
- Retorna mensagem sucesso/erro

### 3. Dados (GET /dados/)
- Tabela com TODAS as vendas
- Histórico de uploads
- Botão para limpar dados

### 4. Limpar (POST /limpar/)
- Página de confirmação
- Delete em cascata
- Limpa Venda + ArquivoImportado

### 5. Admin (GET /admin/)
- Painel Django automático
- Editar vendas
- Filtros e buscas

---

## 🔗 ROTAS

```
GET  /                  → dashboard()
POST /upload/           → upload()
GET  /dados/            → dados()
POST /limpar/           → confirmar_limpeza()
GET  /admin/            → Django admin
```

---

## 💻 VIEW DETALHES

### View: dashboard()
```python
# Queryset de vendas
vendas = Venda.objects.all()

# Agregações para cards
total_faturamento = vendas.aggregate(total=Sum('faturamento'))['total']
total_vendas = vendas.count()
total_itens = vendas.aggregate(total=Sum('quantidade'))['total']
ticket_medio = total_faturamento / total_vendas

# Para gráficos (JSON)
dados_categoria = vendas.values('categoria').annotate(
    total=Sum('faturamento')
).order_by('-total')

# Renderiza template com contexto
return render(request, 'dashboard/dashboard.html', contexto)
```

### View: upload()
```python
# POST: recebe arquivo
arquivo = request.FILES['arquivo']

# Pandas lê
if arquivo.endswith('.csv'):
    df = pd.read_csv(arquivo)
elif arquivo.endswith('.xlsx'):
    df = pd.read_excel(arquivo)

# Valida colunas
colunas_obrigatorias = ['data', 'produto', 'categoria', 'quantidade', 'preco_unitario']

# Itera linhas
for index, row in df.iterrows():
    data = pd.to_datetime(row['data']).date()
    faturamento = row['quantidade'] * row['preco_unitario']
    Venda.objects.create(...)

# Registra em ArquivoImportado
ArquivoImportado.objects.create(...)

# Retorna mensagem
messages.success(request, 'X vendas importadas!')
```

---

## 📋 COLUNAS DA PLANILHA ESPERADA

```
data,produto,categoria,quantidade,preco_unitario
01/01/2024,Notebook,Eletrônicos,2,2500.00
05/01/2024,Mouse,Periféricos,10,50.00
...
```

**Obrigatório:** data, produto, categoria, quantidade, preco_unitario
**Opcional:** cliente (ignorado se existir)

---

## 🎨 FRONTEND

### CSS
- Sem Bootstrap, CSS puro
- Embutido em base.html
- Cores: Azul (#3498db), Cinza (#2c3e50)
- Responsive: Grid CSS

### Templates
- base.html: Layout + CSS
- dashboard.html: Charts com Chart.js
- upload.html: Formulário
- dados.html: Tabelas
- confirmar_limpeza.html: Confirmação

### JavaScript
- Chart.js via CDN
- Sem frameworks (React, Vue, etc)
- Dados em JSON do backend

---

## 🔒 SEGURANÇA

Implementado:
- CSRF Token em formulários
- Django ORM (previne SQL injection)
- Validação de tipos
- Whitelist de extensões

Não implementado (projeto acadêmico):
- Login personalizado
- HTTPS
- Rate limiting

---

## 📦 DEPENDÊNCIAS (requirements.txt)

```
Django>=4.2
pandas>=1.5.0
openpyxl>=3.9.0
mysqlclient>=2.1.0
```

---

## 🗄️ BANCO DE DADOS

**Tipo:** MySQL
**Nome:** datadash_db
**User:** root
**Senha:** (vazia)
**Charset:** utf8mb4

```sql
CREATE DATABASE datadash_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

---

## 🚀 COMO RODAR

```bash
# 1. Setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 2. Banco
# No MySQL: CREATE DATABASE datadash_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# 3. Migrations
cd datadash
python manage.py migrate

# 4. Admin
python manage.py createsuperuser

# 5. Run
python manage.py runserver

# 6. Acesso
# Dashboard: http://127.0.0.1:8000
# Upload: http://127.0.0.1:8000/upload/
# Admin: http://127.0.0.1:8000/admin/
```

---

## 📝 CONVENÇÕES DO CÓDIGO

- **Linguagem:** Português (variáveis, funções, comments)
- **Views:** Function-based (não class-based)
- **ORM:** Django ORM com aggregate/annotate
- **Templates:** Django template language
- **Nomes:** snake_case para variáveis, CamelCase para classes
- **Styling:** Sem dependências, CSS puro

---

## 🎯 OBJETIVO DO PROJETO

Este é um **projeto acadêmico** que demonstra:
1. Conhecimento em Django
2. Processamento de dados com Pandas
3. Banco de dados MySQL
4. Frontend com HTML/CSS/JavaScript
5. ORM e queries agregadas
6. Administração de dados

**Não é** um projeto empresarial. É intencionalmente simples, bem estruturado e fácil de entender.

---

## 📂 ARQUIVO DE EXEMPLO

Existe um arquivo `exemplo_vendas.csv` com 14 linhas fictícias para testar:

```csv
data,produto,categoria,quantidade,preco_unitario
01/01/2024,Notebook,Eletrônicos,2,2500.00
05/01/2024,Mouse,Periféricos,10,50.00
08/01/2024,Teclado,Periféricos,5,150.00
...
```

---

## ⚠️ LIMITAÇÕES (INTENCIONAIS)

- Sem login de usuários personalizado
- Sem permissões avançadas
- Sem API REST
- Sem testes automatizados
- Sem cache (Redis)
- Sem paginação avançada
- Sem exportação de dados
- Sem filtros complexos

---

## 🔄 FLUXO DE DADOS

```
1. Usuário faz upload
2. View recebe arquivo
3. Pandas processa (lê CSV/XLSX)
4. Valida colunas
5. Converte tipos de dados
6. Calcula faturamento
7. Salva em Venda (ORM)
8. Registra em ArquivoImportado
9. Retorna sucesso
10. Usuário acessa dashboard
11. View executa queries agregadas
12. Renderiza template com dados
13. Chart.js desenha gráficos
14. Usuário vê resultado
```

---

## 🤔 QUANDO PEDIR AJUDA

Use este contexto quando precisar de ajuda com:

**Exemplos:**
- "Como adicionar um novo gráfico?"
- "Como adicionar filtros?"
- "Como fazer login?"
- "Como exportar dados?"
- "Como otimizar queries?"
- "Como fazer deploy?"
- "Como adicionar validações?"
- "Como criar testes?"

**Template de pergunta:**

```
Estou trabalhando no DataDash (Django) e preciso:
[SUA_PERGUNTA]

Contexto: [INFORMAÇÕES ESPECÍFICAS]

O que você sugere?
```

---

## 📞 INFORMAÇÕES PARA DEBUGAR

Se pedir ajuda, forneça:

1. **Arquivo afetado:** models.py, views.py, template, etc
2. **O que está acontecendo:** erro, comportamento inesperado, etc
3. **O que esperava:** qual era o resultado esperado
4. **Seu código:** copie o snippet relevante

**Exemplo:**
```
Arquivo: dashboard/views.py
Erro: "No module named 'pandas'"
Esperava: importar pandas
Código:
import pandas as pd
```

---

## 🎓 PARA FINS ACADÊMICOS

Este projeto é ideal para:
- Demonstrar habilidades em Django
- Mostrar processamento de dados
- Apresentar em aula
- Servir como portfólio
- Aprender padrões de web development

---

## ✅ CHECKLIST DE ENTENDIMENTO

Após ler este contexto, você deveria saber:

- [ ] Qual é o objetivo do projeto
- [ ] Como está estruturado (pastas e arquivos)
- [ ] Quais são os 2 modelos (Venda e ArquivoImportado)
- [ ] Como funciona o upload
- [ ] Quais são as 5 rotas principais
- [ ] Qual é o stack tecnológico
- [ ] Como rodar o projeto
- [ ] Qual é o arquivo de exemplo

---

## 🚀 PRÓXIMOS PASSOS

1. **Entender o projeto:** Leia DOCUMENTACAO_IMPRESSAO.md
2. **Rodar localmente:** Siga os passos em QUICKSTART.md
3. **Explorar código:** Leia models.py, views.py
4. **Testar:** Use exemplo_vendas.csv
5. **Apresentar:** Use APRESENTACAO.md

---

## 📖 DOCUMENTAÇÃO RELACIONADA

- **DOCUMENTACAO_IMPRESSAO.md** - Tudo em detalhes (para imprimir)
- **README.md** - Documentação completa
- **COMECE_AQUI.md** - Passo a passo
- **QUICKSTART.md** - 5 minutos
- **TROUBLESHOOTING.md** - Erros comuns
- **REFERENCIA_TECNICA.md** - Detalhes técnicos
- **APRESENTACAO.md** - Como apresentar

---

## 🎯 RESUMO EM UMA FRASE

**DataDash é um dashboard Django acadêmico que permite upload de planilhas CSV/XLSX e visualiza dados de vendas com gráficos interativos.**

---

---

## FIM DO CONTEXTO

**Use este documento para contextualizar ChatGPT ou qualquer IA sobre o projeto DataDash.**

Após colar este texto, você pode fazer perguntas específicas e o assistente terá contexto completo do projeto.

---

*Contexto do Projeto DataDash*
*Versão: 1.0*
*Data: 19 de maio de 2026*
