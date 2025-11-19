import streamlit as st
import pandas as pd 
import plotly.express as px
import numpy as np

st.title("Widgets interactivos de Streamlit con proyectos reales")

df= pd.read_csv('projectos_forvia_clean.csv', encoding='latin1')
df['Percent complete'] = pd.to_numeric(df['Percent complete'], errors='coerce')

#Creación de variables para los widgets
areas = df['Geographical scope'].unique().tolist()
estados = df['State'].dropna().unique().tolist()
managers = df['Project manager'].dropna().unique().tolist()

st.markdown('### Checkbox: Mostrar tabla')
if st.checkbox('¿Mostrar tabla de los primeros proyectos?'):
    st.dataframe(df.head(10))

st.markdown('### Radio: Eleguir estado del proyecto')
estadi_seleccionado=st.radio(
    'Slecciona el estado del proyecto: ',
    options= estados,
    horizontal=True #Coloca los radiositems de forma horizontal
)
st.write(f"Mostrando los proyectos cn estado: **{estadi_seleccionado}**")
st.dataframe(df[df['State'] == estadi_seleccionado][['Number','Project Name', 'Percent complete']].head(5))


st.markdown('### Selectbox: Filtra por Area/ Ubicación')
area_elegida = st.selectbox(
    'Filtra los proyectos por área',
    options= areas
)

df_filtrado = df[df['Geographical scope'] == area_elegida]
st.write(f"Proyectos en el area seleccionada: *{area_elegida}*")
st.dataframe(df_filtrado[['Number', 'Project Name', 'Percent complete', 'Project manager']])

st.markdown('### Multiselected: Sección múltiple de Project Managers')
pms = st.multiselect(
    'Selecciona uno o más Project Managers: ',
    options= managers,
    default=managers[:2]
)

df_pms = df[df['Project manager'].isin(pms)]
st.write(f"Proyectos a cargo de {', '.join(pms)}:")
st.dataframe(df_pms[['Number', 'Project Name', 'Percent complete', 'Project manager']].head(8))

st.markdown('### Slider: rango del proceso')
min_prog, max_prog = st.slider(
    'filtra proyectos por rango',
    0,100, (0, 50), step=5
)
df_rango=df[(df['Percent complete']>= min_prog) & (df['Percent complete']<= max_prog)]
st.write(f'mostrando {len(df_rango)} proyectos de avance entre {min_prog}% y {max_prog}%')
st.dataframe(df_rango[['Number', 'Project Name', 'Percent complete']].head(10))

st.markdown('### select slider: evaluaciond e desempeño')
opciones= ['malo', 'reguar', 'aceptable', 'bueno', 'excelente']
desepeño= st.select_slider(
    'como clsificarias el avance promedio de estos proyectos',
    options= opciones,
    value='bueno'
)
st.success(f'evaluacion seleccionada:**{desepeño}**')

st.markdown("---")
st.subheader("grafica depende de los filtros ")
if not df_filtrado.empty:
    fig=px.histogram(df_filtrado, x='Percent complete', nbins=10,
                     title=f"distribucion del avance en {area_elegida}")
    st.plotly_chart(fig)

st.markdown('### text imput busqueda flexible')
buscar= st.text_input('buscar palabra clave')
if buscar:
    resultados= df[df['Project Name'].str.contains(buscar, case=False, na=False)]
    st.write(f'resultados para {buscar}')
    st.dataframe(resultados[['Number','Project Name', 'Percent complete']].head(5))

st.markdown('### number imput: filtro de progreso minimo')
minimo= st.number_input('progreso minimo de proyecyto', min_value=0, )
df_filtrado=df[df['Percent complete']>=minimo]
st.write(f'mostranso proyectos con progreso >= **{minimo}%**')

st.markdown('### selecionar columnas eje x y y')
numericnum=['Percent complete']
categoricalop=[c for c in ['Project manager', 'Project size', 'Project type', 'State', 'Geographical scope']]
ejex=st.selectbox('selecciona para x', numericnum + categoricalop, index=0 )
ejey=st.selectbox('selecciona para y', numericnum, index=0 )

if ejex and ejey:
    st.markdown(f'### grafica: {ejey} vs {ejex}')
    if ejex in numericnum and ejey in numericnum:
        st.plotly_chart(px.scatter(df,x=ejex,y=ejey, title= f'{ejey} vs {ejex}'))
    elif ejex in categoricalop and ejey in numericnum:
        st.plotly_chart(px.box(df,x=ejex,y=ejey, title= f'{ejey} vs {ejex}'))
    elif ejex in numericnum and ejey in categoricalop:
        st.plotly_chart(px.scatter(df,x=ejex,y=ejey, title= f'{ejey} vs {ejex}'))
    else:
        st.warning("seleciona al menos un eje numerico")
    st.markdown("---")
    st.caption("demostracion de widgets con projectos reales")

