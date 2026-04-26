import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import feedparser
from datetime import datetime

# Configuración de pantalla completa
st.set_page_config(layout="wide", page_title="MONITOR SLP", page_icon="🇲🇽")

# Estilo oscuro para la interfaz
st.markdown("<style>body {background-color: #0e1117; color: white;}</style>", unsafe_allow_html=True)

st.title("🛰️ SISTEMA DE INTELIGENCIA: SAN LUIS POTOSÍ")

# --- FUNCIÓN PARA NOTICIAS REALES DE SLP ---
def get_slp_news():
    # Buscamos noticias de las últimas 24h en San Luis Potosí
    feed_url = "https://news.google.com/rss/search?q=San+Luis+Potosi+when:24h&hl=es-419&gl=MX&ceid=MX:es-419"
    feed = feedparser.parse(feed_url)
    return feed.entries[:8] # Tomamos las 8 más recientes

# --- DISEÑO DE COLUMNAS ---
col_mapa, col_noticias = st.columns([2, 1])

with col_mapa:
    st.subheader("📍 Mapa de Eventos Recientes")
    # Crear el mapa base centrado en SLP
    # Usamos CartoDB Dark Matter para que se vea estilo "World Monitor" (Oscuro)
    m = folium.Map(location=[22.1565, -100.9855], zoom_start=8, tiles='CartoDB dark_matter')
    
    # Añadimos un marcador de ejemplo en la capital
    folium.CircleMarker(
        location=[22.1565, -100.9855],
        radius=10,
        color='red',
        fill=True,
        fill_color='red',
        popup='Zona de Monitoreo Central'
    ).add_to(m)

    # Renderizar el mapa
    st_folium(m, width=1000, height=500)

with col_noticias:
    st.subheader("🔥 Noticias y Tendencias")
    noticias = get_slp_news()
    
    if not noticias:
        st.write("Buscando señales de inteligencia...")
    else:
        for n in noticias:
            with st.expander(f"⚠️ {n.title[:60]}..."):
                st.write(n.title)
                st.caption(f"Publicado: {n.published}")
                st.markdown(f"[Leer reporte completo]({n.link})")

# --- BARRA LATERAL ---
st.sidebar.title("ESTADO DEL SISTEMA")
st.sidebar.info(f"📡 Satélite: ONLINE\n\n⏰ Actualizado: {datetime.now().strftime('%H:%M:%S')}")
st.sidebar.markdown("---")
st.sidebar.warning("Este monitor agrupa noticias locales automáticamente para el estado de San Luis Potosí.")
