import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import feedparser
from datetime import datetime

# 1. ESTILO RADAR Y MODO OSCURO TOTAL
st.set_page_config(layout="wide", page_title="SLP C4 INTELLIGENCE", page_icon="🚨")

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #000000; color: #00ff00; }
    .stMarkdown { font-family: 'Courier New', monospace; }
    
    /* Animación de Ticker (Barra de noticias) */
    .ticker-wrapper { width: 100%; overflow: hidden; background-color: #ff0000; color: white; padding: 5px; font-weight: bold; }
    .ticker-text { display: inline-block; white-space: nowrap; animation: ticker 30s linear infinite; }
    @keyframes ticker { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
    
    /* Tarjetas de Dependencias */
    .gov-card { border: 1px solid #00ff00; padding: 8px; margin-bottom: 5px; background: rgba(0,255,0,0.05); }
    .live-dot { height: 10px; width: 10px; background-color: #ff0000; border-radius: 50%; display: inline-block; animation: blink 1s infinite; }
    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0; } 100% { opacity: 1; } }
    </style>
    """, unsafe_allow_html=True)

# 2. CAPTURA DE DATOS GUBERNAMENTALES Y MUNICIPALES
def get_gov_intel():
    # Filtro específico para dependencias de SLP
    query = "(Ayuntamiento SLP OR SSPC SLP OR Gobierno del Estado SLP OR Protección Civil SLP) when:12h"
    feed = feedparser.parse(f"https://news.google.com/rss/search?q={query}&hl=es-419&gl=MX&ceid=MX:es-419")
    return feed.entries[:12]

# 3. INTERFAZ DE CABECERA
st.markdown("<div class='ticker-wrapper'><div class='ticker-text'>ALERTA: MONITOREO DE DEPENDENCIAS ESTATALES Y MUNICIPALES ACTIVO --- VIGILANCIA VIAL EN CARRETERA 57 --- REPORTES CIUDADANOS EN TIEMPO REAL --- ZONA METROPOLITANA SIN NOVEDADES MAYORES ---</div></div>", unsafe_allow_html=True)

col_h1, col_h2, col_h3 = st.columns([2,1,1])
with col_h1:
    st.markdown("## 📟 TERMINAL DE INTELIGENCIA SLP v3.0")
with col_h2:
    st.markdown(f"**SISTEMA:** <span class='live-dot'></span> EN VIVO", unsafe_allow_html=True)
with col_h3:
    st.write(f"**FECHA:** {datetime.now().strftime('%d/%m/%Y %H:%M')}")

# 4. DASHBOARD PRINCIPAL
c1, c2, c3 = st.columns([1.5, 1, 1])

with c1:
    st.markdown("### 🛰️ RADAR ESTATAL")
    # Mapa con marcadores dinámicos
    m = folium.Map(location=[22.5, -100.5], zoom_start=7, tiles='CartoDB dark_matter', zoom_control=False)
    
    # Añadiendo "Puntos de Interés" de Dependencias
    puntos = [
        [22.1565, -100.9855, "C4 Centro Histórico"],
        [22.1265, -101.0100, "Zona Industrial - Vigilancia"],
        [21.9833, -99.0167, "Base Huasteca - Activa"]
    ]
    for p in puntos:
        folium.Marker(location=[p[0], p[1]], tooltip=p[2], icon=folium.Icon(color='red', icon='info-sign')).add_to(m)
    
    st_folium(m, width="100%", height=500)

with c2:
    st.markdown("### 🏛️ GOBIERNO & MUNICIPIOS")
    st.caption("Actividad de Dependencias")
    gov_data = get_gov_intel()
    for entry in gov_data:
        st.markdown(f"""
            <div class='gov-card'>
                <span style='font-size:11px; color:#00ff00;'>>> REPORTE DETECTADO</span><br>
                <b style='font-size:13px;'>{entry.title[:70]}...</b><br>
                <a href='{entry.link}' style='color:#666; font-size:10px;'>ACCEDER AL ARCHIVO</a>
            </div>
        """, unsafe_allow_html=True)

with c3:
    st.markdown("### 📱 RADAR DE REDES")
    st.caption("Tendencias en San Luis Potosí")
    # Simulación de volumen de conversación por zona
    st.write("📍 **Capital:** ALTA")
    st.progress(0.9)
    st.write("📍 **Matehuala:** MEDIA")
    st.progress(0.4)
    st.write("📍 **Valles:** ALTA")
    st.progress(0.7)
    
    st.markdown("---")
    st.write("📊 **Términos más usados:**")
    st.code("1. Vialidad SLP\n2. Clima Huasteca\n3. Guardia Civil\n4. Carranza")

# Botón oculto para actualizar
if st.button('FORCE SYSTEM RELOAD'):
    st.rerun()
