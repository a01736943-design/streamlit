import streamlit as st
import pandas as pd
from utils.data_loader import load_projects_data
from utils.functions import filter_projects

st.title("Análisis de proyectos")

df= load_projects_data()

with st.sidebar:
    st.markdown('### Filtros')
    estados= df['State'].dropna().unique().tolist()
    st.write(type(estados))
    estados_filtro= st.multiselect("Estado del projecto", estados, default=estados)

    areas= df['Geographical scope'].dropna().unique().tolist()
    areas_filtro= st.selectbox("Área geográfica",["Todas"] + areas)
    st.write(type(areas))
    st.markdown("---")
    st.info(f"Registros: {len(df)}")

    avance_min= st.slider("Avance mínimo (%)", 0, 100, 0)

df_filtrado, avg_progress = filter_projects(df, estados_filtro, areas_filtro, avance_min)


col1, col2, col3, col4 = st.columns(4) 
with col1:
    st.mertric("Projectos filtrados", len(df_filtrado))
with col2:
    st.metric("Avance promedio", f"{avg_progress:.1f}")
with col3:
    st.metric("Project mangers", df_filtrado['Project manager'].nunique())
with col4:
    st.metric("Ubicaciones", df_filtrado['Geographical scope'].nunique())

