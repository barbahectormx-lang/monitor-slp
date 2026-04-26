import streamlit as st
import feedparser
import urllib.parse
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

# --- 2. MOTOR RSS REPARADO ---
def buscar_noticias(query):
    # urllib.parse.quote asegura que los espacios y caracteres se conviertan a un formato web seguro (%20)
    query_segura = urllib.parse.quote(query)
    url = f"https://news.google.com/rss/search?q={query_segura}&hl=es-419&gl=MX&ceid=MX:es-419"
    
    try:
        feed = feedparser.parse(url)
        # Si la lista de noticias viene vacía, no dejamos el espacio en blanco
        if len(feed.entries) == 0:
            return [{"title": "📡 Escaneando fuentes locales... (Sin resultados recientes)", "link": url}]
        return feed.entries[:6]
    except:
        return [{"title": "⚠️ Enlace de comunicación interrumpido.", "link": "#"}]

# --- 3. CABECERA ---
st.markdown("<h1 class='header-title'>📡 C4 ESTATAL: SAN LUIS POTOSÍ</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#00ff00; font-family:monospace;'>SISTEMA EN LÍNEA | ACTUALIZADO: {datetime.now().strftime('%H:%M:%S')} | ZONA METROPOLITANA, ALTIPLANO, MEDIA Y HUASTECA</p>", unsafe_allow_html=True)

# --- 4. RADARES EN VIVO (TRÁFICO Y CLIMA) ---
c_trafico, c_clima = st.columns(2)

with c_trafico:
    st.markdown("<h3 class='panel-title'>🚗 TRÁFICO Y VIALIDAD (EN VIVO)</h3>", unsafe_allow_html=True)
    st.components.v1.html("""
        <iframe src="https://embed.waze.com/iframe?zoom=13&lat=22.1565&lon=-100.9855&ct=livemap" 
        width="100%" height="400" allowfullscreen style="border: 1px solid #333; border-radius: 5px;"></iframe>
    """, height=410)

with c_clima:
    st.markdown("<h3 class='panel-title'>⛈️ RADAR METEOROLÓGICO ESTATAL</h3>", unsafe_allow_html=True)
    st.components.v1.html("""
        <iframe width="100%" height="400" 
        src="https://embed.windy.com/embed.html?type=map&location=coordinates&metricRain=mm&metricTemp=%C2%B0C&metricWind=km/h&zoom=7&overlay=rain&product=ecmwf&level=surface&lat=22.156&lon=-100.985" 
        frameborder="0" style="border: 1px solid #333; border-radius: 5px;"></iframe>
    """, height=410)

st.markdown("<br>", unsafe_allow_html=True)

# --- 5. MONITORES DE INTELIGENCIA ---
c_noticias, c_gobierno, c_redes = st.columns(3)

with c_noticias:
    st.markdown("<h3 class='panel-title'>📰 TENDENCIAS GLOBALES</h3>", unsafe_allow_html=True)
    # Búsqueda general limpia
    noticias = buscar_noticias("San Luis Potosi noticias hoy")
    for n in noticias:
        # Se verifica si es un diccionario (el mensaje de error) o un objeto de feedparser
        titulo = n.get('title', n.title) if isinstance(n, dict) else n.title
        link = n.get('link', n.link) if isinstance(n, dict) else n.link
        st.markdown(f"<div class='news-card'><b>{titulo}</b><br><a href='{link}' target='_blank'>Leer reporte ></a></div>", unsafe_allow_html=True)

with c_gobierno:
    st.markdown("<h3 class='panel-title'>🏛️ DEPENDENCIAS Y GOBIERNO</h3>", unsafe_allow_html=True)
    # Búsqueda enfocada a comunicados, ayuntamiento y seguridad
    gobierno = buscar_noticias("Gobierno San Luis Potosi seguridad ayuntamiento comunicado")
    for g in gobierno:
        titulo = g.get('title', g.title) if isinstance(g, dict) else g.title
        link = g.get('link', g.link) if isinstance(g, dict) else g.link
        st.markdown(f"<div class='gov-card'><b>{titulo}</b><br><a href='{link}' target='_blank'>Ver boletín ></a></div>", unsafe_allow_html=True)

with c_redes:
    st.markdown("<h3 class='panel-title'>📱 RASTREO EN REDES SOCIALES</h3>", unsafe_allow_html=True)
    # Búsqueda enfocada a denuncias ciudadanas y contenido viral del estado
    redes = buscar_noticias("San Luis Potosi viral denuncia redes sociales")
    for r in redes:
        titulo = r.get('title', r.title) if isinstance(r, dict) else r.title
        link = r.get('link', r.link) if isinstance(r, dict) else r.link
        st.markdown(f"<div class='social-card'><b>{titulo}</b><br><a href='{link}' target='_blank'>Rastrear fuente ></a></div>", unsafe_allow_html=True)

# --- 6. BOTÓN DE SINCRONIZACIÓN ---
if st.button("🔄 FORZAR SINCRONIZACIÓN DE DATOS"):
    st.rerun()
