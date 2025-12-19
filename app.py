import streamlit as st
from gtts import gTTS
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
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
CONTRASEÑA = "pao_premium"
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("🔐 Acceso Privado - Pao- Spanish- Teacher")
    clave = st.text_input("Introduce tu clave de alumno:", type="password")
    if st.button("Ingresar a la Academia"):
        if clave == CONTRASEÑA:
            st.session_state.auth = True
            st.rerun()
        else: st.error("❌ Clave incorrecta")
    st.stop()

# --- 4. BARRA LATERAL ---
with st.sidebar:
    try: st.image("logo.png", width=180)
    except: st.warning("⚠️ Sube 'logo.png'")
    st.title("Pao- Spanish- Teacher")
    st.write("---")
    menu = st.radio("Navegación:", ["Inicio", "Lecciones", "Mi Progreso", "Contacto"])
    if st.button("Cerrar Sesión"):
        st.session_state.auth = False
        st.rerun()

# --- 5. LÓGICA DE SECCIONES ---

if menu == "Inicio":
    st.title("¡Bienvenida a tu Academia! ✨")
    col1, col2 = st.columns([1, 2])
    with col1:
        try: st.image("foto_pao.png", width=300)
        except: st.info("ℹ️ Sube 'foto_pao.png'")
    with col2:
        st.subheader("Tu espacio de aprendizaje de español")
        st.write("Selecciona 'Lecciones' en el menú para comenzar con los temas del curso.")

elif menu == "Lecciones":
    st.title("📚 Temas del Curso")
    # LISTA DE TEMAS PRINCIPALES
    tema_seleccionado = st.selectbox(
        "¿Qué tema quieres estudiar hoy?", 
        ["Selecciona un tema...", "Saludos", "Números", "Alfabeto"]
    )

    st.write("---")

    # --- DESARROLLO DEL TEMA: SALUDOS ---
    if tema_seleccionado == "Saludos":
        st.header("📍 Tema: Los Saludos")
        
        # Aquí creamos todas las herramientas en pestañas para este tema
        t_video, t_dictado, t_cuento, t_nombres, t_quiz, t_print = st.tabs([
            "📺 Video Clase", 
            "🎧 Dictado", 
            "📖 El Cuento", 
            "🖼️ Vocabulario (Nombres)", 
            "✍️ Selección Simple", 
            "📄 Para Imprimir"
        ])

        with t_video:
            st.subheader("Video Principal de Saludos")
            try: st.video("saludos_clase.mp4")
            except: st.info("🎥 Sube 'saludos_clase.mp4' a GitHub")

        with t_dictado:
            st.subheader("Práctica de Escucha (Dictado)")
            frase_saludo = "Hola, ¿cómo estás?"
            if st.button("🔊 Escuchar Dictado"):
                tts = gTTS(text=frase_saludo, lang='es')
                tts.save("dictado_saludos.mp3")
                st.audio("dictado_saludos.mp3")
            resp_dictado = st.text_input("Escribe lo que escuchas:", key="d_saludos")
            if st.button("Comprobar Dictado"):
                if resp_dictado.lower().strip() == frase_saludo.lower().strip(): st.success("¡Excelente!")
                else: st.error(f"La frase era: {frase_saludo}")

        with t_cuento:
            st.subheader("Videocuento Narrado")
            try: st.video("cuento_saludos.mp4")
            except: st.info("🎥 Sube 'cuento_saludos.mp4'")
            with st.expander("Leer texto del cuento"):
                st.write("Había una vez una niña llamada Ana que saludaba a todos...")

        with t_nombres:
            st.subheader("¿Cómo se llama?")
            st.write("Escribe el nombre correcto para cada imagen:")
            col_img1, col_img2 = st.columns(2)
            with col_img1:
                try: st.image("img_saludo1.png", width=200)
                except: st.info("Sube 'img_saludo1.png'")
                nombre1 = st.text_input("Nombre de la acción 1:", key="n1")
            with col_img2:
                try: st.image("img_saludo2.png", width=200)
                except: st.info("Sube 'img_saludo2.png'")
                nombre2 = st.text_input("Nombre de la acción 2:", key="n2")

        with t_quiz:
            st.subheader("Selección Simple")
            opcion = st.radio("¿Cuál es un saludo de mañana?", ["Buenas noches", "Buenos días", "Hola"], key="q_saludos")
            if st.button("Validar Respuesta"):
                if opcion == "Buenos días": st.success("✅ ¡Correcto!")
                else: st.error("❌ Intenta otra vez")

        with t_print:
            st.subheader("Material Descargable")
            st.write("Descarga la ficha de actividades para practicar en papel.")
            try:
                with open("ficha_saludos.pdf", "rb") as f:
                    st.download_button("📩 Descargar Ficha (PDF)", f, "Ficha_Saludos_Pao.pdf")
            except: st.warning("ℹ️ Sube 'ficha_saludos.pdf' para activar la descarga.")

    # --- ESPACIO PARA OTROS TEMAS ---
    elif tema_seleccionado == "Números":
        st.header("📍 Tema: Los Números")
        st.info("Contenido en construcción... pronto verás los videos y ejercicios aquí.")

    elif tema_seleccionado == "Alfabeto":
        st.header("📍 Tema: El Alfabeto")
        st.info("Contenido en construcción...")

elif menu == "Mi Progreso":
    st.title("🏆 Mi Progreso")
    st.progress(20)

elif menu == "Contacto":
    st.title("📩 Contacto")
    st.write("Email: contacto@paospanish.com")
