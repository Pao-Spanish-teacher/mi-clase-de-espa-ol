import streamlit as st
from gtts import gTTS
import os

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Mi Aula de Español", page_icon="🎓")

# --- MENÚ LATERAL ---
with st.sidebar:
    st.title("📖 Actividades")
    opcion = st.radio("Elige una lección:", ["Inicio", "Dictado de Voz", "Adivina la Imagen"])
    st.markdown("---")
    st.info("💡 Consejo: Revisa bien los acentos antes de enviar.")

# --- INICIALIZACIÓN DE VARIABLES ---
if 'paso_dictado' not in st.session_state: st.session_state.paso_dictado = 0
if 'paso_imagen' not in st.session_state: st.session_state.paso_imagen = 0

# --- SECCIÓN: INICIO ---
if opcion == "Inicio":
    st.title("¡Bienvenidos a nuestra clase interactiva! 🇪🇸")
    st.write("Selecciona una actividad en el menú lateral para practicar tu español.")
    st.image("https://images.unsplash.com/photo-1543783232-af9942f4a472?w=800")

# --- SECCIÓN: DICTADO (5 FRASES) ---
elif opcion == "Dictado de Voz":
    st.title("🎧 Dictado Auditivo")
    frases = [
        "El profesor explica la lección", 
        "Mañana vamos a ir a la playa", 
        "Me gusta mucho comer fruta", 
        "El español es un idioma muy musical",
        "Hoy es un día excelente para aprender"
    ]
    
    if st.session_state.paso_dictado < len(frases):
        frase = frases[st.session_state.paso_dictado]
        st.write(f"**Frase {st.session_state.paso_dictado + 1} de {len(frases)}**")
        
        tts = gTTS(text=frase, lang='es', tld='es')
        tts.save("dictado.mp3")
        st.audio("dictado.mp3")
        
        with st.form(key='form_dictado'):
            resp = st.text_input("¿Qué escuchaste?")
            enviar = st.form_submit_button("Comprobar")
            
        if enviar:
            if resp.lower().strip().rstrip('.') == frase.lower().strip().rstrip('.'):
                st.success("✨ ¡Perfecto!")
            else:
                st.error(f"❌ Casi... La frase era: '{frase}'")
            st.session_state.paso_dictado += 1
            st.button("Siguiente Ejercicio ➡️")
    else:
        st.success("🏆 ¡Has terminado todos los dictados!")
        if st.button("Reiniciar Dictados"): st.session_state.paso_dictado = 0

# --- SECCIÓN: IMÁGENES (5 IMÁGENES) ---
elif opcion == "Adivina la Imagen":
    st.title("🖼️ Vocabulario Visual")
    fotos = [
        {"url": "https://images.unsplash.com/photo-1557800636-894a64c1696f?w=400", "res": "naranja"},
        {"url": "https://images.unsplash.com/photo-1559181567-c3190ca9959b?w=400", "res": "cereza"},
        {"url": "https://images.unsplash.com/photo-1523348837708-15d4a09cfac2?w=400", "res": "lechuga"},
        {"url": "https://images.unsplash.com/photo-1528825871115-3581a5387919?w=400", "res": "plátano"},
        {"url": "https://images.unsplash.com/photo-1585059895316-2e8b2cc1638a?w=400", "res": "guitarra"}
    ]
    
    if st.session_state.paso_imagen < len(fotos):
        actual = fotos[st.session_state.paso_imagen]
        st.write(f"**Imagen {st.session_state.paso_imagen + 1} de {len(fotos)}**")
        st.image(actual["url"], width=300)
        
        with st.form(key='form_img'):
            resp_img = st.text_input("¿Cómo se llama esto?").lower().strip()
            enviar_img = st.form_submit_button("Verificar")
            
        if enviar_img:
            if resp_img == actual["res"]:
                st.success(f"✅ ¡Sí! Es una {actual['res']}")
            else:
                st.error(f"❌ No, la respuesta correcta es: {actual['res']}")
            st.session_state.paso_imagen += 1
            st.button("Ver siguiente imagen ➡️")
    else:
        st.balloons()
        st.success("🏁 ¡Reto visual terminado!")
        if st.button("Reiniciar Imágenes"): st.session_state.paso_imagen = 0
