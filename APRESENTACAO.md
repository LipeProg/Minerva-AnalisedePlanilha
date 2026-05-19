# 🎓 GUIA DE APRESENTAÇÃO - DataDash

## Estrutura para Apresentação em Aula

Siga esta ordem para uma apresentação limpa e profissional:

---

## 1️⃣ INTRODUÇÃO (1-2 minutos)

**O que é o DataDash?**
- Sistema web para análise de dados de vendas
- Usuário faz upload de planilha (CSV ou XLSX)
- Sistema exibe dashboard com indicadores e gráficos
- Banco de dados MySQL

**Tecnologias:**
- Django (backend)
- HTML/CSS (frontend simples)
- Chart.js (gráficos)
- Pandas (processamento de dados)

---

## 2️⃣ DEMONSTRAÇÃO PRÁTICA (3-5 minutos)

### Passo 1: Mostrar a Página Inicial (Dashboard)
- **O quê:** Indicadores vazios no início
- **Explique:** "Aqui virão os dados depois que importarmos uma planilha"

### Passo 2: Ir para Upload
- **Clique em:** "Upload" no menu
- **Selecione:** `exemplo_vendas.csv`
- **Clique em:** "Enviar Planilha"
- **Mostre a mensagem:** "14 vendas importadas com sucesso!"

### Passo 3: Voltar ao Dashboard
- **Mostre os cards preenchidos:**
  - Faturamento total: R$ 22.770,00
  - Total de vendas: 14
  - Total de itens: 125
  - Ticket médio: R$ 1.626,43
  - Produto mais vendido: Componentes/Notebook

### Passo 4: Mostrar os Gráficos
- **Gráfico 1:** Faturamento por categoria (barras)
- **Gráfico 2:** Quantidade por produto (pizza)
- **Gráfico 3:** Faturamento por mês (linha)

### Passo 5: Ir para Dados
- **Clique em:** "Dados"
- **Mostre:**
  - Histórico de uploads
  - Tabela com todas as vendas

### Passo 6: Mostrar o Admin
- **Vá para:** http://127.0.0.1:8000/admin
- **Login com:** usuário/senha criado
- **Mostre:**
  - Lista de vendas
  - Filtros por categoria e data
  - Arquivo importado registrado

---

## 3️⃣ EXPLICAR O CÓDIGO (2-3 minutos)

### Models (`models.py`)
```python
Venda:
  - data, produto, categoria
  - quantidade, preco_unitario
  - faturamento (calculado)
  - data_importacao

ArquivoImportado:
  - nome_arquivo
  - data_upload
  - total_linhas
```

**O quê:** "Temos duas tabelas principais"

### Views (`views.py`)
- **dashboard:** Calcula indicadores e dados para gráficos
- **upload:** Valida e processa o arquivo CSV/XLSX
- **dados:** Mostra todos os dados importados
- **confirmar_limpeza:** Limpa tudo

**O quê:** "Cada view faz uma coisa específica"

### Forms (`forms.py`)
- Formulário simples para upload
- Validação de arquivo

---

## 4️⃣ RESUMO DE FUNCIONALIDADES (1 minuto)

✅ **Funcionalidades Implementadas:**
- Upload de CSV e XLSX
- Validação de colunas obrigatórias
- Cálculo automático de faturamento
- Dashboard com 5 indicadores
- 3 gráficos interativos com Chart.js
- Tabela de últimas vendas
- Histórico de uploads
- Painel admin do Django
- Limpeza de dados

❌ **Intencionalmente NÃO Implementado (por ser acadêmico):**
- Login próprio (usa admin do Django)
- Permissões avançadas
- API REST
- Testes automatizados
- Paginação complexa
- Exportação de dados

---

## 5️⃣ ESTRUTURA DO PROJETO (1 minuto)

