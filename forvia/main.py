import streamlit as st

st.set_page_config(
    page_title= "Dashboard multi página",
    layout = "wide",
    initial_sidebar_state = "expanded" #collapsed
)

#definir paginas
home_page= st.Page(
    "Paginas/home.py",
    title="Home",
    #icon = ":material​/menu:"
)

projects_page= st.Page(
    "Paginas/projects.py",
    title="Análsis de Projectos"
)

percentage_page= st.Page(
    "Paginas/percentage.py",
    title="Análsis de Porcentajes"
)

mapa_page = st.Page(
    "Paginas/mapa.py",
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