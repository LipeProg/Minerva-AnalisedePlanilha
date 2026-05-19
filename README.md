# DataDash - Dashboard de Planilhas

## 📋 Descrição do Projeto

DataDash é um **dashboard acadêmico simples** para análise de dados de vendas. O usuário faz upload de uma planilha (CSV ou XLSX) com informações de vendas, e o sistema exibe um dashboard com indicadores e gráficos básicos.

Este projeto foi desenvolvido como **trabalho acadêmico** de estudante, com foco em **simplicidade, organização e facilidade de apresentação**.

## 🎯 Objetivo

Fornecer uma solução básica para:
- Upload de planilhas com dados de vendas
- Visualização de indicadores (faturamento, quantidade, ticket médio, etc.)
- Análise através de gráficos simples
- Visualização de dados importados
- Limpeza de dados quando necessário

## 🛠️ Tecnologias Utilizadas

- **Django 4.2+** - Framework web Python
- **MySQL** - Banco de dados relacional
- **Pandas** - Leitura e processamento de planilhas
- **OpenPyXL** - Suporte para arquivos XLSX
- **Chart.js** - Gráficos interativos no frontend
- **HTML5 e CSS3** - Interface web simples

## 📊 Formato da Planilha

A planilha deve obrigatoriamente conter as seguintes colunas:

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| data | Data | Data da venda (DD/MM/YYYY) |
| produto | Texto | Nome do produto |
| categoria | Texto | Categoria do produto |
| quantidade | Número | Quantidade vendida |
| preco_unitario | Número | Preço unitário (com decimais) |

**Formatos Aceitos:** CSV ou XLSX

### Exemplo:

```
data,produto,categoria,quantidade,preco_unitario
01/01/2024,Notebook,Eletrônicos,2,2500.00
05/01/2024,Mouse,Periféricos,10,50.00
```

## 🗄️ Configuração do Banco de Dados

### 1. Criar o Banco MySQL

Execute o comando abaixo no MySQL ou no seu gerenciador de banco:

```sql
CREATE DATABASE datadash_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

**Credenciais Padrão:**
- Usuário: `root`
- Senha: *(vazia)*
- Host: `localhost`
- Porta: `3306`

**Nota:** Se você usa credenciais diferentes, altere o arquivo `datadash/settings.py` na seção `DATABASES`.

## 📦 Instalação e Configuração

### 1. Criar o Ambiente Virtual

```bash
python -m venv venv
```

### 2. Ativar o Ambiente Virtual

**No Linux/Mac:**
```bash
source venv/bin/activate
```

**No Windows:**
```bash
venv\Scripts\activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

**Observação para Windows:** Se o `mysqlclient` der erro na instalação, pode usar `PyMySQL` como alternativa:

```bash
pip install PyMySQL
```

Neste caso, adicione isto ao final de `datadash/settings.py`:

```python
import pymysql
pymysql.install_as_MySQLdb()
```

### 4. Criar as Tabelas do Banco

```bash
python datadash/manage.py makemigrations
python datadash/manage.py migrate
```

### 5. Criar um Superusuário (Admin)

```bash
python datadash/manage.py createsuperuser
```

Você será solicitado a inserir:
- Nome de usuário
- Email
- Senha

### 6. Iniciar o Servidor

```bash
python datadash/manage.py runserver
```

O servidor estará disponível em: `http://127.0.0.1:8000`

## 🚀 Como Testar o Projeto

### 1. Acessar o Dashboard

1. Abra o navegador e vá para: `http://127.0.0.1:8000`
2. Você verá a página inicial com os indicadores (vazios no início)

### 2. Fazer Upload do Arquivo de Exemplo

1. Clique no menu "Upload"
2. Clique em "Selecione o arquivo"
3. Selecione o arquivo `exemplo_vendas.csv` fornecido
4. Clique em "Enviar Planilha"

### 3. Visualizar o Dashboard

