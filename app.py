import streamlit as st
from gtts import gTTS
import os

# --- 1. CONFIGURACIÓN Y DATOS MAESTROS ---
st.set_page_config(page_title="Pao- Spanish- Teacher", page_icon="🎓", layout="wide")

# Diccionario actualizado con tus nuevos enlaces
DATOS_TEMAS = {
    "1. Saludos y Despedidas": {
        "video": "https://www.youtube.com/watch?v=hll10VBLFoQ",
        "video2": "https://www.youtube.com/watch?v=84FNM-Ni-6U",
        "video3": "https://www.youtube.com/watch?v=4txmiiR10wM",
        "pdf": "minilibro Saludos.pdf",
        "frases": ["Buenos días", "¿Cómo estás?", "Mucho gusto", "Hasta mañana"]
    },
    "2. Los Números (0-100)": {
        "video": "https://www.youtube.com/watch?v=nxMBJQAE2ZU",
        "video2": "https://www.youtube.com/watch?v=u_BAr1fjILU",
        "pdf": "Minilibros Los números en español (0-100).pdf",
        "frases": ["Diez", "Cincuenta", "Cien"]
    },
    "3. Los Colores": {
        "video": "https://www.youtube.com/watch?v=UF5HWnCrAU8",
        "pdf": "Minilibro Los colores en español.pdf",
        "frases": ["Rojo", "Azul", "Verde"]
    },
    "4. Días, Meses y Estaciones": {
        "video": "https://www.youtube.com/watch?v=T9fvfbMQn2I",
        "video2": "https://www.youtube.com/watch?v=mhI73gkjtwk",
        "pdf": "Minilibro Los días, los meses y las estaciones.pdf",
        "frases": ["Lunes", "Enero", "Verano"]
    },
    "5. La Hora": {
        "video": "https://youtu.be/CbqNMMNza9w",
        "video2": "https://www.youtube.com/watch?v=xmeIIuBwxu4",
        "pdf": "Minilibro La Hora en Español.pdf",
        "frases": ["Es la una", "Son las dos", "En punto"]
    },
    "6. La Familia": {
        "video": "https://www.youtube.com/watch?v=4C9JiqgMt8o",
        "pdf": "minilibro La familia en español.pdf",
        "frases": ["Mi madre", "Mi padre", "Mi abuelo"]
    },
    "7. Las Profesiones": {
        "video": "https://www.youtube.com/watch?v=szed1no5viA",
        "pdf": "Minilibro Las profesiones en español.pdf",
        "frases": ["Doctor", "Maestra", "Ingeniero"]
    },
    "8. Profesiones Técnicas": {
        "video": "https://www.youtube.com/watch?v=jnyMcesUtsI",
        "pdf": "Minilibro Las profesiones técnicas en español.pdf",
        "frases": ["Técnico", "Mecánico", "Electricista"]
    },
    "9. Nacionalidad y Países": {
        "video": "https://www.youtube.com/watch?v=T2HVf4YqHZY",
        "pdf": "Minilibros Los países y nacionalidades en español.pdf",
        "frases": ["España", "México", "Soy colombiano"]
    },
    "10. Partes del Cuerpo": {
        "video": "https://www.youtube.com/watch?v=OfX0hCFCdeA",
        "pdf": "Minilibro Las partes del cuerpo en español.pdf",
        "frases": ["La cabeza", "La mano", "El pie"]
    },
    "11. La Ropa y Vestimenta": {
        "video": "https://www.youtube.com/watch?v=nOisiL-Pyak",
        "pdf": "Minilibro La ropa y la vestimenta en español.pdf",
        "frases": ["La camisa", "Los zapatos", "El vestido"]
    },
    "12. Comida y Bebidas": {
        "video": "https://www.youtube.com/watch?v=9iPhcCg64j8",
        "video2": "https://www.youtube.com/watch?v=LgpwYTK9RTc",
        "pdf": "Minilibro Comidas y Bebidas en Español..pdf",
        "frases": ["Manzana", "Agua", "Comida"]
    },
    "13. La Casa": {
        "video": "https://youtu.be/2Wz5yyw80gs",
        "pdf": "Minilibro La casa y sus partes en español.pdf",
        "frases": ["La sala", "La cocina", "Mi cuarto"]
    },
    "14. Objetos Cotidianos": {
        "video": "URL_YOUTUBE",
        "pdf": "Minilibros Los objetos cotidianos en español.pdf",
        "frases": ["La mesa", "La silla"]
    },
    "15. Medios de Transporte": {
        "video": "URL_YOUTUBE",
        "pdf": "Minilibros Los medios de transporte en español.pdf",
        "frases": ["El carro", "El avión"]
    },
    "16. Los Lugares": {
        "video": "https://www.youtube.com/watch?v=DziT1MJLmk4",
        "video2": "https://www.youtube.com/watch?v=Ss_2il1-Sm8",
        "pdf": "Minilibro Los lugares en español.pdf",
        "frases": ["El cine", "La escuela", "El hospital"]
    },
    "17. Animales Domésticos": {
        "video": "https://www.youtube.com/watch?v=G2n_FA_vhPU",
        "pdf": "Minilibro Los animales domésticos en español.pdf",
        "frases": ["El perro", "El gato", "El conejo"]
    },
    "18. Animales Salvajes": {
        "video": "URL_YOUTUBE",
        "pdf": "Minilibro Los animales salvajes en español.pdf",
        "frases": ["El león", "El tigre"]
    }
}

