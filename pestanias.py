import pandas as pd
import streamlit as st
import plotly.express as px

@st.cache_data
def load_data():
    return pd.read_csv('projectos.csv', encoding='latin1')
