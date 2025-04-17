import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# título do app
st.title("📊 Análise de Vendas")

# carregar os dados
dados = pd.read_csv("./vendas.csv")

# mostrar os primeiros dados
st.subheader("🔍 Primeiras linhas da base de dados")
st.dataframe(dados.head())

# mostrar estatísticas
st.subheader("📈 Estatísticas básicas")
st.write(dados.describe())

# criar gráfico de barras com total de vendas por região
st.subheader("📍 Total de Vendas por Região")
vendas_por_regiao = dados.groupby('Region')['Sales'].sum()

fig, ax = plt.subplots()
vendas_por_regiao.plot(kind="bar", ax=ax)
st.pyplot(fig)