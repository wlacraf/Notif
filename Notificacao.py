import streamlit as st
import pandas as pd

# Carrega o DataFrame a partir de um arquivo CSV
def carregar_dados(nome_arquivo):
    return pd.read_csv(nome_arquivo,encoding='ISO-8859-8')



    # Titulo do aplicativo
st.title("Mapa de Localizações com Pesos")

    # Carrega os dados
nome_arquivo = 'notificacao.csv'
df = carregar_dados(nome_arquivo)
#df['Peso'] = pd.to_numeric(df['Peso'], errors='coerce').fillna(0)

    # Verifica se o DataFrame não está vazio
        # Ajusta os tamanhos dos pontos baseado no peso
        # Esta é uma forma simples de fazer isso, pode ser adaptada conforme necessário
df['Peso']=df['Peso']*10   #.apply(lambda x: x * 0.1)  # Multiplica por 10 para aumentar a visibilidade
#st.write(df)
        # Mostra o mapa
st.map(df,size='Peso')

