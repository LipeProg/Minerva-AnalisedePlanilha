#!/bin/bash
# COMANDOS RÁPIDOS - DataDash
# Copie e cole os comandos abaixo conforme necessário

# ============================================
# 1️⃣ CONFIGURAÇÃO INICIAL
# ============================================

# Entrar na raiz do projeto
cd /caminho/para/Minerva-AnalisedePlanilha

# Criar ambiente virtual
python3 -m venv venv

# Ativar (Linux/Mac)
source venv/bin/activate

# Ativar (Windows)
# venv\Scripts\activate

# Instalar dependências
python3 -m pip install -r requirements.txt

# ============================================
# 2️⃣ BANCO DE DADOS
# ============================================

# Padrão: sqlite3 (não precisa criar banco manualmente)
python3 datadash/manage.py migrate

# Opcional: usar MySQL
# export DATADASH_DB_ENGINE=mysql
# export DATADASH_DB_NAME=datadash_db
# export DATADASH_DB_USER=root
# export DATADASH_DB_PASSWORD=
# export DATADASH_DB_HOST=localhost
# export DATADASH_DB_PORT=3306
# CREATE DATABASE datadash_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
# python3 datadash/manage.py migrate

# ============================================
# 3️⃣ ADMIN E USUÁRIOS
# ============================================

# Criar superusuário
python3 datadash/manage.py createsuperuser

# Reset de banco (cuidado!)
# python3 datadash/manage.py flush

# ============================================
# 4️⃣ RODAR PROJETO
# ============================================

# Rodar servidor (porta padrão 8000)
python3 datadash/manage.py runserver

# Rodar em porta diferente
# python3 datadash/manage.py runserver 8001

# ============================================
# 5️⃣ ACESSOS
# ============================================

# Dashboard:     http://127.0.0.1:8000
# Upload:        http://127.0.0.1:8000/upload/
# Dados:         http://127.0.0.1:8000/dados/
# Admin:         http://127.0.0.1:8000/admin/

# ============================================
# 6️⃣ DESENVOLVIMENTO
# ============================================

# Shell Django interativo
# python3 datadash/manage.py shell

# Ver dados no banco
# python3 datadash/manage.py dbshell

# ============================================
# 7️⃣ TROUBLESHOOTING
# ============================================

# Verificar versão Django
# python3 datadash/manage.py --version

# Listar dependências
# pip list

# Reinstalar dependências
# python3 -m pip install --upgrade -r requirements.txt

# ============================================
# 8️⃣ ARQUIVO DE TESTE
# ============================================

# O arquivo exemplo_vendas.csv está na raiz
# Use-o para testar o upload no dashboard
