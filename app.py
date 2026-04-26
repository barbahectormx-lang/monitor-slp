import streamlit as st
import pandas as pd
import pydeck as pdk
from datetime import datetime

# Configuración visual de la página
st.set_page_config(layout="wide", page_title="MONITOR SLP", page_icon="🇲🇽")

# Estilo de mapa oscuro tipo World Monitor
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stTitle { color: #ff4b4b; font-family: 'Courier New'; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛰️ SISTEMA DE MONITOREO SAN LUIS POTOSÍ")
st.subheader("Inteligencia de Fuentes Abiertas en Tiempo Real")

# --- DATOS DE EJEMPLO (Esto es lo que verás en el mapa) ---
# Aquí puedes editar los textos entre comillas para cambiar las alertas
datos_alertas = pd.DataFrame({
    'lat': [22.1565, 22.1450, 21.9833, 22.4883, 21.4833],
    'lon': [-100.9855, -101.0100, -99.0167, -100.6333, -98.8833],
    'evento': ['Bloqueo Vial - Carranza', 'Alerta de Lluvia - Centro', 'Incendio Forestal - Huasteca', 'Accidente - Matehuala', 'Reporte Ciudadano - Xilitla'],
    'gravedad': [100, 50, 200, 150, 80] # Tamaño del punto
})

# --- EL MAPA ---
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/dark-v10',
    initial_view_state=pdk.ViewState(
        latitude=22.1565,
        longitude=-100.9855,
        zoom=7,
        pitch=45,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=datos_alertas,
            get_position='[lon, lat]',
            get_color='[255, 75, 75, 180]',
            get_radius='gravedad * 100',
        ),
        pdk.Layer(
            'TextLayer',
            data=datos_alertas,
            get_position='[lon, lat]',
            get_text='evento',
            get_color=[255, 255, 255],
            get_size=16,
            get_alignment_baseline="'bottom'",
        )
    ],
))

# --- PANEL LATERAL ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/854/854878.png", width=100)
st.sidebar.title("LOG DE EVENTOS")
st.sidebar.info(f"Última actualización: {datetime.now().strftime('%H:%M:%S')}")

for i, row in datos_alertas.iterrows():
    st.sidebar.warning(f"⚠️ {row['evento']}")

st.sidebar.markdown("---")
st.sidebar.write("Desarrollado para monitoreo estatal en San Luis Potosí.")
