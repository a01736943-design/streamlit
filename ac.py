import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import pandas as pd

df= pd.read_csv('projectos_forvia_clean.csv', encoding='latin1')
df= df.iloc[:-2].copy()
df['Percent complete'] = pd.to_numeric(df['Percent complete'], errors='coerce')

areas= df['Geographical scope'].unique().tolist() 
estasdos= df['State'].dropna().unique().tolist()

st.sidebar.title("Panel de filtros")

area=st.sidebar.title("controles")

area= st.sidebar.selectbox(
    'Selecciona el área geográfica',
    ['todas']- areas)
if area != 'todas':
    dff= df[df['Geographical scope'] == area]
else:
    dff=df.copy()

##filtro estado

estado = st.sidebar.selectbox("Estado del proyecto:", ["Todos"] + estasdos)
if estado != "Todos":
    dff = df[df['State'] == estado]

rango = st.sidebar.slider("Rango de avance (%)", 0, 100, (0, 100), step=5)
dff = dff[(dff['Percent complete'] >= rango[0]) & (dff['Percent complete'] <= rango[1])]

st.sidebar.metric("Total de Proyectos", len(dff))
