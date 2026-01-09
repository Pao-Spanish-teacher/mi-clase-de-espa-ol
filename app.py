import streamlit as st
from gtts import gTTS
import os

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Pao- Spanish- Teacher", page_icon="🎓", layout="wide")

# --- 2. DICCIONARIO MAESTRO ---
DATOS_TEMAS = {
    "1. Saludos y Despedidas": {
        "video": "https://www.youtube.com/watch?v=hll10VBLFoQ", 
        "video2": "https://www.youtube.com/watch?v=84FNM-Ni-6U", 
        "video3": "https://www.youtube.com/watch?v=4txmiiR10wM",
        "cuento": "https://www.youtube.com/watch?v=yhH8rwpEHRo",
        "pdf": "minilibro Saludos.pdf", 
        "frases": ["Buenos días", "¿Cómo estás?", "Mucho gusto", "Hasta mañana"],
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. ¿Cómo se llama la niña que juega en la arena?", "o": ["María", "Brisa", "Ana"], "r": "Brisa"},
                {"p": "2. ¿Cuál es la primera palabra que usa Río?", "o": ["Adiós", "Gracias", "Hola"], "r": "Hola"},
                {"p": "3. ¿Qué edad mencionan tener ambos niños?", "o": ["5 años", "7 años", "10 años"], "r": "5 años"},
                {"p": "4. ¿Qué frase usan después de presentarse?", "o": ["De nada", "Mucho gusto", "Perdón"], "r": "Mucho gusto"},
                {"p": "5. ¿Qué palabra usan para despedirse?", "o": ["Hola", "Adiós", "Por favor"], "r": "Adiós"},
                {"p": "6. ¿Qué estaba construyendo Brisa?", "o": ["Una casa", "Un castillo de arena", "Un túnel"], "r": "Un castillo de arena"},
                {"p": "7. ¿En qué lugar se encuentran los niños?", "o": ["En la escuela", "En un parque", "En la playa"], "r": "En un parque"},
                {"p": "8. Si alguien te pregunta cómo estás, respondes:", "o": ["¡Qué mal!", "Estoy bien, gracias", "No quiero hablar"], "r": "Estoy bien, gracias"},
                {"p": "9. Si es de mañana, debes decir:", "o": ["Buenas noches", "Buenos días", "Hasta luego"], "r": "Buenos días"},
                {"p": "10. ¿Cómo se llama el niño?", "o": ["Mar", "Río", "Lago"], "r": "Río"}
            ],
            "completar": [
                {"p": "11. Cuando Río quiere saber cómo se siente su amiga, pregunta: '¿Cómo __________?'", "r": "estás"},
                {"p": "12. Para conocer el nombre de la niña, el niño pregunta: '¿Cómo te __________?'", "r": "llamas"},
                {"p": "13. Río le cuenta a Brisa el lugar donde reside diciendo: 'Yo vivo en la __________'", "r": "ciudad"},
                {"p": "14. Para pedir algo de forma educada, siempre debemos usar la frase: '__________ favor'", "r": "Por"},
                {"p": "15. Si los niños se volvieran a ver al día siguiente, podrían despedirse diciendo: 'Hasta __________'", "r": "mañana"},
                {"p": "16. Al recibir un cumplido o una ayuda, la palabra mágica es: '__________'", "r": "Gracias"},
                {"p": "17. Brisa y Río decidieron que a partir de ese momento serían muy buenos __________", "r": "amigos"},
                {"p": "18. Si saludas a alguien por la tarde, la expresión correcta es 'Buenas __________'", "r": "tardes"},
                {"p": "19. Cuando te presentan a alguien dices 'Encantado' o 'Mucho __________'", "r": "gusto"},
                {"p": "20. El nombre de la niña es __________ y el nombre del niño es Río.", "r": "Brisa"}
            ]
        }
    },
    "2. Los Números (0-100)": {"video": "https://www.youtube.com/watch?v=nxMBJQAE2ZU", "pdf": "Minilibros Los números en español (0-100).pdf", "frases": ["Diez", "Cincuenta"]},
    "3. Los Colores": {"video": "https://www.youtube.com/watch?v=UF5HWnCrAU8", "pdf": "Minilibro Los colores en español.pdf"},
    "4. Días, Meses y Estaciones": {
        "video": "https://www.youtube.com/watch?v=T9fvfbMQn2I", 
        "cuento": "https://www.youtube.com/watch?v=h1K6BKCX6g8",
        "pdf": "Minilibro Los días, los meses y las estaciones.pdf", 
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. ¿Cuál es el primer mes del año?", "o": ["Febrero", "Enero", "Marzo"], "r": "Enero"},
                {"p": "2. ¿Cuál es el mes más corto del año?", "o": ["Abril", "Febrero", "Junio"], "r": "Febrero"},
                {"p": "3. ¿En qué mes se celebra la Navidad?", "o": ["Noviembre", "Octubre", "Diciembre"], "r": "Diciembre"},
                {"p": "4. ¿Qué mes sigue después de agosto?", "o": ["Septiembre", "Julio", "Octubre"], "r": "Septiembre"},
                {"p": "5. ¿Cuál es el mes número seis del año?", "o": ["Mayo", "Junio", "Julio"], "r": "Junio"},
                {"p": "10. ¿Cuál es el último mes del año?", "o": ["Octubre", "Noviembre", "Diciembre"], "r": "Diciembre"}
            ],
            "completar": [
                {"p": "11. El mes que está entre marzo y mayo se llama __________.", "r": "Abril"},
                {"p": "15. Un año completo tiene un total de __________ meses.", "r": "doce"},
                {"p": "20. El mes número siete del año es __________.", "r": "Julio"}
            ]
        }
    }
}

