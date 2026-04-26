import streamlit as st
import feedparser
import urllib.parse
from datetime import datetime
import streamlit.components.v1 as components

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(layout="wide", page_title="C4 SAN LUIS POTOSÍ", page_icon="🚨")

st.markdown("""
    <style>
    body { background-color: #050505; color: #ffffff; }
    .stApp { background-color: #050505; }
    .header-title { font-family: 'Arial Black', sans-serif; color: #ff0000; text-align: center; }
    .panel-title { border-bottom: 2px solid #333; padding-bottom: 5px; color: #00ff00; font-family: monospace; font-size: 18px; margin-top: 20px;}
    .news-card { background: #111; padding: 10px; border-left: 3px solid #ff0000; margin-bottom: 8px; font-size: 13px; }
    .gov-card { background: #0a192f; padding: 10px; border-left: 3px solid #0088ff; margin-bottom: 8px; font-size: 13px; }
    .social-card { background: #1a0b2e; padding: 10px; border-left: 3px solid #b700ff; margin-bottom: 8px; font-size: 13px; }
    .media-box { background: #111; padding: 5px; border: 1px solid #333; text-align: center; border-radius: 5px; }
    a { color: #aaaaaa; text-decoration: none; }
    a:hover { color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. MOTOR RSS BLINDADO ---
def buscar_noticias(query, limite=6):
    query_segura = urllib.parse.quote(query)
    url = f"https://news.google.com/rss/search?q={query_segura}&hl=es-419&gl=MX&ceid=MX:es-419"
    try:
        feed = feedparser.parse(url)
        if len(feed.entries) == 0:
            return [{"title": "📡 Escaneando... (Sin datos recientes)", "link": url}]
        return feed.entries[:limite]
    except:
        return [{"title": "⚠️ Enlace interrumpido.", "link": "#"}]

# --- 3. CABECERA ---
st.markdown("<h1 class='header-title'>📡 C4 ESTATAL: SAN LUIS POTOSÍ</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#00ff00; font-family:monospace;'>SISTEMA EN LÍNEA | ACTUALIZADO: {datetime.now().strftime('%H:%M:%S')} | ESTADO DE SAN LUIS POTOSÍ</p>", unsafe_allow_html=True)

# --- 4. MONITORES DE VIDEO Y RADIO EN VIVO 24/7 ---
st.markdown("<h3 class='panel-title'>📺 VIDEOWALL DE MONITOREO (24/7)</h3>", unsafe_allow_html=True)

# Cuadrícula de 4 Televisiones (Noticias Nacionales 24/7 para que nunca esté en negro)
tv1, tv2, tv3, tv4 = st.columns(4)

with tv1:
    st.markdown("<div class='media-box'><span style='color:red;'>● LIVE</span> <b>MILENIO TV</b></div>", unsafe_allow_html=True)
    components.html('<iframe width="100%" height="200" src="https://www.youtube.com/embed/live_stream?channel=UCxw6XCA0-vS_BOPi_FvA2fA&autoplay=1&mute=1" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>', height=210)

with tv2:
    st.markdown("<div class='media-box'><span style='color:red;'>● LIVE</span> <b>N+ FORO TV</b></div>", unsafe_allow_html=True)
    components.html('<iframe width="100%" height="200" src="https://www.youtube.com/embed/live_stream?channel=UC1YaTQCjG_B1n2L1Lz_I0Mw&autoplay=1&mute=1" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>', height=210)

with tv3:
    st.markdown("<div class='media-box'><span style='color:red;'>● LIVE</span> <b>ADN 40</b></div>", unsafe_allow_html=True)
    components.html('<iframe width="100%" height="200" src="https://www.youtube.com/embed/live_stream?channel=UCg2H2oU7_r9-yQn4R9A2N6A&autoplay=1&mute=1" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>', height=210)

with tv4:
    st.markdown("<div class='media-box'><span style='color:red;'>● LIVE</span> <b>MULTIMEDIOS</b></div>", unsafe_allow_html=True)
    components.html('<iframe width="100%" height="200" src="https://www.youtube.com/embed/live_stream?channel=UCY4U02yq8_2uD-lDccFp3uQ&autoplay=1&mute=1" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>', height=210)

# Fila de Estaciones de Radio (Usando streams de YouTube para garantizar funcionamiento)
st.markdown("<br><p style='font-size:14px; color:#b700ff; margin-bottom:5px;'>📻 RADIO NACIONAL DE EMERGENCIA / NOTICIAS</p>", unsafe_allow_html=True)
r1, r2, r3, r4 = st.columns(4)

with r1:
    st.markdown("<div style='text-align:center; font-size:12px;'><b>Radio Fórmula</b></div>", unsafe_allow_html=True)
    components.html('<iframe width="100%" height="60" src="https://www.youtube.com/embed/live_stream?channel=UCmD3N0Jc2F4B3Y6L-n9m7wQ" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>', height=65)

with r2:
    st.markdown("<div style='text-align:center; font-size:12px;'><b>MVS Noticias</b></div>", unsafe_allow_html=True)
    components.html('<iframe width="100%" height="60" src="https://www.youtube.com/embed/live_stream?channel=UCXw11m2gMv-ZAR6R3bZXXlA" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>', height=65)

with r3:
    st.markdown("<div style='text-align:center; font-size:12px;'><b>Aristegui En Vivo</b></div>", unsafe_allow_html=True)
    components.html('<iframe width="100%" height="60" src="https://www.youtube.com/embed/live_stream?channel=UCbF_V7xNfXy1T66zV3lBngg" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>', height=65)

with r4:
    st.markdown("<div style='text-align:center; font-size:12px;'><b>Imagen Radio</b></div>", unsafe_allow_html=True)
    components.html('<iframe width="100%" height="60" src="https://www.youtube.com/embed/live_stream?channel=UC1v-HIfmO_2e06180X5vjAA" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>', height=65)


st.markdown("<hr style='border-color: #333;'>", unsafe_allow_html=True)

# --- 5. RADARES EN VIVO (TRÁFICO Y CLIMA) ---
c_trafico, c_clima = st.columns(2)

with c_trafico:
    st.markdown("<h3 class='panel-title'>🚗 TRÁFICO Y VIALIDAD (EN VIVO)</h3>", unsafe_allow_html=True)
    st.components.v1.html("""
        <iframe src="https://embed.waze.com/iframe?zoom=13&lat=22.1565&lon=-100.9855&ct=livemap" 
        width="100%" height="350" allowfullscreen style="border: 1px solid #333; border-radius: 5px;"></iframe>
    """, height=360)

with c_clima:
    st.markdown("<h3 class='panel-title'>⛈️ RADAR METEOROLÓGICO</h3>", unsafe_allow_html=True)
    st.components.v1.html("""
        <iframe width="100%" height="350" 
        src="https://embed.windy.com/embed.html?type=map&location=coordinates&metricRain=mm&metricTemp=%C2%B0C&metricWind=km/h&zoom=7&overlay=rain&product=ecmwf&level=surface&lat=22.156&lon=-100.985" 
        frameborder="0" style="border: 1px solid #333; border-radius: 5px;"></iframe>
    """, height=360)

st.markdown("<br>", unsafe_allow_html=True)

# --- 6. MONITORES DE INTELIGENCIA (NOTICIAS Y REDES) ---
c_noticias, c_gobierno, c_redes = st.columns(3)

with c_noticias:
    st.markdown("<h3 class='panel-title'>📰 NOTICIAS LOCALES</h3>", unsafe_allow_html=True)
    noticias = buscar_noticias("San Luis Potosi noticias", 8)
    for n in noticias:
        titulo = n.get('title', n.title) if isinstance(n, dict) else n.title
        link = n.get('link', n.link) if isinstance(n, dict) else n.link
        st.markdown(f"<div class='news-card'><b>{titulo}</b><br><a href='{link}' target='_blank'>Leer reporte ></a></div>", unsafe_allow_html=True)

with c_gobierno:
    st.markdown("<h3 class='panel-title'>🏛️ GOBIERNO Y DEPENDENCIAS</h3>", unsafe_allow_html=True)
    gobierno = buscar_noticias("Gobierno San Luis Potosi OR Seguridad Pública SLP OR Ayuntamiento SLP OR Protección Civil SLP", 8)
    for g in gobierno:
        titulo = g.get('title', g.title) if isinstance(g, dict) else g.title
        link = g.get('link', g.link) if isinstance(g, dict) else g.link
        st.markdown(f"<div class='gov-card'><b>{titulo}</b><br><a href='{link}' target='_blank'>Ver boletín ></a></div>", unsafe_allow_html=True)

with c_redes:
    st.markdown("<h3 class='panel-title'>🔥 TENDENCIAS Y REDES SOCIALES</h3>", unsafe_allow_html=True)
    
    st.markdown("<p style='font-size:12px; color:#b700ff; margin-bottom:0;'>📈 TEMAS EXPLOSIVOS (Últimas 24h)</p>", unsafe_allow_html=True)
    components.html("""
        <script type="text/javascript" src="https://ssl.gstatic.com/trends_nrtr/3620_RC01/embed_loader.js"></script>
        <script type="text/javascript">
          trends.embed.renderExploreWidget("RELATED_QUERIES", {"comparisonItem":[{"keyword":"San Luis Potosi","geo":"MX-SLP","time":"now 1-d"}],"category":0,"property":""}, {"exploreQuery":"date=now%201-d&geo=MX-SLP&q=San%20Luis%20Potosi","guestPath":"https://trends.google.com:443/trends/embed/"});
        </script>
    """, height=300)

    st.markdown("<p style='font-size:12px; color:#b700ff; margin-bottom:0;'>📱 POSTEOS RECIENTES</p>", unsafe_allow_html=True)
    redes = buscar_noticias('"San Luis Potosí" site:twitter.com OR site:tiktok.com OR site:facebook.com', 4)
    for r in redes:
        titulo = r.get('title', r.title) if isinstance(r, dict) else r.title
        link = r.get('link', r.link) if isinstance(r, dict) else r.link
        st.markdown(f"<div class='social-card'><b>{titulo}</b><br><a href='{link}' target='_blank'>Ver publicación original ></a></div>", unsafe_allow_html=True)

# --- 7. BOTÓN DE RECARGA ---
if st.button("🔄 ACTUALIZAR SISTEMA C4"):
    st.rerun()
