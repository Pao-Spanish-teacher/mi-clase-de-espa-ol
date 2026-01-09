import streamlit as st
from gtts import gTTS
import os

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Pao- Spanish- Teacher", page_icon="🎓", layout="wide")

# --- 2. DICCIONARIO MAESTRO CON TODOS LOS TEMAS ---
DATOS_TEMAS = {
    "1. Saludos y Despedidas": {
        "video": "https://www.youtube.com/watch?v=hll10VBLFoQ", 
        "video2": "https://www.youtube.com/watch?v=84FNM-Ni-6U", 
        "video3": "https://www.youtube.com/watch?v=4txmiiR10wM",
        "cuento": "https://www.youtube.com/watch?v=yhH8rwpEHRo",
        "pdf": "minilibro Saludos.pdf", 
        "frases": ["Buenos días", "¿Cómo estás?", "Mucho gusto", "Hasta mañana"],
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. ¿Cómo se llama la niña que está jugando en la arena?", "o": ["María", "Brisa", "Ana"], "r": "Brisa"},
                {"p": "2. ¿Cuál es la primera palabra que usa Río para saludar?", "o": ["Adiós", "Gracias", "Hola"], "r": "Hola"},
                {"p": "3. ¿Qué edad mencionan tener ambos niños?", "o": ["5 años", "7 años", "10 años"], "r": "5 años"},
                {"p": "4. ¿Qué frase de cortesía usan después de presentarse?", "o": ["De nada", "Mucho gusto", "Perdón"], "r": "Mucho gusto"},
                {"p": "5. ¿Qué palabra usan para despedirse?", "o": ["Hola", "Adiós", "Por favor"], "r": "Adiós"},
                {"p": "6. ¿Qué estaba construyendo Brisa?", "o": ["Una casa", "Un castillo de arena", "Un túnel"], "r": "Un castillo de arena"},
                {"p": "7. ¿En qué lugar se encuentran los niños?", "o": ["En la escuela", "En un parque", "En la playa"], "r": "En un parque"},
                {"p": "8. Si alguien te pregunta cómo estás, respondes:", "o": ["¡Qué mal!", "Estoy bien, gracias", "No quiero hablar"], "r": "Estoy bien, gracias"},
                {"p": "9. Si es de mañana, debes decir:", "o": ["Buenas noches", "Buenos días", "Hasta luego"], "r": "Buenos días"},
                {"p": "10. ¿Cómo se llama el niño que se acerca?", "o": ["Mar", "Río", "Lago"], "r": "Río"}
            ],
            "completar": [
                {"p": "11. Cuando Río quiere saber cómo se siente su amiga, pregunta: '¿Cómo __________?'", "r": "estás"},
                {"p": "12. Para conocer el nombre de la niña, pregunta: '¿Cómo te __________?'", "r": "llamas"},
                {"p": "13. Río le cuenta a Brisa: 'Yo vivo en la __________'", "r": "ciudad"},
                {"p": "14. Para pedir algo educadamente: '__________ favor'", "r": "Por"},
                {"p": "15. Si se ven al día siguiente: 'Hasta __________'", "r": "mañana"},
                {"p": "16. Palabra mágica: '__________'", "r": "Gracias"},
                {"p": "17. Brisa y Río decidieron que serían buenos __________", "r": "amigos"},
                {"p": "18. Si saludas por la tarde: 'Buenas __________'", "r": "tardes"},
                {"p": "19. Cuando te sientes feliz de conocerle: 'Mucho __________'", "r": "gusto"},
                {"p": "20. La niña es __________ y el niño es Río.", "r": "Brisa"}
            ]
        }
    },
    "2. Los Números (0-100)": {"video": "https://www.youtube.com/watch?v=nxMBJQAE2ZU", "video2": "https://www.youtube.com/watch?v=u_BAr1fjILU", "pdf": "Minilibros Los números.pdf", "frases": ["Diez", "Cincuenta", "Cien"]},
    "3. Los Colores": {"video": "https://www.youtube.com/watch?v=UF5HWnCrAU8", "pdf": "Minilibro Colores.pdf", "frases": ["Rojo", "Azul", "Amarillo"]},
    "4. Días, Meses y Estaciones": {"video": "https://www.youtube.com/watch?v=T9fvfbMQn2I", "video2": "https://www.youtube.com/watch?v=mhI73gkjtwk", "pdf": "Minilibro Tiempo.pdf", "frases": ["Lunes", "Enero", "Verano"]},
    "5. La Hora": {"video": "https://youtu.be/CbqNMMNza9w", "video2": "https://www.youtube.com/watch?v=xmeIIuBwxu4", "pdf": "Minilibro Hora.pdf", "frases": ["Es la una", "Son las dos"]},
    "6. La Familia": {"video": "https://www.youtube.com/watch?v=4C9JiqgMt8o", "pdf": "Minilibro Familia.pdf", "frases": ["Mi padre", "Mi abuela"]},
    "7. Las Profesiones": {"video": "https://www.youtube.com/watch?v=szed1no5viA", "pdf": "Minilibro Profesiones.pdf", "frases": ["Doctor", "Maestra"]},
    "8. Profesiones Técnicas": {"video": "https://www.youtube.com/watch?v=jnyMcesUtsI", "pdf": "Minilibro Tecnicos.pdf", "frases": ["Mecánico", "Electricista"]},
    "9. Nacionalidad y Países": {"video": "https://www.youtube.com/watch?v=T2HVf4YqHZY", "pdf": "Minilibro Paises.pdf", "frases": ["México", "España", "Colombia"]},
    "10. Partes del Cuerpo": {"video": "https://www.youtube.com/watch?v=OfX0hCFCdeA", "pdf": "Minilibro Cuerpo.pdf", "frases": ["Cabeza", "Brazos", "Piernas"]},
    "11. La Ropa y Vestimenta": {"video": "https://www.youtube.com/watch?v=nOisiL-Pyak", "pdf": "Minilibro Ropa.pdf", "frases": ["Camisa", "Zapatos", "Pantalón"]},
    "12. Comida y Bebidas": {"video": "https://www.youtube.com/watch?v=9iPhcCg64j8", "video2": "https://www.youtube.com/watch?v=LgpwYTK9RTc", "pdf": "Minilibro Comida.pdf", "frases": ["Agua", "Manzana", "Pan"]},
    "13. La Casa": {"video": "https://youtu.be/2Wz5yyw80gs", "pdf": "Minilibro Casa.pdf", "frases": ["Cocina", "Habitación"]},
    "14. Objetos Cotidianos": {"video": "URL_PROXIMO", "pdf": "Minilibro Objetos.pdf", "frases": ["Mesa", "Silla"]},
    "15. Medios de Transporte": {"video": "URL_PROXIMO", "pdf": "Minilibro Transporte.pdf", "frases": ["Carro", "Avión"]},
    "16. Los Lugares": {"video": "https://www.youtube.com/watch?v=DziT1MJLmk4", "video2": "https://www.youtube.com/watch?v=Ss_2il1-Sm8", "pdf": "Minilibro Lugares.pdf", "frases": ["Cine", "Parque"]},
    "17. Animales Domésticos": {"video": "https://www.youtube.com/watch?v=G2n_FA_vhPU", "pdf": "Minilibro AnimalesD.pdf", "frases": ["Perro", "Gato"]},
    "18. Animales Salvajes": {"video": "URL_PROXIMO", "pdf": "Minilibro AnimalesS.pdf", "frases": ["León", "Tigre"]}
}

