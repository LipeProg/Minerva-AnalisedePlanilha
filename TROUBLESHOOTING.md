# TROUBLESHOOTING E FAQ

## Problemas Comuns

### 1. Erro: "mysqlclient not found" ou "No module named 'MySQLdb'"

**Causa:** A biblioteca `mysqlclient` não está instalada ou não conseguiu compilar.

**Solução 1 (Linux):**
```bash
sudo apt-get install python3-dev default-libmysqlclient-dev
pip install mysqlclient
```

**Solução 2 (Windows) - Use PyMySQL:**
```bash
pip uninstall mysqlclient
pip install PyMySQL
```

Depois, adicione isto ao final do arquivo `datadash/settings.py`:
```python
import pymysql
pymysql.install_as_MySQLdb()
```

**Solução 3 (Mac):**
```bash
brew install mysql
pip install mysqlclient
```

---

### 2. Erro: "Access denied for user 'root'@'localhost'"

**Causa:** Senha ou credenciais do MySQL estão incorretas.

**Solução:**
1. Edite `datadash/settings.py`
2. Na seção `DATABASES`, altere `USER` e `PASSWORD`
3. Exemplo com senha:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'datadash_db',
        'USER': 'root',
        'PASSWORD': 'sua_senha_aqui',  # <- Altere isso
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

### 3. Erro: "Unknown database 'datadash_db'"

**Causa:** O banco de dados não foi criado no MySQL.

**Solução:**
1. Abra o MySQL Command Line ou MySQL Workbench
2. Execute:
```sql
CREATE DATABASE datadash_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

---

### 4. Erro ao fazer migrations: "No such table: dashboard_venda"

**Causa:** Você não rodou as migrations ainda.

**Solução:**
```bash
python datadash/manage.py makemigrations
python datadash/manage.py migrate
```

---

### 5. ImportError: No module named 'django'

**Causa:** Django não está instalado no ambiente virtual.

**Solução:**
```bash
source venv/bin/activate  # No Linux/Mac
# ou
venv\Scripts\activate  # No Windows

pip install -r requirements.txt
```

---

### 6. "No such file or directory: 'manage.py'"

**Causa:** Você está rodando o comando fora da pasta correta.

**Solução:**
Certifique-se de estar DENTRO da pasta `datadash`:
```bash
cd datadash
python manage.py runserver
```

---

### 7. Upload de arquivo retorna erro

**Causa:** A planilha pode ter formato incorreto ou colunas faltantes.

**Verificar:**
- A planilha tem as colunas: `data`, `produto`, `categoria`, `quantidade`, `preco_unitario`?
- O arquivo é CSV ou XLSX?
- Os dados estão corretos (sem valores nulos nas colunas obrigatórias)?

**Solução:**
1. Baixe o arquivo `exemplo_vendas.csv` como referência
2. Use-o como modelo para sua planilha
3. Certifique-se de usar a mesma formatação

---

### 8. Gráficos não aparecem no dashboard

**Causa:** Pode ser um erro de JavaScript ou dados não foram importados.

**Verificar:**
1. Você fez upload de uma planilha?
2. Abra o Console do Navegador (F12) e procure por erros
3. Certifique-se de que o Chart.js foi carregado (linha de CDN no base.html)

---

### 9. "CSRF token missing or incorrect"

**Causa:** Problema com proteção CSRF do Django.

**Solução:**
1. Certifique-se de que o template contém `{% csrf_token %}`
2. Limpe o cache do navegador (Ctrl+Shift+Del)
3. Reinicie o servidor Django

---

### 10. Porta 8000 já está em uso

**Causa:** Outro processo já está usando a porta 8000.

**Solução:**
Use outra porta:
```bash
python datadash/manage.py runserver 8001
```

---

## Dicas e Truques

### Resetar o Banco de Dados Completamente

```bash
# Apagar todas as tabelas e começar do zero
python datadash/manage.py flush

# Depois rodar as migrations novamente
python datadash/manage.py migrate
```

### Ver logs de SQL

Adicione isto a `settings.py` para ver as queries SQL:
```python
LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
```

### Criar um Superusuário Automático (Script)

Crie um arquivo `criar_admin.py` na raiz do projeto:
```python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datadash.settings')
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superusuário 'admin' criado com sucesso!")
else:
    print("Superusuário já existe!")
```

Execute com:
```bash
python datadash/manage.py shell < criar_admin.py
```

---

## Contato e Suporte

Se encontrar outros problemas:
1. Verifique a documentação oficial do Django: https://docs.djangoproject.com/
2. Procure no Stack Overflow por mensagens de erro similares
3. Verifique se todas as dependências estão instaladas: `pip list`

---

**Boa sorte com seu projeto! 🚀**
