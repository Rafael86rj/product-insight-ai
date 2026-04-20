# 📊 Product Insight AI

## 🎯 Objetivo

Desenvolver um sistema capaz de transformar dados de produtos e avaliações de clientes em **insights estratégicos e operacionais**, utilizando análise de dados e modelos de linguagem (LLM) executados localmente.

O foco é reduzir a distância entre **dados brutos → tomada de decisão**.

---

## 🚀 Problema

Empresas possuem grande volume de dados e reviews, mas enfrentam dificuldades em:

* Identificar padrões relevantes
* Priorizar categorias estratégicas
* Traduzir feedback de clientes em melhorias acionáveis

---

## 💡 Solução

Este projeto implementa um pipeline completo que:

1. Realiza **tratamento e padronização de dados**
2. Executa **análise estatística (KPIs)**
3. Utiliza **LLM local (LM Studio)** para:

   * gerar insights estratégicos (categorias)
   * interpretar feedback de clientes (reviews)
4. Consolida tudo em:

   * 📊 Dashboard interativo (Streamlit)
   * 📄 Relatório automatizado

---

## 🧠 Arquitetura

```
Dados → Tratamento → Análise → IA → Output
                               ├── Dashboard
                               └── Relatório
```

---

## 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* Streamlit
* LM Studio (LLM local)
* Qwen / Llama (modelos leves)

---

## 📊 Principais Análises

* Média ponderada por categoria
* Relação entre desconto e avaliação
* Identificação de padrões em reviews
* Classificação de categorias por relevância

---

## 🔍 Principais Insights

* Categorias apresentam **alta consistência de avaliação**
* Segmentos como *Electronics* combinam **escala + boa percepção**
* Nichos como *OfficeProducts* apresentam **alta qualidade com menor volume**
* Feedback de clientes aponta **problemas recorrentes de consistência e durabilidade**

---

## ⚙️ Como Executar

### 1. Clonar o repositório

```
git clone https://github.com/Rafael86rj/product-insight-ai.git
cd product-insight-ai
```

### 2. Criar ambiente virtual

```
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar dependências

```
pip install -r requirements.txt
```

### 4. Executar dashboard

```
streamlit run app.py
```
## 📊 Dashboard


---

## 🤖 Diferencial Técnico

Este projeto utiliza **LLM local**, o que garante:

* Baixo custo operacional (sem APIs pagas)
* Maior controle sobre os dados
* Independência de serviços externos

---

## 📌 Próximos Passos

* Evoluir para arquitetura multi-agente
* Implementar scoring automático de produtos
* Integrar com APIs externas (opcional)

---

## 📬 Contato

Aberto a feedbacks e oportunidades para aplicar esse tipo de solução em cenários reais.