1. Após o upload, volte para "Dashboard"
2. Você verá os indicadores preenchidos
3. Os gráficos serão exibidos com base nos dados importados

### 4. Visualizar os Dados

1. Clique em "Dados" para ver todas as vendas importadas
2. A página mostra um histórico dos uploads e uma tabela com as vendas

### 5. Acessar o Admin

1. Vá para: `http://127.0.0.1:8000/admin`
2. Faça login com o superusuário criado
3. Você pode gerenciar vendas e arquivos importados

## 📁 Estrutura do Projeto

```
datadash/
├── datadash/                    # Configurações principais
│   ├── __init__.py
│   ├── settings.py              # Configurações do Django
│   ├── urls.py                  # URLs do projeto
│   └── wsgi.py
├── dashboard/                   # App principal
│   ├── migrations/              # Migrações do banco
│   ├── templates/
│   │   └── dashboard/
│   │       ├── base.html        # Template base
│   │       ├── dashboard.html   # Dashboard principal
│   │       ├── upload.html      # Upload de planilha
│   │       ├── dados.html       # Visualização de dados
│   │       └── confirmar_limpeza.html  # Confirmação de limpeza
│   ├── models.py                # Modelos do banco
│   ├── views.py                 # Lógica das views
│   ├── forms.py                 # Formulários
│   ├── urls.py                  # URLs do app
│   └── admin.py                 # Configuração do admin
├── manage.py                    # Gerenciador do Django
├── requirements.txt             # Dependências
├── README.md                    # Este arquivo
└── exemplo_vendas.csv           # Arquivo de exemplo
```

## 🔗 Rotas Disponíveis

| Rota | Descrição |
|------|-----------|
| `/` | Dashboard principal com indicadores e gráficos |
| `/upload/` | Página para fazer upload de planilhas |
| `/dados/` | Visualização de dados importados |
| `/limpar/` | Página para limpar todos os dados |
| `/admin/` | Painel administrativo do Django |

## 💡 Funcionalidades

### Dashboard Principal
- ✅ Card com faturamento total
- ✅ Card com quantidade de vendas
- ✅ Card com total de itens vendidos
- ✅ Card com ticket médio
- ✅ Card com produto mais vendido
- ✅ Gráfico de faturamento por categoria (barras)
- ✅ Gráfico de quantidade vendida por produto (pizza)
- ✅ Gráfico de faturamento por mês (linha)
- ✅ Tabela com últimas vendas

### Upload
- ✅ Upload de arquivos CSV ou XLSX
- ✅ Validação de colunas obrigatórias
- ✅ Cálculo automático de faturamento (quantidade × preço)
- ✅ Mensagens de sucesso e erro
- ✅ Registro de arquivo importado

### Dados
- ✅ Visualização de todos os dados importados
- ✅ Histórico de uploads
- ✅ Botão para limpar dados

### Admin
- ✅ Gerenciamento de vendas
- ✅ Gerenciamento de arquivos importados
- ✅ Filtros simples

## 📸 Sugestões para Documentação (Screenshots)

Para documentar o projeto, capture screenshots das seguintes páginas:

1. **Dashboard Principal**
   - Mostrar os 5 cards de indicadores
   - Mostrar os 3 gráficos principais

2. **Página de Upload**
   - Mostrar o formulário de upload
   - Mostrar a mensagem de sucesso após upload

3. **Página de Dados**
   - Mostrar a tabela com os dados importados

4. **Admin Django**
   - Mostrar a lista de vendas no admin

## 🎓 Conclusão

DataDash é um projeto acadêmico simples e direto que demonstra:
- Conhecimento em **Django**
- Manipulação de **dados com Pandas**
- Integração com **banco de dados MySQL**
- Criação de **interfaces web simples**
- Uso de **gráficos com Chart.js**

O projeto é **fácil de apresentar** em aula, pois tem funcionalidades claras e um visual limpo que não aparenta ser "sobredimensionado".

---

**Desenvolvido como projeto acadêmico | 2024**
