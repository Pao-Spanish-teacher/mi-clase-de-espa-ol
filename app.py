import streamlit as st
from gtts import gTTS
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Pao- Spanish- Teacher", page_icon="🎓", layout="wide")

# --- 2. DISEÑO VISUAL (CSS) ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #e0f2fe 0%, #fdfcfb 100%); }
    .stTabs { background-color: rgba(255, 255, 255, 0.8); padding: 25px; border-radius: 20px; box-shadow: 0 10px 15px rgba(0,0,0,0.05); }
    h1 { color: #1E88E5 !important; font-weight: 800; }
    .stVideo { border-radius: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.2); }
    .stButton>button { background-color: #1E88E5; color: white; border-radius: 12px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. CONTROL DE ACCESO ---
CONTRASEÑA = "pao_premium"
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("🔐 Acceso Privado - Pao- Spanish- Teacher")
    clave = st.text_input("Introduce tu clave de alumno:", type="password")
    if st.button("Entrar a la Academia"):
        if clave == CONTRASEÑA:
            st.session_state.auth = True
            st.rerun()
        else: st.error("Clave incorrecta")
    st.stop()

# --- 4. BARRA LATERAL ---
with st.sidebar:
    try: st.image("logo.png", width=180)
    except: st.warning("Sube 'logo.png'")
    st.title("Menú Principal")
    menu = st.radio("Ir a:", ["Inicio", "Lecciones", "Mi Progreso", "Contacto"])
    st.write("---")
    if st.button("Cerrar Sesión"):
        st.session_state.auth = False
        st.rerun()

# --- 5. SECCIONES ---

if menu == "Inicio":
    st.title("¡Hola! Bienvenida a tu espacio de aprendizaje ✨")
    col1, col2 = st.columns([1, 2])
    with col1:
        try: st.image("foto_pao.png", width=300)
        except: st.info("Sube 'foto_pao.png'")
    with col2:
        st.subheader("Contenido 100% original por Pao")
        st.write("Hoy vamos a sumergirnos en historias fascinantes para mejorar tu fluidez.")

elif menu == "Lecciones":
    st.title("📚 Videocuentos Interactivos")
    tema = st.selectbox("Elige tu cuento de hoy:", ["Cuento: El viaje de Luna"])

    if tema == "Cuento: El viaje de Luna":
        st.header("🌙 Lección: El viaje de Luna")
        tab_v, tab_e, tab_d = st.tabs(["📺 Videocuento", "✍️ Actividades", "📄 Material Descargable"])

        with tab_v:
            st.subheader("Mira y escucha el cuento")
            try: st.video("cuento_luna.mp4")
            except: st.info("🎥 Aquí irá tu video narrado: 'cuento_luna.mp4'")
            
            with st.expander("Ver guion del cuento"):
                st.write("Luna era una estrella que quería conocer la Tierra...")

        with tab_e:
            st.subheader("¿Cuánto comprendiste?")
            p1 = st.radio("¿A dónde quería viajar Luna?", ["Al sol", "A la Tierra", "A Marte"])
            if st.button("Validar"):
                if p1 == "A la Tierra": st.success("¡Perfecto!")
                else: st.error("Inténtalo de nuevo")

        with tab_d:
            st.subheader("📥 Tu material para imprimir")
            st.write("Descarga esta ficha original para practicar la escritura de lo aprendido en el cuento.")
            
            # Lógica para descargar PDF (Debes subir el PDF a GitHub)
            try:
                with open("ficha_luna.pdf", "rb") as file:
                    st.download_button(
                        label="📩 Descargar Ficha de Trabajo (PDF)",
                        data=file,
                        file_name="Ficha_Luna_PaoSpanish.pdf",
                        mime="application/pdf"
                    )
            except:
                st.info("ℹ️ Sube tu archivo 'ficha_luna.pdf' a GitHub para activar la descarga.")

elif menu == "Mi Progreso":
    st.title("🏆 Tus Logros")
    st.progress(50)
    st.write("¡Vas por la mitad del curso! Sigue así.")

elif menu == "Contacto":
    st.title("📩 Soporte")
    st.write("Email: contacto@paospanish.com")
