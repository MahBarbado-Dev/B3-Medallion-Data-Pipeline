# 📈 Roadmap: Data Pipeline B3 (Arquitetura Medalhão)

Este documento detalha as etapas de um Analista/Engenheiro de Dados para construir um pipeline completo, desde a extração dos dados brutos da B3 até a entrega de valor através de visualizações.

---

## 🛠 Fase 1: Ingestão e Camada Bronze (Raw)
**Objetivo:** Trazer os dados para o ambiente de forma íntegra e organizada.

- [ ] **Tarefa 1.1: Validação de Layout**
  - Estudar o manual do COTAHIST (PDF da B3) para entender as posições fixas (`colspecs`).
- [ ] **Tarefa 1.2: Otimização do Parser**
  - Ajustar o `read_fwf` para usar `nrows` e `encoding='latin-1'`.
  - Implementar leitura em blocos (`chunksize`) se o arquivo for muito grande para a RAM.
- [ ] **Tarefa 1.3: Carga Initial (Bronze)**
  - Salvar os dados brutos lidos em formato **Parquet** na pasta `bronze/`. Parquet é mais rápido e ocupa menos espaço.

---

## 🧹 Fase 2: Limpeza e Camada Silver (Trusted)
**Objetivo:** Transformar os dados brutos em uma tabela limpa, tipada e pronta para análise.

- [ ] **Tarefa 2.1: Tipagem de Dados**
  - Converter colunas de data (YYYMMDD) para o formato `datetime`.
  - Ajustar campos de preço (dividir por 100, conforme manual da B3 para tratar decimais).
- [ ] **Tarefa 2.2: Filtragem de Segmento**
  - Filtrar apenas registros de negociação de ações (`tipo_registro == "01"`).
  - Remover headers e footers do arquivo original.
- [ ] **Tarefa 2.3: Persistência (Silver)**
  - Salvar o DataFrame limpo em `silver/cotahist_consolidado.parquet`.

---

## 💎 Fase 3: Agregação e Camada Gold (Business)
**Objetivo:** Criar tabelas de indicadores prontas para Dashboards.

- [ ] **Tarefa 3.1: Cálculo de Volatilidade e Médias**
  - Criar médias móveis (7, 21 e 50 dias) para os principais ativos (PETR4, VALE3, etc.).
- [ ] **Tarefa 3.2: Tabela de Comportamento Setorial**
  - Cruzar dados da B3 com uma tabela de setores (Setor Financeiro, Varejo, etc.).
- [ ] **Tarefa 3.3: Persistência (Gold)**
  - Salvar as tabelas de KPIs em `gold/indicadores_mercado.parquet`.

---

## 📊 Fase 4: Análise e Visualização
**Objetivo:** Contar a história dos dados e gerar insights.

- [ ] **Tarefa 4.1: Exploração em Notebook**
  - Criar gráficos de linha para preços de fechamento.
  - Analisar correlação entre diferentes ações.
- [ ] **Tarefa 4.2: Dashboard (PowerBI/Streamlit/Plotly)**
  - Criar uma visualização interativa onde o usuário escolhe o "Ticker" (ex: ITUB4) e vê o histórico e indicadores.

---

## 🚀 Fase 5: Automação e Melhores Práticas
- [ ] **Documentação:** Manter o `README.md` atualizado com como rodar o projeto.
- [ ] **Scripts:** Converter os notebooks de ETL em scripts `.py` organizados dentro da pasta `scripts/`.
- [ ] **Logs:** Adicionar mensagens de log para saber quando cada etapa do pipeline terminar com sucesso.
