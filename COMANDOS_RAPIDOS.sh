#!/bin/bash
# COMANDOS RÁPIDOS - DataDash
# Copie e cole os comandos abaixo conforme necessário

# ============================================
# 1️⃣ CONFIGURAÇÃO INICIAL
# ============================================

# Criar ambiente virtual
python -m venv venv

# Ativar (Linux/Mac)
source venv/bin/activate

# Ativar (Windows)
# venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# ============================================
# 2️⃣ BANCO DE DADOS
# ============================================

# Criar banco MySQL (execute no MySQL)
# CREATE DATABASE datadash_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# Fazer migrations
cd datadash
python manage.py makemigrations
python manage.py migrate

# ============================================
# 3️⃣ ADMIN E USUÁRIOS
# ============================================

# Criar superusuário
python manage.py createsuperuser

# Reset de banco (cuidado!)
# python manage.py flush

# ============================================
# 4️⃣ RODAR PROJETO
# ============================================

# Rodar servidor (porta padrão 8000)
python manage.py runserver

# Rodar em porta diferente
# python manage.py runserver 8001

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
# python manage.py shell

# Ver dados no banco
# python manage.py dbshell

# ============================================
# 7️⃣ TROUBLESHOOTING
# ============================================

# Verificar versão Django
# python -m django --version

# Listar dependências
# pip list

# Reinstalar dependências
# pip install --upgrade -r requirements.txt

# ============================================
# 8️⃣ ARQUIVO DE TESTE
# ============================================

# O arquivo exemplo_vendas.csv está na raiz
# Use-o para testar o upload no dashboard
