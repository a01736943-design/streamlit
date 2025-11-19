import streamlit as st
import pandas as pd
import numpy as np

# Configurar pagina
st.set_page_config(
    page_title= "Generador de data frames",
    page_icon = "📊",
    #layout= "wide",
    layout= "centered",
    menu_items = {
        "Get help": 'https://www.faurecia-mexico.mx/acerca-de-nosotros/descubre-faurecia-mexico',
        "About": "Dashboard profesional para gestión de proyectos",
    }
)

sheet_name ="WAR"

st.title("Visualización de proyectos")
dataframe= pd.read_excel("PRMSnow KPIs_062025_modified2.xlsx",
                         sheet_name= sheet_name)

st.dataframe(dataframe)

def convert_df(df):
    return df. to_csv().encode("utf-8")
csv=convert_df(dataframe)
st.download_button(
    label=(f"descargar datos como csv"),
    data=csv,
    file_name=(f"{sheet_name}" + ".csv"),
    mime="text/csv"
    )