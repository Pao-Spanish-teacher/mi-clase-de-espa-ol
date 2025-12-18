import streamlit as st
from gtts import gTTS
import os

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Mi Clase de Español", page_icon="🎓")

st.title("🎧 Ejercicio de Dictado")
st.write("Escucha el audio y escribe la frase correctamente. ¡Cuidado con la ortografía!")

# --- BASE DE DATOS DE FRASES ---
# Puedes añadir o cambiar estas frases cuando quieras
frases = [
    "El profesor explica la lección",
    "Mañana vamos a ir a la playa",
    "Me gusta mucho comer fruta",
    "El español es un idioma muy musical"
]

# Usamos el "session_state" para que la página no se reinicie al azar
if 'indice' not in st.session_state:
    st.session_state.indice = 0
if 'puntos' not in st.session_state:
    st.session_state.puntos = 0

# --- LÓGICA DEL EJERCICIO ---
if st.session_state.indice < len(frases):
    frase_actual = frases[st.session_state.indice]
    
    # 1. Generar el audio
    tts = gTTS(text=frase_actual, lang='es', tld='es')
    tts.save("dictado.mp3")
    
    # 2. Mostrar el reproductor de audio
    st.audio("dictado.mp3")
    
    # 3. Entrada de texto del alumno
    respuesta = st.text_input("Escribe lo que escuchaste:", key=f"input_{st.session_state.indice}")
    
    if st.button("Comprobar"):
        # Limpieza básica de la respuesta
        if respuesta.lower().strip().rstrip('.') == frase_actual.lower().strip().rstrip('.'):
            st.success("✨ ¡Excelente! Lo has logrado.")
            st.session_state.puntos += 1
        else:
            st.error(f"❌ Casi... La frase correcta era: '{frase_actual}'")
        
        # Botón para pasar a la siguiente
        if st.button("Siguiente frase ➡️"):
            st.session_state.indice += 1
            st.rerun()

else:
    # --- RESULTADOS FINALES ---
    st.balloons()
    st.header("¡Examen terminado! 🎉")
    st.subheader(f"Tu puntuación: {st.session_state.puntos} de {len(frases)}")
    
    if st.button("Reiniciar ejercicio"):
        st.session_state.indice = 0
        st.session_state.puntos = 0
        st.rerun()
