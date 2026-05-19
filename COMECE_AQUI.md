# COMECE AQUI - DataDash

## Fluxo Recomendado

O projeto agora roda por padrao com `sqlite3`, sem depender de MySQL para iniciar.

### 0. Entrar na pasta certa
```bash
cd /caminho/para/Minerva-AnalisedePlanilha
```

Confira se voce esta no lugar certo:

```bash
ls
```

Voce deve ver `requirements.txt` e a pasta `datadash/`.

### 1. Criar o ambiente virtual
```bash
python3 -m venv venv
```

Se esse comando falhar no Linux com `ensurepip is not available`, instale antes:

```bash
sudo apt install python3-venv
```

### 2. Ativar o ambiente
```bash
source venv/bin/activate
```

No Windows:
```bash
venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
python3 -m pip install -r requirements.txt
```

### 4. Criar o banco local
```bash
python3 datadash/manage.py migrate
```

### 5. Criar usuario admin
```bash
python3 datadash/manage.py createsuperuser
```

### 6. Rodar o servidor
```bash
python3 datadash/manage.py runserver
```

### 7. Abrir no navegador
`http://127.0.0.1:8000`

## Teste Rapido

1. Acesse `http://127.0.0.1:8000/upload/`
2. Envie `exemplo_vendas.csv`
3. Volte ao dashboard para ver os cards e graficos

## Se Quiser Usar MySQL

O MySQL ficou opcional. Antes de rodar `migrate`, exporte estas variaveis:

```bash
export DATADASH_DB_ENGINE=mysql
export DATADASH_DB_NAME=datadash_db
export DATADASH_DB_USER=root
export DATADASH_DB_PASSWORD=
export DATADASH_DB_HOST=localhost
export DATADASH_DB_PORT=3306
```

Depois crie o banco no MySQL:

```sql
CREATE DATABASE datadash_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

E rode normalmente:

```bash
python3 datadash/manage.py migrate
python3 datadash/manage.py runserver
```

## Arquivos Importantes

- `QUICKSTART.md`: versao resumida
- `README.md`: documentacao completa
- `TROUBLESHOOTING.md`: erros comuns
- `COMANDOS_RAPIDOS.sh`: comandos prontos
