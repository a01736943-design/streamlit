import streamlit as st

#Titulo principal
st.title("Demostración de tipos de texto en Streamlit")
st.markdown("---")

st.header ("Introducción") #Encabezado
st.write("""
En Esta aplicacion mostraremos como **Streamlit** permite presentar distintos tipos de texto
para construir interfaces informativas en proyectos de **IA** y **analiticade datos**.
"""

)

st.subheader("Texto con Markdown")
st.markdown("""
Con **Markdown**, podemos dar formato al texto, por ejemplo:

- **Negritas** y *Cursivas*
-Lista con viñetas
- Citas y enlaces
- Tablas de datos
- Inclusión de emojis

> La analitica de datos combina estadisticas, programacion y visualizacion.
""")

st.caption("Tip: Markdown es ideal para agregar descripciones, explicaciones y notas informativas")
st.markdown("---")

st.header("Inclusión de fragmentos de código")
st.code("""
import pandas as pd

#Cargar datos
df = pd.read_csv("ventas.csv")
        
#Calcular metricas basicas
df.describe()
""")

st.subheader("Resolver la siguiente ecuación:  ")
st.latex(r' a+a r^1+a r^2+a r^3 r**2')