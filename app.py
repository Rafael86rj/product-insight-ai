# %%
import streamlit as st
import pandas as pd
from src.data_processing.tratamento import tratar_dados, tratar_categoria

st.set_page_config(page_title="Product Insight AI", layout="wide")

st.title("📊 Product Insight AI")

# Carregamento
caminho = r"data/amazon.csv"
df = pd.read_csv(caminho)

# 🔥 AQUI ESTÁ O DIFERENCIAL
df = tratar_dados(df)
df = tratar_categoria(df)

# Visão geral
st.subheader("📌 Visão Geral")
st.write(df.head())

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Total Produtos", len(df))
col2.metric("Rating Médio", round(df["avaliacao"].mean(), 2))
col3.metric("Desconto Médio", round(df["porcentagem_desconto"].mean(), 2))

# Gráfico por categoria (com filtro inteligente)
st.subheader("📊 Avaliação por Categoria")

df_categoria = (
    df.groupby("categoria_principal")
    .agg(
        media_avaliacao=("avaliacao", "mean"),
        qtd_produtos=("nome_produto", "count")
    )
    .query("qtd_produtos >= 10")  # 🔥 filtro estratégico
    .sort_values("media_avaliacao", ascending=False)
)

st.bar_chart(df_categoria["media_avaliacao"])
