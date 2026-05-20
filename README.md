# DataDash

Aplicacao web em Django para importar planilhas de vendas em `CSV` ou `XLSX`, armazenar os registros no banco e exibir um dashboard com indicadores, graficos e listagem dos dados importados.

## Stack

- Python
- Django 4.2
- Pandas
- OpenPyXL
- Chart.js
- SQLite por padrao
- MySQL opcional via variaveis de ambiente

## O que o projeto faz

- Upload de planilhas de vendas em `CSV` e `XLSX`
- Validacao das colunas obrigatorias
- Importacao dos registros para o banco
- Dashboard com faturamento, total de vendas, total de itens e ticket medio
- Graficos por categoria, produto e mes
- Tela para consultar os dados importados
- Acao para limpar os dados carregados
- Admin do Django em `/admin/`

## Estrutura principal

```text
.
├── datadash/
│   ├── manage.py
│   ├── settings.py
│   ├── urls.py
│   └── dashboard/
│       ├── models.py
│       ├── views.py
│       ├── forms.py
│       ├── urls.py
│       └── templates/dashboard/
├── exemplo_vendas.csv
└── requirements.txt
```

## Requisitos

- Python 3.8 ou superior
- `pip`
- Ambiente virtual recomendado

## Dependencias

As dependencias do projeto estao em `requirements.txt`:

- `Django`
- `pandas`
- `openpyxl`
- `PyMySQL`

## Banco de dados

Por padrao o projeto usa `SQLite` e cria o arquivo `db.sqlite3` automaticamente apos as migracoes.

Se voce quiser usar `MySQL`, configure estas variaveis antes de rodar as migracoes:

```bash
export DATADASH_DB_ENGINE=mysql
export DATADASH_DB_NAME=datadash_db
export DATADASH_DB_USER=root
export DATADASH_DB_PASSWORD=
export DATADASH_DB_HOST=localhost
export DATADASH_DB_PORT=3306
```

## Como rodar

Na raiz do projeto:

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 datadash/manage.py migrate
python3 datadash/manage.py runserver
```

Depois acesse `http://127.0.0.1:8000`.

## Rotas principais

- `/` dashboard principal
- `/upload/` envio de planilhas
- `/dados/` visualizacao dos dados importados
- `/limpar/` limpeza dos dados
- `/admin/` painel administrativo

## Formato esperado da planilha

Colunas obrigatorias:

- `data`
- `produto`
- `categoria`
- `quantidade`
- `preco_unitario`

Exemplo:

```csv
data,produto,categoria,quantidade,preco_unitario
01/01/2024,Notebook,Eletronicos,2,2500.00
05/01/2024,Mouse,Perifericos,10,50.00
```

O projeto inclui o arquivo [exemplo_vendas.csv](/media/bardo/Developer/Repositorio/Portifolio/Minerva-AnalisedePlanilha/exemplo_vendas.csv) para teste.

## Fluxo rapido de teste

1. Rode o servidor.
2. Abra `/upload/`.
3. Envie `exemplo_vendas.csv`.
4. Consulte o dashboard em `/` e a listagem em `/dados/`.

## Observacoes

- O upload aceita `CSV` e `XLSX`.
- Para `CSV`, a leitura tenta lidar com diferentes codificacoes e separadores.
- Datas sao interpretadas com `dayfirst=True`.
- O projeto esta com `DEBUG = True` em [datadash/settings.py](/media/bardo/Developer/Repositorio/Portifolio/Minerva-AnalisedePlanilha/datadash/settings.py:1).
