import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import feedparser
from pytrends.request import TrendReq
from datetime import datetime

# 1. CONFIGURACIÓN DE PANTALLA TIPO "WAR ROOM"
st.set_page_config(layout="wide", page_title="SLP INTELLIGENCE", page_icon="📡")

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #050505; }
    .stMarkdown { font-family: 'Monaco', monospace; }
    .trend-card { background-color: #111; border: 1px solid #333; padding: 10px; border-radius: 5px; margin-bottom: 5px; }
    .live-indicator { color: #ff0000; font-weight: bold; animation: blink 1s infinite; }
    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0; } 100% { opacity: 1; } }
    </style>
    """, unsafe_allow_html=True)

# 2. FUNCIONES DE CAPTURA DE DATOS
def get_slp_news():
    feed = feedparser.parse("https://news.google.com/rss/search?q=San+Luis+Potosi+when:24h&hl=es-419&gl=MX&ceid=MX:es-419")
    return feed.entries[:10]

def get_social_trends():
    try:
        pytrends = TrendReq(hl='es-MX', tz=360)
        # Obtenemos tendencias de búsqueda en tiempo real para México
        df = pytrends.trending_searches(pn='mexico')
        return df[0].tolist()[:10]
    except:
        return ["Seguridad SLP", "Tráfico Carretera 57", "Clima Huasteca", "Feria SLP"]

# 3. INTERFAZ SUPERIOR
col_header_1, col_header_2 = st.columns([4, 1])
with col_header_1:
    st.markdown("<h1><span class='live-indicator'>●</span> SLP GLOBAL MONITOR <span style='font-size:15px; color:#666;'>v2.0 PRO</span></h1>", unsafe_allow_html=True)
with col_header_2:
    if st.button('🔄 REFRESCAR SISTEMA'):
        st.rerun()

# 4. CUERPO DEL MONITOR (3 COLUMNAS)
col_map, col_trends, col_news = st.columns([1.5, 1, 1])

with col_map:
    st.markdown("### 🗺️ GEOLOCALIZACIÓN")
    m = folium.Map(location=[22.5, -100.5], zoom_start=7, tiles='CartoDB dark_matter', zoom_control=False)
    # Puntos de calor ficticios en zonas de interés
    for loc in [[22.15, -100.98], [21.98, -99.01], [23.64, -100.64]]:
        folium.Circle(location=loc, radius=15000, color='red', fill=True, opacity=0.3).add_to(m)
    st_folium(m, width="100%", height=550)

with col_trends:
    st.markdown("### 📱 TENDENCIAS SOCIALES")
    st.caption("Búsquedas y Redes en SLP/México")
    trends = get_social_trends()
    for t in trends:
        st.markdown(f"""
            <div class="trend-card">
                <span style="color:#00ff00;">#</span> <span style="color:white;">{t}</span>
                <br><span style="font-size:10px; color:#666;">Tendencia detectada hace poco</span>
            </div>
        """, unsafe_allow_html=True)

with col_news:
    st.markdown("### 📰 ÚLTIMOS REPORTES")
    st.caption("Fuentes: Periódicos y Boletines")
    noticias = get_slp_news()
    for n in noticias:
        with st.container():
            st.markdown(f"""
                <div style="border-left: 3px solid #ff0000; padding-left:10px; margin-bottom:15px;">
                    <a href="{n.link}" style="color:white; text-decoration:none; font-size:13px;"><b>{n.title[:80]}...</b></a>
                    <br><span style="font-size:11px; color:#ff4b4b;">{n.published[:16]}</span>
                </div>
            """, unsafe_allow_html=True)

# 5. FOOTER
st.markdown("---")
st.markdown(f"<p style='text-align: center; color: #444;'>SISTEMA DE MONITOREO ACTIVO | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | SAN LUIS POTOSÍ, MÉXICO</p>", unsafe_allow_html=True)
