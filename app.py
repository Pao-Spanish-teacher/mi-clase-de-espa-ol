import streamlit as st
from gtts import gTTS
import os

st.set_page_config(page_title="Dictado de Español", page_icon="🇪🇸")

# --- FRASES DEL EXAMEN ---
frases = [
    "El profesor explica la lección",
    "Mañana vamos a ir a la playa",
    "Me gusta mucho comer fruta",
    "El español es un idioma muy musical"
]

# Inicializar el estado de la sesión si no existe
if 'paso' not in st.session_state:
    st.session_state.paso = 0
if 'puntos' not in st.session_state:
    st.session_state.puntos = 0

st.title("🎧 Ejercicio de Dictado Interactivo")

# Verificar si aún hay frases
if st.session_state.paso < len(frases):
    frase_actual = frases[st.session_state.paso]
    
    st.write(f"### Frase {st.session_state.paso + 1} de {len(frases)}")
    
    # Generar y reproducir audio
    tts = gTTS(text=frase_actual, lang='es', tld='es')
    tts.save("dictado.mp3")
    st.audio("dictado.mp3")

    # Formulario para evitar que la página se refresque antes de tiempo
    with st.form(key='mi_formulario'):
        respuesta = st.text_input("Escribe lo que escuchas:")
        boton_enviar = st.form_submit_button(label='Comprobar y Continuar')

    if boton_enviar:
        # Comparar respuestas
        if respuesta.lower().strip().rstrip('.') == frase_actual.lower().strip().rstrip('.'):
            st.success("✨ ¡Excelente! Es correcto.")
            st.session_state.puntos += 1
        else:
            st.error(f"❌ Incorrecto. La frase era: '{frase_actual}'")
        
        # Avanzar al siguiente paso
        st.session_state.paso += 1
        st.button("Hacer siguiente ejercicio") # Botón simple para refrescar

else:
    # --- PANTALLA FINAL ---
    st.balloons()
    st.header("🎊 ¡Has terminado el dictado!")
    st.subheader(f"Tu nota final: {st.session_state.puntos} / {len(frases)}")
    
    if st.button("Reiniciar desde el principio"):
        st.session_state.paso = 0
        st.session_state.puntos = 0
        st.rerun()