```
datadash/
├── datadash/          ← Configurações principais
│   ├── settings.py    ← Banco MySQL, apps, etc
│   ├── urls.py        ← Rotas principais
│   └── wsgi.py        ← WSGI para produção
│
├── dashboard/         ← Aplicação principal
│   ├── models.py      ← Modelos (Venda, ArquivoImportado)
│   ├── views.py       ← Lógica das páginas
│   ├── forms.py       ← Formulários
│   ├── urls.py        ← Rotas do app
│   ├── admin.py       ← Configuração do admin
│   └── templates/     ← Templates HTML
│       ├── base.html
│       ├── dashboard.html
│       ├── upload.html
│       ├── dados.html
│       └── confirmar_limpeza.html
│
├── manage.py          ← Gerenciador do Django
├── requirements.txt   ← Dependências
└── exemplo_vendas.csv ← Arquivo de exemplo
```

---

## 6️⃣ COMO RODAR O PROJETO (Mostrar no Terminal)

```bash
# 1. Ativar ambiente
source venv/bin/activate

# 2. Instalar (primeira vez)
pip install -r requirements.txt

# 3. Criar banco
CREATE DATABASE datadash_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# 4. Migrations
python datadash/manage.py migrate

# 5. Superusuário (primeira vez)
python datadash/manage.py createsuperuser

# 6. Rodar servidor
cd datadash
python manage.py runserver

# 7. Acessar
http://127.0.0.1:8000
```

---

## 📸 SCREENSHOTS SUGERIDOS PARA DOCUMENTAÇÃO

Se precisar fazer screenshots para documentação:

1. **Dashboard completo** - Mostrar cards e gráficos
2. **Upload com mensagem de sucesso**
3. **Página de dados** com tabela
4. **Admin Django** com lista de vendas
5. **Console do terminal** mostrando `runserver`

---

## 💬 POSSÍVEIS PERGUNTAS E RESPOSTAS

**P: Por que usou Django?**
R: "Django é um framework robusto, bem documentado e perfeito para aplicações web. Oferece admin automático, ORM poderosa e segurança."

**P: Por que pandas?**
R: "Pandas é a biblioteca padrão em Python para processar dados. Facilita ler CSV/XLSX e fazer transformações."

**P: Por que não usou React/Vue?**
R: "Este é um projeto acadêmico simples. A proposta era criar algo direto sem complexidade desnecessária. Templates Django são suficientes."

**P: Como validou as colunas?**
R: "Quando o arquivo é enviado, verificamos se as colunas obrigatórias existem. Se faltarem, mostramos erro."

**P: Por que o faturamento é calculado?**
R: "Economiza espaço no banco. A fórmula é: quantidade × preco_unitario. É feita no Python antes de salvar."

**P: Como funciona o Chart.js?**
R: "O Django envia os dados em JSON, o Chart.js renderiza os gráficos no navegador em tempo real."

---

## ⏱️ TIMING SUGERIDO

| Parte | Tempo |
|-------|-------|
| Introdução | 1-2 min |
| Demonstração | 3-5 min |
| Código | 2-3 min |
| Funcionalidades | 1 min |
| Estrutura | 1 min |
| **TOTAL** | **8-12 min** |

---

## ✅ CHECKLIST PRÉ-APRESENTAÇÃO

- [ ] Banco MySQL está rodando
- [ ] Servidor Django iniciado (`python manage.py runserver`)
- [ ] Arquivo `exemplo_vendas.csv` está acessível
- [ ] Superusuário foi criado
- [ ] Migrations foram executadas
- [ ] Teste upload com o arquivo de exemplo
- [ ] Todos os gráficos aparecem
- [ ] Admin está funcionando
- [ ] Tem um terminal pronto para mostrar comandos

---

## 🎯 DICA FINAL

**Seja sincero!** Diga que é um projeto acadêmico. Professores GOSTAM de ver:
- Código limpo e organizado ✅
- Funcionalidades que trabalham ✅
- Uso correto das tecnologias ✅
- Documentação adequada ✅
- Sem fingir ser algo que não é ✅

Isso é muito melhor que tentar fazer algo "super profissional" e parecer suspeito!

---

**Boa apresentação! 🚀**
