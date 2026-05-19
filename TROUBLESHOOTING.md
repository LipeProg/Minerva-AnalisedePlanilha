# TROUBLESHOOTING

## 1. `No module named django`

Crie e ative o ambiente virtual antes de instalar:

```bash
cd /caminho/para/Minerva-AnalisedePlanilha
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

## 2. `requirements.txt` nao foi encontrado

Voce provavelmente esta fora da pasta do projeto.

Entre na raiz e confira:

```bash
cd /caminho/para/Minerva-AnalisedePlanilha
ls
```

Voce precisa ver:

- `requirements.txt`
- `datadash/`

## 3. `zsh: command not found: python`

Use `python3` no lugar de `python`:

```bash
python3 datadash/manage.py runserver
```

Se estiver com o ambiente virtual ativado, `python3` continua funcionando normalmente.

## 4. `pip install -r requirements.txt` falha

Atualize o `pip` dentro do ambiente e tente de novo:

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## 5. `python3 -m venv venv` falha com `ensurepip is not available`

No Debian/Ubuntu, instale o pacote do venv:

```bash
sudo apt install python3-venv
```

## 6. `python3 datadash/manage.py migrate` falha com MySQL

O projeto usa `sqlite3` por padrao. Se voce nao precisa de MySQL, remova a variavel:

```bash
unset DATADASH_DB_ENGINE
```

Depois rode:

```bash
python3 datadash/manage.py migrate
```

Se voce quer mesmo MySQL, confira:

- `DATADASH_DB_ENGINE=mysql`
- banco `datadash_db` criado
- usuario e senha corretos nas variaveis de ambiente

## 7. `Unknown database 'datadash_db'`

Crie o banco antes das migrations:

```sql
CREATE DATABASE datadash_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

## 8. `Access denied for user`

Ajuste as variaveis:

```bash
export DATADASH_DB_USER=seu_usuario
export DATADASH_DB_PASSWORD=sua_senha
```

## 9. `No such file or directory: manage.py`

Rode os comandos a partir da raiz do projeto usando:

```bash
python3 datadash/manage.py runserver
```

Ou entre na pasta `datadash/` antes de usar `python3 manage.py`.

## 10. Upload retorna erro de coluna

Verifique se sua planilha tem estas colunas:

- `data`
- `produto`
- `categoria`
- `quantidade`
- `preco_unitario`

## 11. Graficos nao aparecem

Confira se houve upload com sucesso e se o navegador conseguiu carregar o CDN do Chart.js.

## 12. Porta 8000 ocupada

Use outra porta:

```bash
python3 datadash/manage.py runserver 8001
```
