import streamlit as st
from gtts import gTTS
import os

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Mi Aula de Español", page_icon="🎓", layout="centered")

# --- MENÚ LATERAL ---
with st.sidebar:
    st.title("📖 Actividades")
    opcion = st.radio("Elige una lección:", ["Inicio", "Dictado de Voz", "Adivina la Imagen"])
    st.markdown("---")
    st.write("Profesora: Español")

# --- INICIALIZACIÓN DE VARIABLES (SESSION STATE) ---
if 'paso_dictado' not in st.session_state: st.session_state.paso_dictado = 0
if 'paso_imagen' not in st.session_state: st.session_state.paso_imagen = 0

# --- SECCIÓN: INICIO ---
if opcion == "Inicio":
    st.title("¡Bienvenidos a nuestra clase interactiva! 🇪🇸")
    st.write("Selecciona una de las actividades en el menú de la izquierda para comenzar a practicar.")
    st.image("https://images.unsplash.com/photo-1543783232-af9942f4a472?w=800", caption="Aprender español es divertido")

# --- SECCIÓN: DICTADO ---
elif opcion == "Dictado de Voz":
    st.title("🎧 Dictado Auditivo")
    frases = ["El profesor explica la lección", "Me gusta mucho comer fruta"]
    
    if st.session_state.paso_dictado < len(frases):
        frase = frases[st.session_state.paso_dictado]
        tts = gTTS(text=frase, lang='es')
        tts.save("dictado.mp3")
        st.audio("dictado.mp3")
        
        with st.form(key='form_dictado'):
            resp = st.text_input("¿Qué escuchaste?")
            if st.form_submit_button("Comprobar"):
                if resp.lower().strip().rstrip('.') == frase.lower().strip().rstrip('.'):
                    st.success("¡Perfecto!")
                else:
                    st.error(f"Era: {frase}")
                st.session_state.paso_dictado += 1
                st.button("Siguiente")
    else:
        st.success("¡Has terminado el dictado!")
        if st.button("Reiniciar Dictado"): st.session_state.paso_dictado = 0

# --- SECCIÓN: IMÁGENES ---
elif opcion == "Adivina la Imagen":
    st.title("🖼️ Vocabulario Visual")
    fotos = [
        {"url": "https://images.unsplash.com/photo-1557800636-894a64c1696f?w=400", "res": "naranja"},
        {"url": "https://images.unsplash.com/photo-1559181567-c3190ca9959b?w=400", "res": "cereza"}
    ]
    
    if st.session_state.paso_imagen < len(fotos):
        actual = fotos[st.session_state.paso_imagen]
        st.image(actual["url"], width=300)
        
        with st.form(key='form_img'):
            resp_img = st.text_input("¿Qué es esto?").lower().strip()
            if st.form_submit_button("Verificar"):
                if resp_img == actual["res"]:
                    st.success(f"¡Sí! Es una {actual['res']}")
                else:
                    st.error(f"No, es una {actual['res']}")
                st.session_state.paso_imagen += 1
                st.button("Siguiente")
    else:
        st.success("¡Reto visual terminado!")
        if st.button("Reiniciar Imágenes"): st.session_state.paso_imagen = 0
