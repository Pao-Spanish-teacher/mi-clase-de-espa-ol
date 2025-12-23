import streamlit as st
from gtts import gTTS
import os

# --- 1. CONFIGURACIÓN Y DATOS ---
st.set_page_config(page_title="Pao- Spanish- Teacher", page_icon="🎓", layout="wide")

# Diccionario Maestro con todos los temas de A1
DATOS_TEMAS = {
    "1. Saludos y Despedidas": {"video": "https://www.youtube.com/watch?v=dD7dw9MN4H0", "pdf": "minilibro Saludos.pdf", "frases": ["Buenos días", "Mucho gusto", "Hasta luego"]},
    "2. Los Números (0-100)": {"video": "URL_YOUTUBE", "pdf": "Minilibros Los números en español (0-100).pdf", "frases": ["Cincuenta", "Ochenta y dos", "Cien"]},
    "3. Los Colores": {"video": "URL_YOUTUBE", "pdf": "Minilibro Los colores en español.pdf", "frases": ["Azul", "Rojo", "Amarillo"]},
    "4. Días, Meses y Estaciones": {"video": "URL_YOUTUBE", "pdf": "Minilibro Los días, los meses y las estaciones.pdf", "frases": ["Lunes", "Octubre", "Primavera"]},
    "5. La Hora": {"video": "URL_YOUTUBE", "pdf": "Minilibro La Hora en Español.pdf", "frases": ["Son las tres", "Es la una", "En punto"]},
    "6. La Familia": {"video": "URL_YOUTUBE", "pdf": "minilibro La familia en español.pdf", "frases": ["Mi madre", "Mi hermano", "Mi abuela"]},
    "7. Las Profesiones": {"video": "URL_YOUTUBE", "pdf": "Minilibro Las profesiones en español.pdf", "frases": ["Médico", "Profesor", "Abogado"]},
    "8. Profesiones Técnicas": {"video": "URL_YOUTUBE", "pdf": "Minilibro Las profesiones técnicas en español.pdf", "frases": ["Ingeniero", "Técnico", "Mecánico"]},
    "9. Nacionalidad y Países": {"video": "URL_YOUTUBE", "pdf": "Minilibros Los países y nacionalidades en español.pdf", "frases": ["España", "Soy mexicano", "Francia"]},
    "10. Partes del Cuerpo": {"video": "URL_YOUTUBE", "pdf": "Minilibro Las partes del cuerpo en español.pdf", "frases": ["La cabeza", "El brazo", "La pierna"]},
    "11. La Ropa y Vestimenta": {"video": "URL_YOUTUBE", "pdf": "Minilibro La ropa y la vestimenta en español.pdf", "frases": ["La camisa", "Los pantalones", "Zapatos"]},
    "12. Comida y Bebidas": {"video": "URL_YOUTUBE", "pdf": "Minilibro Comidas y Bebidas en Español..pdf", "frases": ["Manzana", "Café", "Agua"]},
    "13. La Casa": {"video": "URL_YOUTUBE", "pdf": "Minilibro La casa y sus partes en español.pdf", "frases": ["La cocina", "El baño", "Sala"]},
    "14. Objetos Cotidianos": {"video": "URL_YOUTUBE", "pdf": "Minilibros Los objetos cotidianos en español.pdf", "frases": ["La llave", "El libro", "Mesa"]},
    "15. Medios de Transporte": {"video": "URL_YOUTUBE", "pdf": "Minilibros Los medios de transporte en español.pdf", "frases": ["El coche", "Avión", "Bicicleta"]},
    "16. Los Lugares": {"video": "URL_YOUTUBE", "pdf": "Minilibro Los lugares en español.pdf", "frases": ["El parque", "La escuela", "Cine"]},
    "17. Animales Domésticos": {"video": "URL_YOUTUBE", "pdf": "Minilibro Los animales domésticos en español.pdf", "frases": ["El perro", "El gato", "Pájaro"]},
    "18. Animales Salvajes": {"video": "URL_YOUTUBE", "pdf": "Minilibro Los animales salvajes en español.pdf", "frases": ["El león", "Elefante", "Tigre"]}
}

# --- 2. CONTROL DE ACCESO ---
CONTRASEÑA = "pao_premium"
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("🔐 Academia Pao- Spanish- Teacher")
    clave = st.text_input("Clave de alumno:", type="password")
    if st.button("Ingresar"):
        if clave == CONTRASEÑA:
            st.session_state.auth = True
            st.rerun()
        else: st.error("Clave incorrecta")
    st.stop()

# --- 3. BARRA LATERAL ---
with st.sidebar:
    st.title("Pao- Spanish- Teacher")
    menu = st.radio("Menú:", ["Inicio", "Lecciones A1", "Contacto"])
    if st.button("Cerrar Sesión"):
        st.session_state.auth = False
        st.rerun()

# --- 4. SECCIONES ---
if menu == "Inicio":
    st.title("¡Bienvenida a tu Academia! ✨")
    st.info("Selecciona 'Lecciones A1' para comenzar a estudiar los 18 temas.")

elif menu == "Lecciones A1":
    st.title("📚 Temario Nivel A1")
    tema_elegido = st.selectbox("Selecciona el tema de hoy:", ["Selecciona..."] + list(DATOS_TEMAS.keys()))

    if tema_elegido != "Selecciona...":
        datos = DATOS_TEMAS[tema_elegido]
        st.header(f"📍 {tema_elegido}")
        
        t_vid, t_dict, t_quiz, t_print = st.tabs(["📺 Video Clase", "🎧 Dictado", "✍️ Quiz / Cuento", "📄 Minilibro"])

        with t_vid:
            if datos["video"] != "URL_YOUTUBE":
                st.video(datos["video"])
            else:
                st.info("🎥 Video próximamente...")

        with t_dict:
            st.subheader("🎧 Desafío de Dictado")
            if 'idx' not in st.session_state: st.session_state.idx = 0
            frases = datos["frases"]
            
            if st.session_state.idx < len(frases):
                actual = frases[st.session_state.idx]
                st.write(f"Frase {st.session_state.idx + 1} de {len(frases)}")
                if st.button("🔊 Escuchar"):
                    gTTS(text=actual, lang='es').save("d.mp3")
                    st.audio("d.mp3")
                resp = st.text_input("Escribe:", key=f"in_{tema_elegido}_{st.session_state.idx}")
                if st.button("Comprobar"):
                    if resp.lower().strip() == actual.lower().strip():
                        st.success("¡Correcto!")
                        st.session_state.idx += 1
                        st.rerun()
            else:
                st.balloons()
                st.success("¡Completado!")
                if st.button("Reiniciar"): st.session_state.idx = 0; st.rerun()

        with t_quiz:
            st.subheader("Pregunta de Repaso")
            st.write("¿Listo para el cuento y el quiz?")
            st.info("Aquí puedes añadir una pregunta rápida sobre el tema.")

        with t_print:
            st.subheader("📄 Material para Imprimir")
            nombre_pdf = datos["pdf"]
            try:
                with open(nombre_pdf, "rb") as f:
                    st.download_button(f"📥 Descargar {nombre_pdf}", f, file_name=nombre_pdf)
            except FileNotFoundError:
                st.warning(f"⚠️ Por favor, sube el archivo '{nombre_pdf}' a GitHub.")

elif menu == "Contacto":
    st.title("📩 Contacto")
    st.write("Email: pao.mzh16@gmail.com")
