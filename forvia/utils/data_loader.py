import streamlit as st
import pandas as pd

@st.cache_data
def load_percentage_data():
    return pd.read_csv('/Users/hijos/Desktop/Analitica Prof/Prof. Rigoberto/M2_Streamlit/Forvia/data/percentage_not_completed.csv')

@st.cache_data
def load_projects_data():
    df = pd.read_csv('/Users/hijos/Desktop/Analitica Prof/Prof. Rigoberto/M2_Streamlit/Forvia/data/projects.csv', encoding='latin1')
    df = df.iloc[:-2].copy()
    df['Percent complete']=pd.to_numeric(df['Percent complete'], errors='coerce')
    return df

