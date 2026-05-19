# 🎯 COMECE AQUI - DataDash

## 👋 Bem-vindo ao Projeto DataDash!

Este é um **projeto Django completo** para análise de dados de vendas. 
Tudo que você precisa já está aqui. Segue este guia para começar.

---

## ⚡ 5 Minutos para Começar

### Passo 1: Ativar Ambiente
```bash
# Linux/Mac:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

### Passo 2: Instalar Dependências
```bash
pip install -r requirements.txt
```

### Passo 3: Criar Banco MySQL
```sql
CREATE DATABASE datadash_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### Passo 4: Migrations
```bash
cd datadash
python manage.py migrate
```

### Passo 5: Criar Admin
```bash
python manage.py createsuperuser
# Digite um usuário e senha qualquer
```

### Passo 6: Rodar!
```bash
python manage.py runserver
```

### Passo 7: Acessar
Abra seu navegador e vá para:
```
http://127.0.0.1:8000
```

---

## 📚 Documentos Importantes

Escolha de acordo com sua necessidade:

### 🚀 **Quer começo rápido?**
→ Leia [`QUICKSTART.md`](QUICKSTART.md)

### ❓ **Deu erro?**
→ Procure em [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md)

### 🎓 **Vai apresentar em aula?**
→ Estude [`APRESENTACAO.md`](APRESENTACAO.md)

### 📖 **Quer entender o código?**
→ Consulte [`REFERENCIA_TECNICA.md`](REFERENCIA_TECNICA.md)

### 📝 **Leia tudo em detalhes**
→ Veja [`README.md`](README.md)

### 📊 **Visão geral rápida**
→ Confira [`SUMARIO.md`](SUMARIO.md)

---

## 🧪 Testando o Projeto

Depois de rodar o servidor:

### 1. Ir para Upload
Clique em "Upload" no menu, ou vá para:
```
http://127.0.0.1:8000/upload/
```

### 2. Enviar Arquivo de Exemplo
- Clique em "Selecione o arquivo"
- Escolha: `exemplo_vendas.csv` (está na raiz do projeto)
- Clique em "Enviar Planilha"

### 3. Ver o Dashboard
- Volte para o Dashboard (home)
- Você verá:
  - 5 Cards com números
  - 3 Gráficos com dados
  - Tabela com vendas

### 4. Explorar
- Clique em "Dados" para ver todas as vendas
- Clique em "Admin" para gerenciar
- Clique em "Limpar" para apagar (opcional)

---

## 🎯 Estrutura do Projeto

```
Seu projeto está aqui:
📁 Minerva-AnalisedePlanilha/

Dentro tem:
├── 📄 README.md              ← Documentação completa
├── 📄 QUICKSTART.md          ← Começo rápido
├── 📄 TROUBLESHOOTING.md     ← Resolução de erros
├── 📄 APRESENTACAO.md        ← Para apresentar
├── 📄 REFERENCIA_TECNICA.md  ← Detalhes técnicos
├── 📄 SUMARIO.md             ← Resumo
│
├── 📄 requirements.txt        ← O que instalar
├── 📄 exemplo_vendas.csv      ← Dados para testar
│
└── 📁 datadash/              ← Projeto Django
    ├── 📄 manage.py          ← Gerenciador
    ├── 📄 settings.py        ← Configurações
    ├── 📄 urls.py            ← Rotas principais
    │
    └── 📁 dashboard/         ← Aplicação principal
        ├── 📄 models.py      ← Dados (Venda, Arquivo)
        ├── 📄 views.py       ← Lógica (4 páginas)
        ├── 📄 urls.py        ← Rotas do app
        ├── 📄 admin.py       ← Admin do Django
        │
        └── 📁 templates/     ← Páginas HTML
            └── 📁 dashboard/
                ├── base.html           ← Layout
                ├── dashboard.html      ← Gráficos
                ├── upload.html         ← Upload
                ├── dados.html          ← Dados
                └── confirmar_limpeza.html
```

---

## ✅ Checklist de Configuração

- [ ] Ambiente virtual criado e ativado
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] Banco MySQL criado (`CREATE DATABASE...`)
- [ ] Migrations feitas (`python manage.py migrate`)
- [ ] Superusuário criado (`python manage.py createsuperuser`)
- [ ] Servidor rodando (`python manage.py runserver`)
- [ ] Navegador abrindo em http://127.0.0.1:8000
- [ ] Arquivo `exemplo_vendas.csv` encontrado
- [ ] Upload do arquivo funcionou
- [ ] Dashboard mostrando dados

---

## 🆘 Tive um Erro!

### Erro comum #1: "mysqlclient not found"
**Solução:** Leia `TROUBLESHOOTING.md` seção 1

### Erro comum #2: "Unknown database"
**Solução:** Crie o banco MySQL (passo 3 acima)

### Erro comum #3: "No such table"
**Solução:** Execute as migrations (passo 4 acima)

### Erro comum #4: Outro erro?
**Solução:** Procure em `TROUBLESHOOTING.md` - tem +10 soluções lá!

---

## 🎓 O Que Você Tem

Um projeto **completo** com:

✅ **Backend:** Django com MySQL
✅ **Frontend:** HTML/CSS simples
✅ **Dados:** Pandas para processar planilhas
✅ **Gráficos:** Chart.js interativo
✅ **Admin:** Painel administrativo
✅ **Documentação:** 6 arquivos explicando tudo
✅ **Exemplo:** CSV pronto para testar

---

## 🚀 Próximos Passos

### Hoje (Começar)
1. Ativar ambiente virtual
2. Instalar dependências
3. Configurar banco MySQL
4. Rodar servidor
5. Testar com exemplo

### Esta Semana (Aprender)
1. Ler `README.md` (entender tudo)
2. Estudar `models.py` (estrutura de dados)
3. Estudar `views.py` (lógica principal)
4. Explorar templates (interface)

### Depois (Expandir)
1. Adicionar novos gráficos
2. Adicionar filtros
3. Adicionar login
4. Exportar dados

---

## 💬 FAQ Rápido

**P: Por que não funciona?**
R: Verifique `TROUBLESHOOTING.md`

**P: Como apresentar em aula?**
R: Leia `APRESENTACAO.md`

**P: O arquivo de exemplo está onde?**
R: Na raiz: `exemplo_vendas.csv`

**P: Como mudar a senha do banco?**
R: Edite `datadash/settings.py` seção `DATABASES`

**P: Qual é a senha padrão?**
R: Não tem senha padrão (deixamos em branco)

**P: Pode usar em produção?**
R: Não, este é um projeto acadêmico. Para produção, leia Django docs.

---

## 🎉 Tudo Pronto?

Você agora tem um projeto Django **profissional**, **documentado** e **fácil de entender**.

### Seu próximo passo:

```bash
# Ativa ambiente
source venv/bin/activate

# Vai para pasta
cd datadash

# Roda servidor
python manage.py runserver
```

Depois abra: **http://127.0.0.1:8000**

---

## 📞 Ajuda Rápida

| Dúvida | Arquivo |
|--------|---------|
| Como fazer em 5 min? | `QUICKSTART.md` |
| Não funciona! | `TROUBLESHOOTING.md` |
| Como apresentar? | `APRESENTACAO.md` |
| Entender o código | `REFERENCIA_TECNICA.md` |
| Tudo bem explicado | `README.md` |
| Resumo rápido | `SUMARIO.md` |

---

**Bem-vindo ao DataDash! Boa codificação! 🚀**

---

*Desenvolvido para ser simples, claro e acadêmico.*  
*Sucesso na sua apresentação! 🎓*
