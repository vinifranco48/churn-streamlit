import streamlit as st
import pandas as pd 
import plotly.express as px

# Definindo o título da página
st.title('Análise de Churn')

# Supondo que 'df' seja o DataFrame que contém seus dados
df = st.session_state["data"]

# Dividir a tela em colunas
col1, col2 = st.columns(2)  
col3, col4 = st.columns(2)  

# Criar o gráfico de distribuição do churn por idade
fig_churn_age = px.histogram(df, x='Age', color='Exited', title='Churn por Idade', labels={"Age": "Idade", "Exited": "Churn"})
col1.plotly_chart(fig_churn_age, use_container_width=True)

# Criar o gráfico de barras para exibir o churn por país
country_churn = df.groupby("Geography")[["Exited"]].mean().reset_index()
fig_churn_country = px.bar(country_churn, x="Geography", y="Exited",
                           labels={"Geography": "País", "Exited": "Churn Médio"})
col2.plotly_chart(fig_churn_country, use_container_width=True)

# Criar o histograma para analisar o churn por credit score
fig_churn_creditscore = px.histogram(df, x='CreditScore', color='Exited', title='Churn por Credit Score', 
                                     labels={"CreditScore": "Pontuação de Crédito", "Exited": "Churn"})
col3.plotly_chart(fig_churn_creditscore, use_container_width=True)

# Criar o gráfico de pizza para exibir o churn por gênero
gender_churn = df.groupby("Gender")[["Exited"]].mean().reset_index()
fig_churn_gender_pie = px.pie(gender_churn, values="Exited", names="Gender",
                              title="Churn por Gênero")
col4.plotly_chart(fig_churn_gender_pie, use_container_width=True)