# --- 3. CONTROL DE ACCESO ---
CONTRASEÑA = "pao_premium"
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("🎓 Academia Pao- Spanish- Teacher")
    clave = st.text_input("Ingresa tu clave de alumno:", type="password")
    if st.button("Entrar"):
        if clave == CONTRASEÑA:
            st.session_state.auth = True
            st.rerun()
        else: st.error("Clave incorrecta")
    st.stop()

# --- 4. BARRA LATERAL ---
with st.sidebar:
    st.title("Pao- Spanish")
    menu = st.radio("Menú Principal:", ["Inicio", "Gramática Española", "Lecciones A1", "Contacto"])
    if st.button("Cerrar Sesión"):
        st.session_state.auth = False
        st.rerun()

# --- 5. LÓGICA DE SECCIONES ---
if menu == "Inicio":
    st.title("¡Bienvenida a tu Academia! ✨")
    st.write("Explora las secciones para comenzar.")

elif menu == "Gramática Española":
    st.title("📖 Gramática Española")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("1. El Alfabeto"); st.video("https://www.youtube.com/watch?v=NMgN5gsvhWk") 
        st.subheader("3. El Género Gramatical"); st.video("https://www.youtube.com/watch?v=FSqRurjGIqw")
        st.subheader("5. Número Gramatical"); st.video("https://www.youtube.com/watch?v=VU5ylA-WjI8")
        st.subheader("7. Artículos Definidos e Indefinidos"); st.video("https://www.youtube.com/watch?v=rLL0NWpz6IE")
        st.subheader("9. Pronombres Personales"); st.video("https://www.youtube.com/watch?v=LorQtNAKeb4")
        st.subheader("11. Verbos de Movimiento"); st.video("https://www.youtube.com/watch?v=2o4sO1IS3oM")
        st.subheader("13. Tiempos Verbales"); st.video("https://www.youtube.com/watch?v=KA2RryvqfIM")
    with col2:
        st.subheader("2. Preguntas Comunes"); st.video("https://www.youtube.com/watch?v=gLnuqh-CUNQ")
        st.subheader("4. Singular y Plural"); st.video("https://www.youtube.com/watch?v=h9pCzNZ1jTI")
        st.subheader("6. Palabras Opuestas"); st.video("https://youtu.be/fADLwhd43ac")
        st.subheader("8. Palabras Opuestas 1"); st.video("https://www.youtube.com/watch?v=icJML1BE9qA")
        st.subheader("10. Preguntas y Frases al Viajar"); st.video("https://www.youtube.com/watch?v=UI1Bmk3_q08")
        st.subheader("12. Formar Oraciones en Español"); st.video("https://www.youtube.com/watch?v=JKt16i6BwkM")

