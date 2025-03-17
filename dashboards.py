import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")  # Faz pegar a tela toda

# Carregar os dados
df = pd.read_csv('supermarket_sales.csv', sep=';', decimal=',')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# Criar coluna 'Month' no formato 'Ano - Mês'
df['Month'] = df['Date'].apply(lambda x: f'{x.year} - {x.month}')
month = st.sidebar.selectbox('Selecione o mês', df['Month'].unique())

# Filtrar os dados pelo mês selecionado
df_filtered = df[df['Month'] == month]

# Divisão da tela em colunas
col1, col2 = st.columns(2)  # Colunas para os gráficos 1 e 2
col3, col4, col5 = st.columns(3)  # Colunas para os gráficos 3, 4 e 5

# Primeiro gráfico: Faturamento por dia
fig_date = px.bar(df_filtered, x='Date', y='Total',
                  color='City', title='Faturamento por dia',
                  color_discrete_sequence=['#4AA6F7', '#ff7f0e', '#2ca02c'])
col1.plotly_chart(fig_date, use_container_width=True)

# Segundo gráfico: Faturamento por tipo de produto
fig_product = px.bar(df_filtered, x='Total', y='Product line',
                     title='Faturamento por tipo de produto',
                     orientation='h',
                     color='Product line',
                     color_discrete_sequence=[
                         '#4AA6F7', '#ff7f0e', '#2ca02c',
                         '#17becf', '#bcbd22', '#9467bd'
                     ])
col2.plotly_chart(fig_product, use_container_width=True)

# Terceiro gráfico: Faturamento por filial
city_total = df_filtered.groupby('City')[['Total']].sum().reset_index()
fig_city = px.bar(city_total, x='City', y='Total',
                  color='City', title='Faturamento por filial',
                  color_discrete_sequence=['#4AA6F7', '#9467bd', '#2ca02c'])
col3.plotly_chart(fig_city, use_container_width=True)

# Quarto gráfico: Faturamento por tipo de pagamento
fig_kind = px.pie(df_filtered, values='Total', names='Payment',
                  color='City', title='Faturamento por tipo de pagamento',
                  color_discrete_sequence=['#4AA6F7', '#9467bd', '#2ca02c'])
col4.plotly_chart(fig_kind, use_container_width=True)

# Quinto gráfico: Avaliação por filial
city_rating = df_filtered.groupby('City')[['Rating']].mean().reset_index()
fig_rating = px.bar(city_rating, x='City', y='Rating',
                    color='City', title='Avaliação por filial',
                    color_discrete_sequence=['#4AA6F7', '#bcbd22', '#2ca02c'])
col5.plotly_chart(fig_rating, use_container_width=True)
