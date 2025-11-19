import streamlit as st
from utils.data_loader import load_projects_data
from utils.functions import map_projects
from streamlit_folium import st_folium
import folium

# Cargar datos
df = load_projects_data()
df_coords = map_projects(df, 'Geographical scope')

st.map(df_coords[['lat','lon']])

map_center = [df_coords['lat'].mean(), df_coords['lon'].mean()]
m = folium.Map(location=map_center, zoom_start=2)

for _, row in df_coords.iterrows():
    folium.Marker(
        [row['lat'], row['lon']],
        popup=f"{row['Project Name']} - {row['Geographical scope']}"
    ).add_to(m)


st_folium(m, width=800, height=500)

