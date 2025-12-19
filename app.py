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
        st.markdown("""
        ### 🚀 ¿Cómo aprovechar tus clases?
        1. **Mira el video:** Comienza siempre con la video-clase.
        2. **Interactúa:** Escucha los cuentos y haz los dictados.
        3. **Practica offline:** Descarga las fichas PDF.
        """)
        st.info("**'El idioma es el mapa de una cultura. ¡Estoy aquí para ayudarte a recorrerlo!'**")

elif menu == "Lecciones":
    st.title("📚 Centro de Capacitación")
    nivel = st.selectbox("Primero, elige tu nivel:", ["Selecciona...", "Nivel A1 (Principiante)", "Nivel A2", "Nivel B1"])

    if nivel == "Nivel A1 (Principiante)":
        tema_a1 = st.selectbox("Elige un tema:", ["Selecciona...", "Saludos", "Números"])

        if tema_a1 == "Saludos":
            st.header("📍 Tema: Los Saludos")
            t_video, t_dictado, t_cuento, t_quiz, t_print = st.tabs(["📺 Video", "🎧 Dictado", "📖 Cuento", "✍️ Quiz", "📄 PDF"])

            with t_video:
                try: st.video("saludos_clase.mp4")
                except: st.info("🎥 Sube 'saludos_clase.mp4'")

            with t_dictado:
                st.subheader("🎧 Desafío de 5 Frases")
                frases = ["Hola, ¿cómo estás?", "Buenos días", "Mucho gusto", "¿Cómo te llamas?", "Hasta mañana"]
                if 'idx' not in st.session_state: st.session_state.idx = 0
                
                if st.session_state.idx < len(frases):
                    actual = frases[st.session_state.idx]
                    st.write(f"Frase {st.session_state.idx + 1} de 5")
                    if st.button("🔊 Escuchar"):
                        gTTS(text=actual, lang='es').save("d.mp3")
                        st.audio("d.mp3")
                    resp = st.text_input("Escribe:", key=f"d{st.session_state.idx}")
                    if st.button("Comprobar"):
                        if resp.lower().strip() == actual.lower().strip():
                            st.success("¡Bien!")
                            st.session_state.idx += 1
                            st.rerun()
                        else: st.error("Intenta de nuevo")
                else:
                    st.balloons()
                    st.success("¡Completado!")
                    if st.button("Reiniciar"): st.session_state.idx = 0; st.rerun()

            with t_cuento:
                try: st.video("cuento_saludos.mp4")
                except: st.info("🎥 Sube 'cuento_saludos.mp4'")

            with t_quiz:
                q = st.radio("Saludo de mañana:", ["Noches", "Días", "Hola"])
                if st.button("Validar"):
                    if q == "Días": st.snow(); st.success("¡Correcto!")

            with t_print:
                try:
                    with open("ficha_saludos.pdf", "rb") as f:
                        st.download_button("📩 Descargar PDF", f, "Ficha.pdf")
                except: st.warning("Sube 'ficha_saludos.pdf'")

elif menu == "Contacto":
    st.title("📩 Contacto")
    st.markdown("📧 Email: [pao.mzh16@gmail.com](mailto:pao.mzh16@gmail.com)")
    st.success("Responderé a tus dudas lo antes posible.")
