import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import feedparser
from datetime import datetime

# 1. CONFIGURACIÓN TIPO "WAR ROOM"
st.set_page_config(layout="wide", page_title="SLP INTELLIGENCE", page_icon="🚨")

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #000000; color: #00ff00; }
    .stMarkdown { font-family: 'Courier New', monospace; }
    .ticker-wrapper { width: 100%; overflow: hidden; background-color: #ff0000; color: white; padding: 5px; }
    .ticker-text { display: inline-block; white-space: nowrap; animation: ticker 25s linear infinite; }
    @keyframes ticker { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
    .gov-card { border: 1px solid #333; padding: 10px; margin-bottom: 10px; background: #111; border-left: 4px solid #00ff00; }
    </style>
    """, unsafe_allow_html=True)

# 2. FUNCIÓN DE CAPTURA SEGURA
def get_intel(query):
    try:
        url = f"https://news.google.com/rss/search?q={query}+when:24h&hl=es-419&gl=MX&ceid=MX:es-419"
        feed = feedparser.parse(url)
        return feed.entries[:8]
    except:
        return []

# 3. CABECERA DINÁMICA
st.markdown("<div class='ticker-wrapper'><div class='ticker-text'>ESTADO DE VIGILANCIA ACTIVO --- MONITOREO DE DEPENDENCIAS ESTATALES --- ACTUALIZACIÓN EN TIEMPO REAL --- SAN LUIS POTOSÍ MÉXICO ---</div></div>", unsafe_allow_html=True)

col_h1, col_h2 = st.columns([3, 1])
with col_h1:
    st.markdown("## 📟 SISTEMA DE INTELIGENCIA SLP")
with col_h2:
    st.write(f"**LOG:** {datetime.now().strftime('%H:%M:%S')}")

# 4. COLUMNAS DE DATOS
c1, c2 = st.columns([1.8, 1])

with c1:
    st.markdown("### 🛰️ RADAR ESTATAL")
    # Mapa centrado en el estado
    m = folium.Map(location=[22.5, -100.5], zoom_start=7, tiles='CartoDB dark_matter', zoom_control=False)
    
    # Puntos estratégicos
    puntos = [[22.15, -100.98, "CAPITAL"], [21.98, -99.01, "HUASTECA"], [23.64, -100.64, "ALTIPLANO"]]
    for p in puntos:
        folium.CircleMarker(location=[p[0], p[1]], radius=10, color='red', fill=True, popup=p[2]).add_to(m)
    
    st_folium(m, width="100%", height=500)

with c2:
    st.markdown("### 🏛️ ACTIVIDAD GUBERNAMENTAL")
    noticias = get_intel("Gobierno San Luis Potosi OR Seguridad SLP")
    
    if not noticias:
        st.write("Esperando señal...")
    else:
        for n in noticias:
            st.markdown(f"""
                <div class='gov-card'>
                    <b style='color:white; font-size:13px;'>{n.title[:85]}...</b><br>
                    <a href='{n.link}' style='color:#00ff00; font-size:11px;'>VER REPORTE ORIGINAL ></a>
                </div>
            """, unsafe_allow_html=True)

# BOTÓN DE RECARGA
if st.button('REINICIAR ESCÁNER'):
    st.rerun()