# --- 3. SEGURIDAD ---
CONTRASEÑA = "pao_premium"
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("🎓 Academia Pao- Spanish- Teacher")
    clave = st.text_input("Clave de alumno:", type="password")
    if st.button("Ingresar"):
        if clave == CONTRASEÑA:
            st.session_state.auth = True
            st.rerun()
        else: st.error("❌ Clave incorrecta")
    st.stop()

# --- 4. MENÚ LATERAL ---
with st.sidebar:
    st.title("Pao- Spanish")
    menu = st.radio("Navegación:", ["Inicio", "Gramática Española", "Lecciones A1", "Contacto"])
    if st.button("Cerrar Sesión"):
        st.session_state.auth = False
        st.rerun()

# --- 5. SECCIONES ---

if menu == "Inicio":
    st.title("¡Bienvenida a tu Academia! ✨")
    st.write("Selecciona una sección en el menú lateral.")

elif menu == "Gramática Española":
    st.title("📖 Gramática Española")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("1. El Alfabeto"); st.video("https://www.youtube.com/watch?v=NMgN5gsvhWk") 
        st.subheader("3. El Género"); st.video("https://www.youtube.com/watch?v=FSqRurjGIqw")
    with c2:
        st.subheader("2. Preguntas Comunes"); st.video("https://www.youtube.com/watch?v=gLnuqh-CUNQ")

elif menu == "Lecciones A1":
    st.title("📚 Lecciones Nivel A1")
    tema = st.selectbox("Selecciona un tema:", ["Selecciona..."] + list(DATOS_TEMAS.keys()))
    
    if tema != "Selecciona...":
        d = DATOS_TEMAS[tema]
        tab1, tab2, tab3, tab4 = st.tabs(["📺 Clase", "🎧 Dictado", "📖 Cuento", "📄 Material para Imprimir"])
        
        with tab1:
            if "video" in d: st.video(d["video"])
            if "video2" in d: st.divider(); st.video(d["video2"])
        
        with tab2:
            st.subheader("🎧 Dictado Interactivo")
            frases = d.get("frases", [])
            if frases:
                if 'it' not in st.session_state: st.session_state.it = 0
                if st.session_state.it < len(frases):
                    txt = frases[st.session_state.it]
                    if st.button("🔊 Escuchar"):
                        gTTS(text=txt, lang='es').save("s.mp3")
                        st.audio("s.mp3")
                    u_in = st.text_input("Escribe lo que oyes:", key=f"in_{tema}_{st.session_state.it}")
                    if st.button("Comprobar"):
                        if u_in.lower().strip() == txt.lower().strip():
                            st.success("¡Muy bien!"); st.session_state.it += 1; st.rerun()
                else:
                    st.success("¡Terminaste!"); st.button("Reiniciar", on_click=lambda: st.session_state.update({"it":0}))
            else: st.info("Próximamente")

        with tab3:
            if "cuento" in d:
                st.video(d["cuento"])
                if "quiz_cuento" in d:
                    st.divider()
                    st.write("### ✍️ Ejercicios del Cuento")
                    # Lógica de Quiz... (Selección y Completación)
            else: st.info("Aún no hay cuento para este tema.")

        with tab4:
            st.subheader("📄 Material para Imprimir")
            st.write("""
            ¡Bienvenido a tu rincón de práctica física! En este apartado encontrarás material diseñado para 
            reforzar lo aprendido de forma manual. Imprimir y escribir a mano te ayudará a memorizar mejor 
            el vocabulario y la gramática.
            """)
            
            col_mini, col_fichas = st.columns(2)
            
            with col_mini:
                st.write("#### 📘 Minilibros")
                st.write("Un resumen compacto y visual de toda la lección, ideal para coleccionar.")
                if "pdf" in d:
                    try:
                        with open(d["pdf"], "rb") as f:
                            st.download_button(f"📥 Descargar Minilibro ({tema})", f, file_name=d["pdf"], key=f"btn_mini_{tema}")
                    except FileNotFoundError:
                        st.warning(f"Archivo '{d['pdf']}' no encontrado en GitHub.")
                else:
                    st.info("Minilibro en desarrollo.")

            with col_fichas:
                st.write("#### 📝 Fichas Descargables")
                st.write("Actividades adicionales, sopas de letras y ejercicios para practicar en casa.")
                st.info("📌 Las fichas de este tema estarán disponibles muy pronto.")

elif menu == "Contacto":
    st.title("📩 Contacto")
    st.write("pao.mzh16@gmail.com")
