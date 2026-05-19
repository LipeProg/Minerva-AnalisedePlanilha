# DataDash - Dashboard de Planilhas

## Descricao

DataDash e um projeto Django academico para importar uma planilha de vendas e mostrar indicadores, graficos e uma tabela com os registros processados.

## Funcionalidades

- Upload de arquivos CSV e XLSX
- Dashboard com cards de resumo
- Graficos com Chart.js
- Tabela com vendas importadas
- Painel administrativo do Django

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

## Instalacao

### Opcao mais simples: sqlite3

Entre primeiro na raiz do projeto:

```bash
cd /caminho/para/Minerva-AnalisedePlanilha
```

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 datadash/manage.py migrate
python3 datadash/manage.py createsuperuser
python3 datadash/manage.py runserver
```

O banco `db.sqlite3` sera criado automaticamente na raiz do projeto.

### Opcao com MySQL

Instale as dependencias, crie o banco e exporte as variaveis:

```bash
export DATADASH_DB_ENGINE=mysql
export DATADASH_DB_NAME=datadash_db
export DATADASH_DB_USER=root
export DATADASH_DB_PASSWORD=
export DATADASH_DB_HOST=localhost
export DATADASH_DB_PORT=3306
```

```sql
CREATE DATABASE datadash_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Depois rode:

```bash
python3 datadash/manage.py migrate
python3 datadash/manage.py runserver
```

## Como testar

1. Abra `http://127.0.0.1:8000`
2. Acesse `http://127.0.0.1:8000/upload/`
3. Envie `exemplo_vendas.csv`
4. Volte ao dashboard

## Estrutura principal

```text
Minerva-AnalisedePlanilha/
├── datadash/
│   ├── manage.py
│   ├── settings.py
│   ├── urls.py
│   └── dashboard/
├── requirements.txt
├── exemplo_vendas.csv
├── COMECE_AQUI.md
├── QUICKSTART.md
└── TROUBLESHOOTING.md
```

## Observacoes tecnicas

- O projeto usa `sqlite3` por padrao para reduzir atrito na primeira execucao
- Se o arquivo CSV vier com `;` ou codificacao diferente, o upload tenta ler de forma mais tolerante
- Datas como `01/02/2024` sao tratadas com `dayfirst=True`
