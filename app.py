import streamlit as st
import feedparser
from datetime import datetime

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(layout="wide", page_title="C4 SAN LUIS POTOSÍ", page_icon="🇲🇽")

st.markdown("""
    <style>
    body { background-color: #050505; color: #ffffff; }
    .stApp { background-color: #050505; }
    .header-title { font-family: 'Arial Black', sans-serif; color: #ff0000; text-align: center; }
    .panel-title { border-bottom: 2px solid #333; padding-bottom: 5px; color: #00ff00; font-family: monospace; }
    .news-card { background: #111; padding: 10px; border-left: 3px solid #ff0000; margin-bottom: 8px; font-size: 13px; }
    .gov-card { background: #0a192f; padding: 10px; border-left: 3px solid #0088ff; margin-bottom: 8px; font-size: 13px; }
    .social-card { background: #1a0b2e; padding: 10px; border-left: 3px solid #b700ff; margin-bottom: 8px; font-size: 13px; }
    a { color: #aaaaaa; text-decoration: none; }
    a:hover { color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. MOTORES DE BÚSQUEDA RSS (BLINDADOS CONTRA ERRORES) ---
def buscar_noticias(query):
    try:
        url = f"https://news.google.com/rss/search?q={query}&hl=es-419&gl=MX&ceid=MX:es-419"
        feed = feedparser.parse(url)
        return feed.entries[:6]
    except:
        return []

# --- 3. CABECERA ---
st.markdown("<h1 class='header-title'>📡 C4 ESTATAL: SAN LUIS POTOSÍ</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#00ff00; font-family:monospace;'>SISTEMA EN LÍNEA | ACTUALIZADO: {datetime.now().strftime('%H:%M:%S')} | ZONA METROPOLITANA, ALTIPLANO, MEDIA Y HUASTECA</p>", unsafe_allow_html=True)

# --- 4. RADARES EN VIVO (TRÁFICO Y CLIMA) ---
c_trafico, c_clima = st.columns(2)

with c_trafico:
    st.markdown("<h3 class='panel-title'>🚗 TRÁFICO Y VIALIDAD (EN VIVO)</h3>", unsafe_allow_html=True)
    # Radar oficial de Waze para SLP
    st.components.v1.html("""
        <iframe src="https://embed.waze.com/iframe?zoom=13&lat=22.1565&lon=-100.9855&ct=livemap" 
        width="100%" height="400" allowfullscreen style="border: 1px solid #333; border-radius: 5px;"></iframe>
    """, height=410)

with c_clima:
    st.markdown("<h3 class='panel-title'>⛈️ RADAR METEOROLÓGICO ESTATAL</h3>", unsafe_allow_html=True)
    # Radar oficial de Windy (Muestra lluvia/clima en todo el estado)
    st.components.v1.html("""
        <iframe width="100%" height="400" 
        src="https://embed.windy.com/embed.html?type=map&location=coordinates&metricRain=mm&metricTemp=%C2%B0C&metricWind=km/h&zoom=7&overlay=rain&product=ecmwf&level=surface&lat=22.156&lon=-100.985" 
        frameborder="0" style="border: 1px solid #333; border-radius: 5px;"></iframe>
    """, height=410)

st.markdown("<br>", unsafe_allow_html=True)

# --- 5. MONITORES DE INTELIGENCIA (NOTICIAS, GOBIERNO, REDES) ---
c_noticias, c_gobierno, c_redes = st.columns(3)

with c_noticias:
    st.markdown("<h3 class='panel-title'>📰 TENDENCIAS GLOBALES</h3>", unsafe_allow_html=True)
    noticias = buscar_noticias("San Luis Potosí when:12h")
    for n in noticias:
        st.markdown(f"<div class='news-card'><b>{n.title}</b><br><a href='{n.link}'>Leer reporte ></a></div>", unsafe_allow_html=True)

with c_gobierno:
    st.markdown("<h3 class='panel-title'>🏛️ DEPENDENCIAS Y GOBIERNO</h3>", unsafe_allow_html=True)
    # Busca específicamente cuentas de gobierno
    gobierno = buscar_noticias("(Gobierno de San Luis Potosí OR Ayuntamiento SLP OR Seguridad SLP OR Protección Civil SLP) when:24h")
    for g in gobierno:
        st.markdown(f"<div class='gov-card'><b>{g.title}</b><br><a href='{g.link}'>Ver boletín ></a></div>", unsafe_allow_html=True)

with c_redes:
    st.markdown("<h3 class='panel-title'>📱 RASTREO EN REDES SOCIALES</h3>", unsafe_allow_html=True)
    # Busca menciones virales o problemas sociales recientes
    redes = buscar_noticias('"San Luis Potosí" (viral OR redes sociales OR Twitter OR Facebook OR TikTok OR denuncia) when:24h')
    for r in redes:
        st.markdown(f"<div class='social-card'><b>{r.title}</b><br><a href='{r.link}'>Rastrear fuente ></a></div>", unsafe_allow_html=True)

# --- 6. BOTÓN DE SINCRONIZACIÓN ---
if st.button("🔄 FORZAR SINCRONIZACIÓN DE DATOS"):
    st.rerun()
