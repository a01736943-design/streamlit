import streamlit as st

st.set_page_config(
    page_title= "Dashboard multi página",
    layout = "wide",
    initial_sidebar_state = "expanded" #collapsed
)

#definir paginas
home_page= st.Page(
    "streamlit/forvia/paginas/home.py",
#    "forvia/paginas/home.py",
    title="Home",
    #icon = ":material​/menu:"
)

projects_page= st.Page(
    "forvia/paginas/projects.py",
    title="Análsis de Projectos"
)

percentage_page= st.Page(
    "forvia/paginas/percentage.py",
    title="Análsis de Porcentajes"
)

mapa_page = st.Page(
    "forvia/paginas/mapa.py",
    title="Mapas"
)


#navegación

pg=st.navigation({
    "Inicio": [home_page],
    "Análsis":[projects_page, percentage_page],
    "Visualización": [mapa_page]
    })

#ejectutar
pg.run()