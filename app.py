import streamlit as st
from gtts import gTTS
import os

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Pao- Spanish- Teacher", page_icon="🎓", layout="wide")

# --- 2. DISEÑO VISUAL (CSS) ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #e0f2fe 0%, #fdfcfb 100%); }
    section[data-testid="stSidebar"] { background-color: #ffffff !important; border-right: 3px solid #1E88E5; }
    h1 { color: #1E88E5 !important; font-weight: 800; }
    .stTabs { background-color: rgba(255, 255, 255, 0.8); padding: 25px; border-radius: 20px; box-shadow: 0 10px 15px rgba(0,0,0,0.05); }
    .stButton>button { background-color: #1E88E5; color: white; border-radius: 12px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. CONTROL DE ACCESO ---
CONTRASEÑA = "123456"
if "auth" not in st.session_state: 
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🔐 Acceso Privado - Pao- Spanish- Teacher")
    clave = st.text_input("Introduce tu clave de alumno:", type="password")
    if st.button("Ingresar a la Academia"):
        if clave == CONTRASEÑA:
            st.session_state.auth = True
            st.rerun()
        else: 
            st.error("❌ Clave incorrecta")
    st.stop()

# --- 4. BARRA LATERAL ---
with st.sidebar:
    try: 
        st.image("logo.png", width=180)
    except: 
        st.warning("⚠️ Sube 'logo.png'")
    st.title("Pao- Spanish- Teacher")
    menu = st.radio("Navegación:", ["Inicio", "Lecciones", "Mi Progreso", "Contacto"])
    if st.button("Cerrar Sesión"):
        st.session_state.auth = False
        st.rerun()

# --- 5. LÓGICA DE SECCIONES ---

if menu == "Inicio":
    st.title("¡Bienvenida a tu Academia! ✨")
    col1, col2 = st.columns([1, 2])
    with col1:
        try: 
            st.image("foto_pao.png", width=300)
        except: 
            st.info("ℹ️ Sube 'foto_pao.png'")
    with col2:
        st.subheader("Tu espacio de aprendizaje de español")
        st.markdown("""
        ### 🚀 ¿Cómo aprovechar tus clases?
        1. **Mira el video:** Comienza siempre con la video-clase.
        2. **Interactúa:** Escucha los cuentos y haz los dictados.
        3. **Practica offline:** Descarga las fichas PDF de teoría y ejercicios.
        """)
        st.info("**'El idioma es el mapa de una cultura. ¡Estoy aquí para ayudarte a recorrerlo!'**")

elif menu == "Lecciones":
    st.title("📚 Centro de Capacitación")
    nivel = st.selectbox("Primero, elige tu nivel:", ["Selecciona...", "Nivel A1 (Principiante)", "Nivel A2", "Nivel B1"])

    if nivel == "Nivel A1 (Principiante)":
        tema_a1 = st.selectbox("Elige un tema:", ["Selecciona...", "Saludos", "Números"])

        if tema_a1 == "Saludos":
            st.header("📍 Tema: Los Saludos")
            # Pestañas basadas en tu minilibro
            t_video, t_dictado, t_quiz, t_print = st.tabs(["📺 Video Clase", "🎧 Dictado", "✍️ Quiz", "📄 Materiales PDF"])

            with t_video:
                st.subheader("Video Principal de Saludos")
                url_video = "https://www.youtube.com/watch?v=dD7dw9MN4H0"
                st.video(url_video)
                st.write("Mira este video para repasar los saludos básicos y respuestas comunes.")

            with t_dictado:
                st.subheader("🎧 Desafío de Dictado")
                # Frases extraídas de tu material
                frases = ["Buenos días", "Buenas tardes", "¿Cómo estás?", "Mucho gusto", "Hasta mañana"]
                
                if 'idx' not in st.session_state: 
                    st.session_state.idx = 0
                
                if st.session_state.idx < len(frases):
                    actual = frases[st.session_state.idx]
                    st.write(f"Frase {st.session_state.idx + 1} de {len(frases)}")
                    if st.button("🔊 Escuchar"):
                        tts = gTTS(text=actual, lang='es')
                        tts.save("d.mp3")
                        st.audio("d.mp3")
                    
                    resp = st.text_input("Escribe lo que escuchas:", key=f"d_in_{st.session_state.idx}")
                    
                    if st.button("Comprobar"):
                        if resp.lower().strip() == actual.lower().strip():
                            st.success("¡Excelente!")
                            st.session_state.idx += 1
                            st.rerun()
                        else: 
                            st.error("Inténtalo de nuevo. Presta atención a los acentos.")
                else:
                    st.balloons()
                    st.success("🎊 ¡Felicidades! Has completado el dictado.")
                    if st.button("Reiniciar práctica"):
                        st.session_state.idx = 0
                        st.rerun()

            with t_quiz:
                st.subheader("Cuestionario de Repaso")
                # Pregunta basada en la página 4 de tu PDF
                preg1 = st.radio("¿Qué saludo es FORMAL (Usted)?", ["¡Hola!", "Buenos días, ¿Cómo está usted?", "¿Qué tal?"])
                if st.button("Validar Pregunta"):
                    if preg1 == "Buenos días, ¿Cómo está usted?":
                        st.snow()
                        st.success("¡Correcto! Usamos 'Usted' con jefes o desconocidos.")
                    else:
                        st.error("Esa opción es informal. ¡Vuelve a revisar la página 4 de tu guía!")

            with t_print:
                st.subheader("📄 Materiales Descargables")
                st.write("Descarga la guía teórica y la ficha de ejercicios práctica.")
                
                c1, c2 = st.columns(2)
                with c1:
                    st.info("📖 **Minilibro de Teoría**")
                    try:
                        with open("Libro_Saludos_A1.pdf", "rb") as f:
                            st.download_button("Descargar Libro", f, "Libro_Saludos_Pao.pdf")
                    except FileNotFoundError:
                        st.warning("⚠️ Sube 'Libro_Saludos_A1.pdf' a GitHub")

                with c2:
                    st.success("✍️ **Ficha de Ejercicios**")
                    try:
                        with open("Ejercicios_Saludos_A1.pdf", "rb") as f:
                            st.download_button("Descargar Ejercicios", f, "Ejercicios_Pao_Spanish.pdf")
                    except FileNotFoundError:
                        st.warning("⚠️ Sube 'Ejercicios_Saludos_A1.pdf' a GitHub")

elif menu == "Contacto":
    st.title("📩 Contacto")
    st.markdown("📧 Email: [pao.mzh16@gmail.com](mailto:pao.mzh16@gmail.com)")
    st.success("Escríbeme si tienes dudas con los materiales de A1.")
