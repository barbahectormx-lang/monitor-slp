# --- SECCIÓN EXTRA: SALA DE MONITORES AUDIOVISUALES (CCTV Y RADIO) ---
st.markdown("<br><h2 class='header-title'>🎥 INTERCEPTACIÓN DE MEDIOS Y CCTV</h2>", unsafe_allow_html=True)

# 1. Monitores de Video (4 Pantallas)
st.markdown("<h3 class='panel-title'>📺 MONITORES DE VIDEO EN VIVO</h3>", unsafe_allow_html=True)
v1, v2, v3, v4 = st.columns(4)

with v1:
    st.markdown("<div class='gov-card' style='text-align:center;'><b>CÁMARA 01: CENTRO HISTÓRICO</b></div>", unsafe_allow_html=True)
    # Ejemplo: Cámara en vivo de SLP (Webcams de México o similar vía YouTube)
    # Nota: Si el video cae, puedes cambiar la ID de YouTube (las letras después de embed/)
    st.components.v1.html("""
        <iframe width="100%" height="180" src="https://www.youtube.com/embed/live_stream?channel=UC2XvO4D1fJ8Ckq_N_E-_Bbg" frameborder="0" allowfullscreen></iframe>
    """, height=190)

with v2:
    st.markdown("<div class='gov-card' style='text-align:center;'><b>CÁMARA 02: NOTICIEROS LOCALES</b></div>", unsafe_allow_html=True)
    # Ejemplo: Canal de N+ (Televisa) o Noticieros locales en vivo
    st.components.v1.html("""
        <iframe width="100%" height="180" src="https://www.youtube.com/embed/live_stream?channel=UCXw1rY0A-P7m_x98E1P5Vow" frameborder="0" allowfullscreen></iframe>
    """, height=190)

with v3:
    st.markdown("<div class='gov-card' style='text-align:center;'><b>CÁMARA 03: CANAL ESTATAL</b></div>", unsafe_allow_html=True)
    st.components.v1.html("""
        <iframe width="100%" height="180" src="https://www.youtube.com/embed/live_stream?channel=UC2oXo_2I7E5m0eU0vQ_wXGA" frameborder="0" allowfullscreen></iframe>
    """, height=190)

with v4:
    st.markdown("<div class='gov-card' style='text-align:center;'><b>CÁMARA 04: RADAR VIAL TRACTO</b></div>", unsafe_allow_html=True)
    st.components.v1.html("""
        <iframe width="100%" height="180" src="https://www.youtube.com/embed/live_stream?channel=UC-2xQ7Yw5z1p4Zg3Q_3WlTw" frameborder="0" allowfullscreen></iframe>
    """, height=190)

# 2. Monitores de Radio Local
st.markdown("<h3 class='panel-title'>📻 FRECUENCIAS DE RADIO LOCALES</h3>", unsafe_allow_html=True)
r1, r2, r3, r4 = st.columns(4)

# Para la radio, usamos la etiqueta nativa de HTML5 <audio>. 
# Necesitas buscar el enlace que termina en .mp3 o .m3u8 de la estación.
with r1:
    st.markdown("<div class='social-card'><b>🎙️ FRECUENCIA 1: GlobalMedia (Ejemplo)</b><br><audio controls style='width:100%; height:30px;'><source src='https://stream.zeno.fm/t0zq8k8z5p8uv' type='audio/mpeg'></audio></div>", unsafe_allow_html=True)

with r2:
    st.markdown("<div class='social-card'><b>🎙️ FRECUENCIA 2: La Caliente SLP</b><br><audio controls style='width:100%; height:30px;'><source src='http://macslayer.com:8000/stream' type='audio/mpeg'></audio></div>", unsafe_allow_html=True)

with r3:
    st.markdown("<div class='social-card'><b>🎙️ FRECUENCIA 3: Candela FM</b><br><audio controls style='width:100%; height:30px;'><source src='http://198.50.156.92:8257/stream' type='audio/mpeg'></audio></div>", unsafe_allow_html=True)

with r4:
    st.markdown("<div class='social-card'><b>🎙️ FRECUENCIA 4: Radio Universidad</b><br><audio controls style='width:100%; height:30px;'><source src='http://radio.uaslp.mx:8000/live' type='audio/mpeg'></audio></div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
