import streamlit as st
import os

# --- 1. CONFIGURACIÓN DE SEGURIDAD ---
# Define aquí la contraseña para tus alumnos
CONTRASEÑA_CORRECTA = "espanol2024" 

def verificar_contraseña():
    """Devuelve True si la contraseña es correcta."""
    if "autenticado" not in st.session_state:
        st.session_state.autenticado = False

    if not st.session_state.autenticado:
        st.title("🔐 Acceso a Contenido Exclusivo")
        st.write("Bienvenido a mi academia de español. Por favor, introduce tu clave de acceso.")
        
        clave = st.text_input("Contraseña:", type="password")
        if st.button("Entrar"):
            if clave == CONTRASEÑA_CORRECTA:
                st.session_state.autenticado = True
                st.rerun()
            else:
                st.error("❌ Contraseña incorrecta. Contacta con tu profesora.")
        return False
    return True

# --- 2. INTERFAZ PRINCIPAL (Solo se ve si está autenticado) ---
if verificar_contraseña():
    
    # Botón para salir en el menú lateral
    with st.sidebar:
        st.title("🎓 Mi Academia")
        if st.button("Cerrar Sesión"):
            st.session_state.autenticado = False
            st.rerun()
        
        st.markdown("---")
        opcion = st.radio("Ir a:", ["Bienvenida", "Video-Lección", "Práctica Visual"])

    # --- SECCIÓN BIENVENIDA ---
    if opcion == "Bienvenida":
        st.title("¡Hola de nuevo! ✨")
        st.write("Este es tu espacio de aprendizaje con material 100% original.")
        # Aquí puedes poner una imagen tuya de bienvenida
        # st.image("bienvenida.png") 

    # --- SECCIÓN VIDEO ---
    elif opcion == "Video-Lección":
        st.header("🎥 Clase del día")
        st.write("Mira este video que he preparado exclusivamente para ti:")
        
        # Cambia "mi_video.mp4" por el nombre real de tu archivo en GitHub
        try:
            st.video("mi_video.mp4") 
        except:
            st.info("Aquí aparecerá tu video cuando lo subas a GitHub con el nombre 'mi_video.mp4'")

    # --- SECCIÓN IMÁGENES ---
    elif opcion == "Práctica Visual":
        st.header("🖼️ Ejercicios con Imágenes Originales")
        
        # Ejemplo de ejercicio con una de tus imágenes
        try:
            st.image("ejercicio1.png", width=400)
            with st.form("quiz"):
                rta = st.text_input("¿Qué representa esta imagen?")
                if st.form_submit_button("Verificar"):
                    st.success("¡Excelente!")
        except:
            st.warning("Sube tu archivo 'ejercicio1.png' a GitHub para verlo aquí.")
