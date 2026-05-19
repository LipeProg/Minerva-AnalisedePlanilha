# DATADASH - PROJETO ACADÊMICO DJANGO

**Resumo Executivo - Capa do Projeto**

---

## 📊 O QUE É

**DataDash** é um **dashboard web para análise de dados de vendas** desenvolvido em **Django**.

O usuário faz upload de uma planilha (CSV ou XLSX) com dados de vendas, e o sistema exibe:
- 5 indicadores principais (cards)
- 3 gráficos interativos
- Tabela de dados
- Histórico de uploads

---

## 🎯 OBJETIVO

Demonstrar habilidades em:
- ✅ Django (Backend)
- ✅ Banco de Dados (MySQL)
- ✅ Processamento de Dados (Pandas)
- ✅ Frontend (HTML, CSS, JavaScript)
- ✅ Gráficos (Chart.js)

---

## 🛠️ TECNOLOGIAS

| Camada | Tecnologia |
|--------|-----------|
| **Backend** | Django 4.2+ |
| **Frontend** | HTML5, CSS3, JS |
| **Banco** | MySQL 5.7+ |
| **Processamento** | Pandas, OpenPyXL |
| **Gráficos** | Chart.js |

---

## 📁 ESTRUTURA

```
datadash/
├── datadash/          (Configurações Django)
├── dashboard/         (Aplicação principal)
│   ├── models.py      (2 modelos: Venda, ArquivoImportado)
│   ├── views.py       (4 views: dashboard, upload, dados, limpar)
│   └── templates/     (5 templates HTML)
├── requirements.txt   (Dependências)
└── exemplo_vendas.csv (Arquivo de teste)
```

---

## 🔗 ROTAS

```
/              Dashboard
/upload/       Upload de planilha
/dados/        Visualização de dados
/limpar/       Limpeza de dados
/admin/        Admin Django
```

---

## ⚡ COMEÇAR RÁPIDO

```bash
# 1. Ambiente
python -m venv venv
source venv/bin/activate

# 2. Instalar
pip install -r requirements.txt

# 3. Banco MySQL
CREATE DATABASE datadash_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# 4. Migrations
cd datadash
python manage.py migrate

# 5. Admin
python manage.py createsuperuser

# 6. Run
python manage.py runserver

# 7. Acessar
http://127.0.0.1:8000
```

---

## 📋 O QUE ESTÁ INCLUÍDO

✅ Código Django completo e funcional
✅ Banco MySQL pré-configurado
✅ Processamento de planilhas com Pandas
✅ Dashboard com 3 gráficos Chart.js
✅ Admin Django automático
✅ 11 documentos de documentação
✅ Arquivo de exemplo para testar

---

## 📚 DOCUMENTAÇÃO

| Arquivo | Para |
|---------|------|
| **COMECE_AQUI.md** | Começar (leia primeiro!) |
| **QUICKSTART.md** | 5 minutos |
| **README.md** | Completo |
| **DOCUMENTACAO_IMPRESSAO.md** | Imprimir e entregar |
| **CONTEXTO_IA.md** | Contextualizar ChatGPT |
| **TROUBLESHOOTING.md** | Erros |
| **APRESENTACAO.md** | Para aula |
| **REFERENCIA_TECNICA.md** | Código |
| **SUMARIO.md** | Resumo |

---

## 🎓 POR QUE ESTE PROJETO?

✅ **Completo:** Não é um "hello world", faz algo real
✅ **Legível:** Código simples e bem organizado
✅ **Apresentável:** Visual limpo e profissional
✅ **Acadêmico:** Apropriado para trabalho escolar
✅ **Documentado:** 11+ documentos explicando tudo

---

## 📊 FUNCIONALIDADES

### Dashboard
- 5 Cards com indicadores
- 3 Gráficos Chart.js
- Tabela com últimas vendas

### Upload
- Suporta CSV e XLSX
- Valida dados
- Processa com Pandas
- Salva no banco

### Dados
- Visualiza todas as vendas
- Histórico de uploads
- Botão para limpar

### Admin
- Painel Django automático
- Editar vendas
- Filtros e buscas

---

## 🗄️ MODELOS

```
Venda:
  - data
  - produto
  - categoria
  - quantidade
  - preco_unitario
  - faturamento (calculado)
  - data_importacao

ArquivoImportado:
  - nome_arquivo
  - data_upload
  - total_linhas
```

---

## 💡 DESTAQUE

A planilha esperada tem esta estrutura:

```csv
data,produto,categoria,quantidade,preco_unitario
01/01/2024,Notebook,Eletrônicos,2,2500.00
05/01/2024,Mouse,Periféricos,10,50.00
```

O sistema:
1. Lê a planilha
2. Valida colunas
3. Calcula: `faturamento = quantidade × preco_unitario`
4. Salva no banco
5. Mostra no dashboard

---

## 🚀 TESTE AGORA

1. Ative o ambiente virtual
2. Rode `python manage.py migrate`
3. Rode `python manage.py createsuperuser`
4. Rode `python manage.py runserver`
5. Acesse `http://127.0.0.1:8000/upload/`
6. Envie `exemplo_vendas.csv`
7. Volte para home e veja o dashboard!

---

## 📦 ARQUIVO INCLUÍDO

O arquivo `exemplo_vendas.csv` tem 14 linhas de dados fictícios para teste:

```
Produtos: Notebook, Mouse, Teclado, Monitor, etc
Categorias: Eletrônicos, Periféricos, Acessórios, Componentes
Período: Janeiro-Fevereiro 2024
```

---

## ⚠️ O QUE NÃO TEM (Intencionalmente)

- ❌ Login personalizado (usa admin Django)
- ❌ Permissões avançadas
- ❌ API REST
- ❌ Testes automatizados
- ❌ Paginação complexa
- ❌ Exportação de dados

Por quê? Porque este é um **projeto acadêmico simples**, não uma aplicação empresarial.

---

## 🎯 PARA APRESENTAÇÃO

O projeto é perfeito para demonstrar em aula porque:

1. **Simples de entender:** Não há complexidade desnecessária
2. **Visualmente atrativo:** Dashboard bonito
3. **Funcional:** Tudo realmente funciona
4. **Explicável:** Fácil justificar cada decision de design

---

## 📖 PRÓXIMA LEITURA

Depois de ler este resumo, leia:

1. **COMECE_AQUI.md** - Guia passo a passo para rodar
2. **DOCUMENTACAO_IMPRESSAO.md** - Detalhes completos para imprimir
3. **CONTEXTO_IA.md** - Para usar com ChatGPT

---

## 📞 SUPORTE RÁPIDO

**Problema?** Verifique em `TROUBLESHOOTING.md`

**Não funciona?** Rode em ordem:
1. `python -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `cd datadash`
5. `python manage.py migrate`
6. `python manage.py runserver`

---

## ✨ CONCLUSÃO

Este é um **projeto Django profissional e bem estruturado** que demonstra conhecimento real em desenvolvimento web, sem pretender ser mais do que é: um trabalho acadêmico de qualidade.

---

**Bem-vindo ao DataDash! 🚀**

---

*Projeto Acadêmico Django | DataDash Dashboard*
*Versão 1.0 | 19 de maio de 2026*

---

## 📋 CHECKLIST RÁPIDO

- [ ] Leu este resumo
- [ ] Explorou a estrutura do projeto
- [ ] Entendeu as tecnologias usadas
- [ ] Vai ler COMECE_AQUI.md
- [ ] Vai instalar as dependências
- [ ] Vai testar com exemplo_vendas.csv
- [ ] Vai apresentar com confiança!

---

**Aproveite! Boa codificação! 🎓**
