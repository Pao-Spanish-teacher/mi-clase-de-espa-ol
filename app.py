import streamlit as st
from gtts import gTTS
import os

# --- 1. CONFIGURACIÓN DE PÁGINA Y DISEÑO ---
st.set_page_config(page_title="Pao- Spanish- Teacher", page_icon="🎓", layout="wide")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #e0f2fe 0%, #fdfcfb 100%); }
    section[data-testid="stSidebar"] { background-color: #ffffff !important; border-right: 3px solid #1E88E5; }
    h1 { color: #1E88E5 !important; font-weight: 800; }
    .stTabs { background-color: rgba(255, 255, 255, 0.8); padding: 25px; border-radius: 20px; box-shadow: 0 10px 15px rgba(0,0,0,0.05); }
    .stButton>button { background-color: #1E88E5; color: white; border-radius: 12px; font-weight: bold; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. CONTROL DE ACCESO ---
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

# --- 3. BARRA LATERAL (LOGO Y MENÚ) ---
with st.sidebar:
    try: st.image("logo.png", width=180)
    except: st.warning("⚠️ Sube 'logo.png' a GitHub")
    st.title("Pao- Spanish- Teacher")
    st.write("---")
    menu = st.radio("Navegación:", ["Inicio", "Lecciones", "Mi Progreso", "Contacto"])
    st.write("---")
    if st.button("Cerrar Sesión"):
        st.session_state.auth = False
        st.rerun()

# --- 4. SECCIONES DEL MENÚ ---

# --- INICIO ---
if menu == "Inicio":
    st.title("¡Bienvenida a tu Academia! ✨")
    col1, col2 = st.columns([1, 2])
    with col1:
        try: st.image("foto_pao.png", width=300)
        except: st.info("ℹ️ Sube 'foto_pao.png'")
    with col2:
        st.subheader("Aprende español con material original")
        st.write("¡Hola! Soy Pao. Aquí tienes todo el material exclusivo para tus clases.")

# --- LECCIONES (TODO INTEGRADO AQUÍ) ---
elif menu == "Lecciones":
    st.title("📚 Centro de Aprendizaje")
    
    # Selector de tipos de lección
    tipo_leccion = st.selectbox("¿Qué quieres practicar hoy?", 
                                ["Tema 1: Saludos (Gramática y Dictado)", 
                                 "Tema 2: El viaje de Luna (Cuento Narrado)"])
    st.write("---")

    # OPCIÓN 1: GRAMÁTICA Y DICTADO
    if tipo_leccion == "Tema 1: Saludos (Gramática y Dictado)":
        st.header("📍 Saludos y Presentaciones")
        t1, t2, t3 = st.tabs(["📺 Video Clase", "🎧 Dictado", "✍️ Quiz"])
        
        with t1:
            try: st.video("tema1_video.mp4")
            except: st.info("🎥 Sube 'tema1_video.mp4'")
        
        with t2:
            st.subheader("Práctica de Escucha")
            frase = "Mucho gusto, soy Pao"
            if st.button("Reproducir Dictado"):
                tts = gTTS(text=frase, lang='es')
                tts.save("audio.mp3")
                st.audio("audio.mp3")
            resp = st.text_input("¿Qué escuchaste?")
            if st.button("Comprobar"):
                if resp.lower().strip() == frase.lower().strip(): st.success("¡Perfecto!")
                else: st.error(f"Era: {frase}")
        
        with t3:
            q = st.radio("¿Cómo se dice 'Good morning'?", ["Hola", "Buenos días", "Adiós"])
            if st.button("Validar Respuesta"):
                if q == "Buenos días": st.success("✅ ¡Correcto!")
                else: st.error("❌ Intenta de nuevo")

    # OPCIÓN 2: CUENTOS
    elif tipo_leccion == "Tema 2: El viaje de Luna (Cuento Narrado)":
        st.header("📖 Videocuento: El viaje de Luna")
        c1, c2, c3 = st.tabs(["📺 Ver Cuento", "✍️ Comprensión", "📄 Ficha PDF"])
        
        with c1:
            try: st.video("cuento_luna.mp4")
            except: st.info("🎥 Sube 'cuento_luna.mp4'")
            with st.expander("Leer el texto del cuento"):
                st.write("Había una vez una estrella llamada Luna...")

        with c2:
            p1 = st.radio("¿Quién es la protagonista?", ["Una estrella", "Un gato", "Una niña"])
            if st.button("Corregir Actividad"):
                if p1 == "Una estrella": st.success("🌟 ¡Muy bien!")
                else: st.error("Vuelve a ver el video.")

        with c3:
            st.subheader("Material para imprimir")
            try:
                with open("ficha_luna.pdf", "rb") as f:
                    st.download_button("📩 Descargar Ficha (PDF)", f, "Ficha_Luna.pdf")
            except: st.warning("ℹ️ Sube 'ficha_luna.pdf' para activar la descarga.")

# --- PROGRESO ---
elif menu == "Mi Progreso":
    st.title("🏆 Tu Progreso")
    st.write("Sigue aprendiendo para completar tu barra de logros.")
    st.progress(40)

# --- CONTACTO ---
elif menu == "Contacto":
    st.title("📩 Contacto")
    st.write("Dudas: contacto@paospanish.com")
