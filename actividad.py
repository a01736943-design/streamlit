import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Ania, LRI",
    page_icon="🎃",
    layout="centered",
    menu_items={
        "Get help": "https://www.faurecia-mexico.mx/acerca-de-nosotros/descubre-faurecia-mexico",
        "About": "a01736943, a01736943@tec.mx",
    }
)

st.title("Ania, LRI")


st.header("Python")
st.code("""
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy import stats
from statsmodels.multivariate.manova import MANOVA

# 
df= pd.read_csv('projectos_forvia.csv')

# 
df = df.fillna(method="bfill").fillna(method="ffill")
df.isnull().sum()

# 
sns.boxplot(data=df, x="Group", y="Percent complete")
plt.title("Distribución de Percent complete por Group")
plt.show()
""", language="python")


st.header("Fórmula")
st.latex(r"a^2 + b^2 = c^2")

st.header("licenciatura en el tec")
st.subheader("no tengo experiencia laboral pero si de social")
st.caption("ingeles español aprendiendo a codficar etc")
