# 🚀 GUIA RÁPIDO - DataDash

## ⚡ Início Rápido (5 minutos)

### 1. Criar o Ambiente Virtual
```bash
python -m venv venv
```

### 2. Ativar o Ambiente (escolha seu OS)

**Linux/Mac:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Criar o Banco de Dados

Abra o MySQL e execute:
```sql
CREATE DATABASE datadash_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 5. Fazer as Migrations
```bash
cd datadash
python manage.py makemigrations
python manage.py migrate
```

### 6. Criar o Admin
```bash
python manage.py createsuperuser
```

### 7. Iniciar o Servidor
```bash
python manage.py runserver
```

### 8. Acessar no Navegador
```
http://127.0.0.1:8000
```

---

## 📤 Testar com o Arquivo de Exemplo

1. **Dashboard:** http://127.0.0.1:8000
2. **Upload:** http://127.0.0.1:8000/upload/
3. **Selecione:** `exemplo_vendas.csv`
4. **Clique:** "Enviar Planilha"
5. **Volte para o Dashboard** para ver os gráficos!

---

## 🔑 Acessos

| Local | URL |
|-------|-----|
| Dashboard | http://127.0.0.1:8000 |
| Admin | http://127.0.0.1:8000/admin |
| Upload | http://127.0.0.1:8000/upload/ |
| Dados | http://127.0.0.1:8000/dados/ |

---

## ⚠️ Problema Comum?

Se receber erro `mysqlclient` no Windows:
```bash
pip install PyMySQL
```

Então adicione ao final de `datadash/settings.py`:
```python
import pymysql
pymysql.install_as_MySQLdb()
```

Veja `TROUBLESHOOTING.md` para mais problemas.

---

**Pronto! Seu projeto está rodando! 🎉**
