import streamlit as st
from gtts import gTTS
import os

# --- 1. CONFIGURACIÓN DE PÁGINA Y MARCA ---
st.set_page_config(page_title="Pao- Spanish- Teacher", page_icon="🎓", layout="wide")

# --- 2. DISEÑO VISUAL PERSONALIZADO (CSS) ---
st.markdown("""
    <style>
    /* Fondo con degradado moderno */
    .stApp {
        background: linear-gradient(135deg, #e0f2fe 0%, #fdfcfb 100%);
    }

    /* Estilo de la barra lateral */
    section[data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 3px solid #1E88E5;
    }

    /* Títulos profesionales */
    h1 {
        color: #1E88E5 !important;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 800;
    }

    /* Botones vibrantes */
    .stButton>button {
        background-color: #1E88E5;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 0.6rem 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        font-weight: bold;
    }
    
    .stButton>button:hover {
        background-color: #1565C0;
        transform: translateY(-2px);
    }

    /* Estilo de las tarjetas de contenido (Tabs) */
    .stTabs {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 15px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. CONTROL DE ACCESO ---
CONTRASEÑA_ACADEMIA = "pao_premium" 

if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.title("🔐 Acceso Privado")
    st.subheader("Bienvenido a Pao- Spanish- Teacher")
    st.write("Introduce tu clave de alumno para acceder al material exclusivo.")
    
    col_login, _ = st.columns([1, 1])
    with col_login:
        clave = st.text_input("Contraseña:", type="password")
        if st.button("Ingresar a la Academia"):
            if clave == CONTRASEÑA_ACADEMIA:
                st.session_state.autenticado = True
                st.rerun()
            else:
                st.error("❌ Código incorrecto.")
    st.stop()

# --- 4. BARRA LATERAL (LOGO Y MENÚ) ---
with st.sidebar:
    try:
        st.image("logo.png", width=200)
    except:
        st.warning("⚠️ Sube 'logo.png' a GitHub")
    
    st.title("Pao- Spanish- Teacher")
    st.write("---")
    menu = st.radio("Navegación:", ["Inicio", "Lecciones", "Mi Progreso", "Contacto"])
    st.write("---")
    if st.button("Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()

# --- 5. LÓGICA DE LAS SECCIONES ---

if menu == "Inicio":
    st.title("¡Hola! 👋 Bienvenido a tu clase personalizada")
    col_foto, col_texto = st.columns([1, 2])
    
    with col_foto:
        try:
            st.image("foto_pao.png", width=350, caption="Tu profesora: Pao")
        except:
            st.info("ℹ️ Sube tu foto como 'foto_pao.png'")
            
    with col_texto:
        st.subheader("Contenido 100% original diseñado para ti.")
        st.write("""
        En esta plataforma premium, aprenderás español de forma práctica y visual. 
        Cada lección ha sido creada para que avances a tu propio ritmo con materiales que no encontrarás en ningún otro lugar.
        
        **Instrucciones:**
        1. Ve a la pestaña **Lecciones**.
        2. Selecciona un tema.
        3. Mira el video y completa las actividades para ganar tus puntos.
        """)

elif menu == "Lecciones":
    st.title("📚 Paquetes de Estudio")
    
    tema = st.selectbox(
        "Elige el tema que quieres practicar hoy:",
        ["Tema 1: Saludos y Presentaciones", 
         "Tema 2: La Rutina Diaria", 
         "Tema 3: En el Restaurante"]
    )

    st.write("---")

    if tema == "Tema 1: Saludos y Presentaciones":
        st.header(f"📍 {tema}")
        
        tab_vid, tab_dic, tab_img, tab_test = st.tabs([
            "📺 Video-Clase", "🎧 Dictado", "🖼️ Vocabulario", "✍️ Examen"
        ])

        with tab_vid:
            st.subheader("Video-Lección Original")
            try:
                st.video("tema1_video.mp4")
            except:
                st.info("🎥 Sube tu video a GitHub con el nombre: 'tema1_video.mp4'")

        with tab_dic:
            st.subheader("Práctica de Dictado")
            frase_oculta = "Mucho gusto, soy Pao"
            if st.button("Reproducir Audio"):
                tts = gTTS(text=frase_oculta, lang='es')
                tts.save("audio_t1.mp3")
                st.audio("audio_t1.mp3")
            
            resp = st.text_input("Escribe lo que escuchaste:", key="input_t1")
            if st.button("Validar Dictado"):
                if resp.lower().strip() == frase_oculta.lower().strip():
                    st.success("✨ ¡Perfecto!")
                else:
                    st.error(f"❌ La respuesta era: {frase_oculta}")

        with tab_img:
            st.subheader("¿Qué ves en mi ilustración?")
            try:
                st.image("tema1_foto.png", width=450)
                nom_img = st.text_input("Nombre del objeto:", key="img_t1").lower().strip()
                if st.button("Verificar Imagen"):
                    if nom_img == "hola": 
                        st.success("✅ ¡Correcto!")
                    else:
                        st.error("❌ Intenta de nuevo")
            except:
                st.info("🖼️ Sube tu imagen original: 'tema1_foto.png'")

        with tab_test:
            st.subheader("Test Rápido de Comprensión")
            q = st.radio("¿Cuál es un saludo formal?", ["¡Qué onda!", "Buenos días", "Chao"])
            if st.button("Corregir Test"):
                if q == "Buenos días": st.success("🌟 ¡Respuesta correcta!")
                else: st.error("Esa opción no es correcta.")

elif menu == "Mi Progreso":
    st.title("🏆 Tu Camino al Éxito")
    st.write("Aquí verás cuánto has avanzado en el curso.")
    st.progress(33)

elif menu == "Contacto":
    st.title("📩 ¿Dudas o Soporte?")
    st.write("Si necesitas ayuda con tu cuenta o las lecciones, escríbeme:")
    st.info("Email: contacto@paospanish.com")