elif menu == "Lecciones A1":
    st.title("📚 Temario Nivel A1")
    tema_elegido = st.selectbox("Elige un tema:", ["Selecciona..."] + list(DATOS_TEMAS.keys()))

    if tema_elegido != "Selecciona...":
        datos = DATOS_TEMAS[tema_elegido]
        st.header(f"📍 {tema_elegido}")
        t_vid, t_dict, t_story, t_print = st.tabs(["📺 Video Clase", "🎧 Dictado", "📖 Cuento y Práctica", "📄 Material para Imprimir"])

        with t_vid:
            st.subheader("📺 Material Audiovisual")
            if "video" in datos: st.video(datos["video"])
            if "video2" in datos: st.markdown("---"); st.video(datos["video2"])
            if "video3" in datos: st.markdown("---"); st.video(datos["video3"])

        with t_dict:
            st.subheader("🎧 Practica tu oído")
            if 'idx' not in st.session_state: st.session_state.idx = 0
            frases = datos.get("frases", [])
            if st.session_state.idx < len(frases):
                actual = frases[st.session_state.idx]
                st.write(f"Frase {st.session_state.idx + 1} de {len(frases)}")
                if st.button("🔊 Escuchar"):
                    gTTS(text=actual, lang='es').save("d.mp3")
                    st.audio("d.mp3")
                resp = st.text_input("Escribe lo que escuchas:", key=f"d_{tema_elegido}_{st.session_state.idx}")
                if st.button("Comprobar"):
                    if resp.lower().strip() == actual.lower().strip():
                        st.success("¡Excelente!"); st.session_state.idx += 1; st.rerun()
            else:
                st.success("🎊 ¡Completado!")
                if st.button("Reiniciar"): st.session_state.idx = 0; st.rerun()

        with t_story:
            st.subheader("🎬 Mira el cuento y resuelve")
            if "cuento" in datos:
                st.video(datos["cuento"])
                st.markdown("---")
                if "quiz_cuento" in datos:
                    st.write("### ✍️ Parte I: Selección Múltiple")
                    resp_sel = {}
                    for item in datos["quiz_cuento"]["seleccion"]:
                        resp_sel[item["p"]] = st.radio(item["p"], item["o"], key=f"sel_{tema_elegido}_{item['p']}")
                    
                    st.markdown("---")
                    st.write("### ✏️ Parte II: Completación")
                    resp_comp = {}
                    for item in datos["quiz_cuento"]["completar"]:
                        resp_comp[item["p"]] = st.text_input(item["p"], key=f"comp_{tema_elegido}_{item['p']}")
                    
                    if st.button("Verificar Respuestas"):
                        err = 0
                        for item in datos["quiz_cuento"]["seleccion"]:
                            if resp_sel[item["p"]] != item["r"]: err += 1
                        for item in datos["quiz_cuento"]["completar"]:
                            if resp_comp[item["p"]].lower().strip() != item["r"].lower(): err += 1
                        
                        if err == 0:
                            st.balloons(); st.success("✨ ¡Perfecto! Has comprendido todo.")
                        else:
                            st.warning(f"⚠️ Tienes {err} errores. ¡Vuelve a ver el video para encontrar la respuesta correcta!")
            else:
                st.info("📌 El video del cuento estará disponible pronto.")

        with t_print:
            st.subheader("📄 Material para Imprimir")
            col1, col2 = st.columns(2)
            with col1:
                st.write("#### 📘 Minilibro")
                if "pdf" in datos:
                    try:
                        with open(datos["pdf"], "rb") as f:
                            st.download_button("📥 Descargar", f, file_name=datos["pdf"], key=f"btn_p_{tema_elegido}")
                    except: st.warning("Archivo no encontrado.")
            with col2:
                st.write("#### 📝 Fichas")
                st.info("Próximamente.")

elif menu == "Contacto":
    st.title("📩 Contacto")
    st.write("pao.mzh16@gmail.com")
