# --- 4. MONITORES DE VIDEO Y RADIO LOCALES (ANTI-CAÍDAS) ---
st.markdown("<h3 class='panel-title'>📺 VIDEOWALL: MEDIOS DE SAN LUIS POTOSÍ</h3>", unsafe_allow_html=True)

# Cuadrícula de 4 Televisiones usando el "Search Embed Hack" para garantizar que siempre haya video local reciente
tv1, tv2, tv3, tv4 = st.columns(4)

with tv1:
    st.markdown("<div class='media-box'><span style='color:red;'>● SEÑAL</span> <b>CANAL 7 SLP</b></div>", unsafe_allow_html=True)
    # Busca automáticamente lo último de Canal 7 SLP
    components.html('<iframe width="100%" height="200" src="https://www.youtube.com/embed?listType=search&list=Noticias+Canal+7+San+Luis+Potosi" frameborder="0" allowfullscreen></iframe>', height=210)

with tv2:
    st.markdown("<div class='media-box'><span style='color:red;'>● SEÑAL</span> <b>N+ (TELEVISA SLP)</b></div>", unsafe_allow_html=True)
    # Busca automáticamente lo último de N+ San Luis Potosí
    components.html('<iframe width="100%" height="200" src="https://www.youtube.com/embed?listType=search&list=N%2B+San+Luis+Potosi+Noticias" frameborder="0" allowfullscreen></iframe>', height=210)

with tv3:
    st.markdown("<div class='media-box'><span style='color:red;'>● SEÑAL</span> <b>CÓDIGO SAN LUIS</b></div>", unsafe_allow_html=True)
    # Busca reportes en video del portal Código San Luis
    components.html('<iframe width="100%" height="200" src="https://www.youtube.com/embed?listType=search&list=Codigo+San+Luis+En+Vivo" frameborder="0" allowfullscreen></iframe>', height=210)

with tv4:
    st.markdown("<div class='media-box'><span style='color:red;'>● SEÑAL</span> <b>EL EXPRÉS / PULSO</b></div>", unsafe_allow_html=True)
    # Busca reportajes de medios escritos locales
    components.html('<iframe width="100%" height="200" src="https://www.youtube.com/embed?listType=search&list=Periodico+Pulso+San+Luis+Potosi" frameborder="0" allowfullscreen></iframe>', height=210)

# Fila de Estaciones de Radio Locales (Usando widgets seguros de TuneIn y ZenoRadio para evitar bloqueos)
st.markdown("<br><p style='font-size:14px; color:#b700ff; margin-bottom:5px;'>📻 INTERCEPCIÓN DE RADIO ESTATAL</p>", unsafe_allow_html=True)
r1, r2, r3, r4 = st.columns(4)

with r1:
    st.markdown("<div style='text-align:center; font-size:12px;'><b>W Radio SLP</b></div>", unsafe_allow_html=True)
    # Widget seguro de TuneIn
    components.html('<iframe src="https://tunein.com/embed/player/s25072/" style="width:100%; height:100px;" scrolling="no" frameborder="no"></iframe>', height=105)

with r2:
    st.markdown("<div style='text-align:center; font-size:12px;'><b>Candela / Factor</b></div>", unsafe_allow_html=True)
    components.html('<iframe src="https://tunein.com/embed/player/s121980/" style="width:100%; height:100px;" scrolling="no" frameborder="no"></iframe>', height=105)

with r3:
    st.markdown("<div style='text-align:center; font-size:12px;'><b>La Caliente 97.7</b></div>", unsafe_allow_html=True)
    components.html('<iframe src="https://tunein.com/embed/player/s21532/" style="width:100%; height:100px;" scrolling="no" frameborder="no"></iframe>', height=105)

with r4:
    st.markdown("<div style='text-align:center; font-size:12px;'><b>Radio Universidad</b></div>", unsafe_allow_html=True)
    components.html('<iframe src="https://tunein.com/embed/player/s187121/" style="width:100%; height:100px;" scrolling="no" frameborder="no"></iframe>', height=105)

st.markdown("<hr style='border-color: #333;'>", unsafe_allow_html=True)
