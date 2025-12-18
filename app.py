import streamlit as st
from gtts import gTTS

# --- CONFIGURACIÓN DE MARCA ---
st.set_page_config(page_title="Pao- Spanish- Teacher", page_icon="🎓", layout="wide")

# --- CONTROL DE ACCESO ---
PASSWORD_ACADEMIA = "pao_premium" # Cambia esto por tu clave deseada

if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.title("🔐 Acceso Exclusivo - Pao- Spanish- Teacher")
    clave = st.text_input("Introduce tu código de alumno:", type="password")
    if st.button("Ingresar a la Academia"):
        if clave == PASSWORD_ACADEMIA:
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("Código incorrecto. Por favor, verifica con tu profesora.")
    st.stop()

# --- INTERFAZ DE LA ACADEMIA (POST-LOGIN) ---
with st.sidebar:
    st.title("🎓 Pao- Spanish- Teacher")
    st.write("---")
    menu = st.radio("Navegación:", ["Inicio", "Lecciones por Temas", "Contacto"])
    if st.button("Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()

# --- SECCIÓN INICIO ---
if menu == "Inicio":
    st.title("¡Bienvenido/a a tu curso de Español! ✨")
    st.subheader("Contenido 100% original diseñado para tu aprendizaje.")
    st.write("En la sección de **Lecciones** encontrarás tus paquetes de estudio que incluyen video-clase y ejercicios prácticos.")
    # st.image("tu_logo_o_foto.png") # Si tienes un logo, súbelo a GitHub y descomenta esto

# --- SECCIÓN LECCIONES (ESTRUCTURA POR PAQUETES) ---
elif menu == "Lecciones por Temas":
    st.title("📚 Tus Lecciones")
    
    tema_seleccionado = st.selectbox(
        "¿Qué quieres estudiar hoy?",
        ["Tema 1: Saludos y Presentaciones", 
         "Tema 2: La Rutina Diaria", 
         "Tema 3: Vocabulario de Viajes"]
    )

    st.write("---")

    # --- LÓGICA DE PAQUETES ---
    if tema_seleccionado == "Tema 1: Saludos y Presentaciones":
        st.header(f"📍 {tema_seleccionado}")
        
        # Usamos pestañas para organizar el "paquete"
        tab_video, tab_dictado, tab_imagenes, tab_quiz = st.tabs([
            "📺 Video-Clase", 
            "🎧 Dictado", 
            "🖼️ Vocabulario Visual", 
            "✍️ Test Rápido"
        ])

        with tab_video:
            st.subheader("Mira la explicación de hoy")
            # st.video("video_tema1.mp4") # Sube tu video a GitHub con este nombre
            st.info("Aquí aparecerá tu video original: 'video_tema1.mp4'")

        with tab_dictado:
            st.subheader("Práctica de oído")
            # Aquí insertaríamos la lógica de gTTS que ya probamos
            st.write("Escucha el audio y transcribe la frase.")

        with tab_imagenes:
            st.subheader("Identifica la imagen original")
            # st.image("imagen_tema1.png", width=400) # Sube tu imagen original
            st.info("Aquí aparecerá tu ilustración original: 'imagen_tema1.png'")

        with tab_quiz:
            st.subheader("Comprueba lo aprendido")
            pregunta = st.radio("¿Cómo se dice 'Nice to meet you'?", ["Hola", "Encantado", "Adiós"])
            if st.button("Enviar respuesta"):
                if pregunta == "Encantado": st.success("¡Correcto!")
                else: st.error("Inténtalo de nuevo.")

# --- SECCIÓN CONTACTO ---
elif menu == "Contacto":
    st.title("📩 Soporte y Dudas")
    st.write("Si tienes problemas con el acceso o alguna duda sobre las lecciones, escríbeme.")
    st.write("Email: contacto@paospanish.com") # Ejemplo
