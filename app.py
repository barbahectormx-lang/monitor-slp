import streamlit as st
import pandas as pd
import pydeck as pdk
import feedparser # Esta herramienta lee las noticias
from datetime import datetime

st.set_page_config(layout="wide", page_title="MONITOR SLP PRO", page_icon="🇲🇽")

# --- LECTOR DE NOTICIAS REALES DE SLP ---
def obtener_noticias():
    # Leemos el feed de Google News para San Luis Potosi
    url = "https://news.google.com/rss/search?q=San+Luis+Potosi+cuando:24h&hl=es-419&gl=MX&ceid=MX:es-419"
    feed = feedparser.parse(url)
    noticias = []
    for entry in feed.entries[:10]: # Solo las 10 más recientes
        noticias.append({
            'titulo': entry.title,
            'link': entry.link,
            'fecha': entry.published
        })
    return noticias

noticias_reales = obtener_noticias()

# --- INTERFAZ ---
st.title("🛰️ SISTEMA DE INTELIGENCIA SLP")

col1, col2 = st.columns([3, 1])

with col1:
    # Mapa configurado para que NO se vea negro
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/navigation-night-v1', # Estilo navegación nocturna
        initial_view_state=pdk.ViewState(
            latitude=22.1565,
            longitude=-100.9855,
            zoom=8,
            pitch=45,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=pd.DataFrame({'lat': [22.15], 'lon': [-100.98]}), # Punto central
                get_position='[lon, lat]',
                get_color='[255, 0, 0, 160]',
                get_radius=2000,
            ),
        ],
    ))

with col2:
    st.subheader("🔥 Tendencias Ahora")
    for n in noticias_reales:
        st.markdown(f"📌 **[{n['titulo']}]({n['link']})**")
        st.caption(f"Publicado: {n['fecha']}")
        st.write("---")

# Panel Lateral mejorado
st.sidebar.title("LOG DE EVENTOS")
st.sidebar.success("Conectado a Satélite: Activo")
st.sidebar.info(f"Último escaneo: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
