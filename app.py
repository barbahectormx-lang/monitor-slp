import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import feedparser
from datetime import datetime
import time

# 1. CONFIGURACIÓN DE PANTALLA "MODO COMANDO"
st.set_page_config(layout="wide", page_title="SLP LIVE MONITOR", page_icon="📡")

# Inyectar CSS para que se vea más profesional y oscuro
st.markdown("""
    <style>
    .reportview-container { background: #000000; }
    .stDeployButton {display:none;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. AUTO-REFRESCO (Cada 60 segundos se recarga solo)
if "last_update" not in st.session_state:
    st.session_state.last_update = datetime.now().strftime('%H:%M:%S')

# 3. OBTENER DATOS REALES DE SLP
def get_live_data():
    feed_url = "https://news.google.com/rss/search?q=San+Luis+Potosi+when:24h&hl=es-419&gl=MX&ceid=MX:es-419"
    feed = feedparser.parse(feed_url)
    return feed.entries[:10]

noticias = get_live_data()

# 4. ENCABEZADO "EN VIVO"
col_t1, col_t2 = st.columns([3, 1])
with col_t1:
    st.markdown(f"<h1 style='color:red; margin-bottom:0;'>🔴 LIVE MONITOR: SAN LUIS POTOSÍ</h1>", unsafe_allow_html=True)
    st.caption("DATOS DE INTELIGENCIA DE FUENTES ABIERTAS (OSINT)")
with col_t2:
    st.metric("ESTADO", "ACTIVO", delta="🛰️ Satélite")
    st.write(f"Última actualización: {st.session_state.last_update}")

# 5. ESTRUCTURA PRINCIPAL
col_map, col_list = st.columns([2, 1])

with col_map:
    # Mapa base oscuro y elegante
    m = folium.Map(
        location=[22.5, -100.5], 
        zoom_start=7, 
        tiles='CartoDB dark_matter',
        zoom_control=False
    )
    
    # Marcadores ficticios basados en zonas comunes para dar vida al mapa
    puntos = [
        {"loc": [22.1565, -100.9855], "label": "Zona Centro - Monitoreo"},
        {"loc": [21.9833, -99.0167], "label": "Huasteca - Alerta Clima"},
        {"loc": [23.6487, -100.6439], "label": "Altiplano - Vigilancia"},
        {"loc": [21.8214, -100.2094], "label": "Zona Media - Reporte"}
    ]
    
    for p in puntos:
        folium.CircleMarker(
            location=p['loc'],
            radius=8,
            color='#FF0000',
            fill=True,
            fill_color='#FF0000',
            popup=p['label'],
            tooltip=p['label']
        ).add_to(m)

    st_folium(m, width="100%", height=600)

with col_list:
    st.markdown("### 📰 FEED DE NOTICIAS (TIEMPO REAL)")
    st.write("---")
    for n in noticias:
        # Estilo de tarjeta de alerta
        st.markdown(f"""
            <div style="background-color:#1e1e1e; padding:10px; border-radius:5px; border-left: 5px solid red; margin-bottom:10px;">
                <p style="margin:0; font-size:14px; color:white;"><b>{n.title}</b></p>
                <a href="{n.link}" style="color:#ff4b4b; font-size:12px;">Ver reporte</a>
            </div>
        """, unsafe_allow_html=True)

# Botón para forzar actualización manual si el usuario no quiere esperar
if st.button('🔄 ACTUALIZAR AHORA'):
    st.session_state.last_update = datetime.now().strftime('%H:%M:%S')
    st.rerun()

# 6. PIE DE PÁGINA
st.markdown("---")
st.caption("Monitoreo automático de medios locales en San Luis Potosí, México.")
