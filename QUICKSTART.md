# GUIA RAPIDO - DataDash

## Subir em poucos minutos

Antes de tudo, entre na pasta raiz do projeto, onde estao `requirements.txt` e a pasta `datadash/`:

```bash
cd /caminho/para/Minerva-AnalisedePlanilha
```

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 datadash/manage.py migrate
python3 datadash/manage.py runserver
```

Abra `http://127.0.0.1:8000`.

## Testar o upload

1. Acesse `http://127.0.0.1:8000/upload/`
2. Selecione `exemplo_vendas.csv`
3. Clique em "Enviar Planilha"
4. Volte ao dashboard

## MySQL opcional

Se quiser usar MySQL em vez de `sqlite3`:

```bash
export DATADASH_DB_ENGINE=mysql
export DATADASH_DB_NAME=datadash_db
export DATADASH_DB_USER=root
export DATADASH_DB_PASSWORD=
export DATADASH_DB_HOST=localhost
export DATADASH_DB_PORT=3306
```

Depois rode:

```bash
python3 datadash/manage.py migrate
python3 datadash/manage.py runserver
```
