import streamlit as st
import pandas as pd
from utils.data_loader import load_percentage_data
from utils.functions import filter_percentage

st.title("Análsis de porcentaje")

df= load_percentage_data()

with st.sidebar:
    st.markdown('### Filtros')
    regiones= df['Region'].unique().tolist()
    region_filtro= st.multiselect("Región", regiones, default=regiones)

    grupos= df['Group'].unique().tolist()
    grupo_filtro= st.selectbox("Grupo",["Todos"] + grupos)
    st.markdown("---")
    st.info(f"Registros: {len(df)}")


df_filtrado = filter_percentage(df, region_filtro, grupo_filtro)

col1, col2 = st.columns([0.4, 0.6]) 
with col1:
    st.header("Resultados")

with col2:
    colu1, colu2, colu3 = st.columns(3)

    with colu1: 
        st.metric("Registros", len(df_filtrado), border=True)

    with colu2: 
        st.metric("Promedio valor", f"{df_filtrado['valor'].mean():.2%}", border=True, delta="1.2")
    
    with colu3: 
        st.metric("Semanas (CW)", df_filtrado['CW'].nunique(), border=True)