# --- 2. CONTROL DE ACCESO ---
CONTRASEÑA = "pao_premium"
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("🎓 Academia Pao- Spanish- Teacher")
    clave = st.text_input("Clave de alumno:", type="password")
    if st.button("Ingresar"):
        if clave == CONTRASEÑA:
            st.session_state.auth = True
            st.rerun()
        else: st.error("❌ Clave incorrecta")
    st.stop()

# --- 3. BARRA LATERAL ---
with st.sidebar:
    st.title("Pao- Spanish")
    menu = st.radio("Secciones:", ["Inicio", "Lecciones A1", "Contacto"])
    if st.button("Cerrar Sesión"):
        st.session_state.auth = False
        st.rerun()

# --- 4. SECCIONES ---
if menu == "Inicio":
    st.title("¡Bienvenida a tu Academia! ✨")
    st.write("Tu plataforma está lista con los videos y minilibros actualizados.")

elif menu == "Lecciones A1":
    st.title("📚 Temario Nivel A1")
    tema_elegido = st.selectbox("Elige un tema:", ["Selecciona..."] + list(DATOS_TEMAS.keys()))

    if tema_elegido != "Selecciona...":
        datos = DATOS_TEMAS[tema_elegido]
        st.header(f"📍 {tema_elegido}")
        
        t_vid, t_dict, t_quiz, t_print = st.tabs(["📺 Video Clase", "🎧 Dictado", "✍️ Quiz", "📄 Minilibro para Imprimir"])

        with t_vid:
            st.subheader("📺 Material Audiovisual")
            
            # Mostrar Video 1
            if datos["video"] != "URL_YOUTUBE":
                st.info("🎥 Video Parte 1")
                st.video(datos["video"])
            
            # Mostrar Video 2 si existe
            if "video2" in datos:
                st.markdown("---")
                st.info("🎥 Video Parte 2")
                st.video(datos["video2"])

            # Mostrar Video 3 si existe (especial para Saludos)
            if "video3" in datos:
                st.markdown("---")
                st.info("🎥 Video Parte 3")
                st.video(datos["video3"])

        with t_dict:
            st.subheader("🎧 Practica tu oído")
            if 'idx' not in st.session_state: st.session_state.idx = 0
            frases = datos["frases"]
            
            if st.session_state.idx < len(frases):
                actual = frases[st.session_state.idx]
                st.write(f"Frase {st.session_state.idx + 1} de {len(frases)}")
                if st.button("🔊 Escuchar"):
                    gTTS(text=actual, lang='es').save("d.mp3")
                    st.audio("d.mp3")
                resp = st.text_input("Escribe lo que escuchas:", key=f"d_{tema_elegido}_{st.session_state.idx}")
                if st.button("Comprobar"):
                    if resp.lower().strip() == actual.lower().strip():
                        st.success("¡Excelente!")
                        st.session_state.idx += 1
                        st.rerun()
            else:
                st.balloons()
                st.success("🎊 ¡Completado!")
                if st.button("Reiniciar"): st.session_state.idx = 0; st.rerun()

        with t_quiz:
            st.subheader("✍️ Quiz")
            st.write("Aquí podrás añadir tus preguntas interactivas.")

        with t_print:
            st.subheader("📄 Material de Estudio")
            nombre_pdf = datos["pdf"]
            try:
                with open(nombre_pdf, "rb") as f:
                    st.download_button(f"📥 Descargar Minilibro", f, file_name=nombre_pdf)
            except FileNotFoundError:
                st.warning(f"⚠️ Sube '{nombre_pdf}' a GitHub.")

elif menu == "Contacto":
    st.title("📩 Contacto")
    st.write("pao.mzh16@gmail.com")
