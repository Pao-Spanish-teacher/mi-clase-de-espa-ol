import streamlit as st
from gtts import gTTS
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Pao- Spanish- Teacher", page_icon="🎓", layout="wide")

# --- 2. DICCIONARIO MAESTRO DE DATOS ---
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
                {"p": "1. ¿Cómo se llama la niña que juega en la arena?", "o": ["María", "Brisa", "Ana"], "r": "Brisa"},
                {"p": "2. ¿Cuál es la primera palabra que usa Río?", "o": ["Adiós", "Gracias", "Hola"], "r": "Hola"},
                {"p": "3. ¿Qué edad mencionan tener ambos niños?", "o": ["5 años", "7 años", "10 años"], "r": "5 años"},
                {"p": "4. ¿Qué frase usan después de presentarse?", "o": ["De nada", "Mucho gusto", "Perdón"], "r": "Mucho gusto"},
                {"p": "5. ¿Qué palabra usan para despedirse?", "o": ["Hola", "Adiós", "Por favor"], "r": "Adiós"},
                {"p": "6. ¿Qué estaba construyendo Brisa?", "o": ["Una casa", "Un castillo de arena", "Un túnel"], "r": "Un castillo de arena"},
                {"p": "7. ¿En qué lugar se encuentran los niños?", "o": ["En la escuela", "En un parque", "En la playa"], "r": "En un parque"},
                {"p": "8. Si alguien te pregunta cómo estás, respondes:", "o": ["¡Qué mal!", "Estoy bien, gracias", "No quiero hablar"], "r": "Estoy bien, gracias"},
                {"p": "9. Si es de mañana, debes decir:", "o": ["Buenas noches", "Buenos días", "Hasta luego"], "r": "Buenos días"},
                {"p": "10. ¿Cómo se llama el niño?", "o": ["Mar", "Río", "Lago"], "r": "Río"}
            ],
            "completar": [
                {"p": "11. Cuando Río quiere saber cómo se siente su amiga, pregunta: '¿Cómo __________?'", "r": "estás"},
                {"p": "12. Para conocer el nombre de la niña, el niño pregunta: '¿Cómo te __________?'", "r": "llamas"},
                {"p": "13. Río le cuenta a Brisa el lugar donde reside diciendo: 'Yo vivo en la __________'", "r": "ciudad"},
                {"p": "14. Para pedir algo de forma educada, siempre debemos usar la frase: '__________ favor'", "r": "Por"},
                {"p": "15. Si los niños se volvieran a ver al día siguiente, podrían despedirse diciendo: 'Hasta __________'", "r": "mañana"},
                {"p": "16. Al recibir un cumplido o una ayuda, la palabra mágica es: '__________'", "r": "Gracias"},
                {"p": "17. Brisa y Río decidieron que a partir de ese momento serían muy buenos __________", "r": "amigos"},
                {"p": "18. Si saludas a alguien por la tarde, la expresión correcta es 'Buenas __________'", "r": "tardes"},
                {"p": "19. Cuando te presentan a alguien dices 'Encantado' o 'Mucho __________'", "r": "gusto"},
                {"p": "20. El nombre de la niña es __________ y el nombre del niño es Río.", "r": "Brisa"}
            ]
        }
    },
    "2. Los Números (0-100)": {"video": "https://www.youtube.com/watch?v=nxMBJQAE2ZU", "pdf": "Minilibros Los números.pdf", "frases": ["Diez", "Cincuenta", "Cien"]},
    "3. Los Colores": {"video": "https://www.youtube.com/watch?v=UF5HWnCrAU8", "pdf": "Minilibro Colores.pdf", "frases": ["Rojo", "Azul", "Amarillo"]},
    "4. Días, Meses y Estaciones": {
        "video": "https://www.youtube.com/watch?v=T9fvfbMQn2I", 
        "cuento": "https://www.youtube.com/watch?v=h1K6BKCX6g8",
        "pdf": "Minilibro Tiempo.pdf", 
        "frases": ["Enero", "Lunes", "Verano"],
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. ¿Cuál es el primer mes del año?", "o": ["Febrero", "Enero", "Marzo"], "r": "Enero"},
                {"p": "2. ¿Cuál es el mes más corto del año?", "o": ["Abril", "Febrero", "Junio"], "r": "Febrero"},
                {"p": "3. ¿En qué mes se celebra la Navidad?", "o": ["Noviembre", "Octubre", "Diciembre"], "r": "Diciembre"},
                {"p": "4. ¿Qué mes sigue después de agosto?", "o": ["Septiembre", "Julio", "Octubre"], "r": "Septiembre"},
                {"p": "5. ¿Cuál es el mes número seis del año?", "o": ["Mayo", "Junio", "Julio"], "r": "Junio"},
                {"p": "6. ¿Qué mes está antes de noviembre?", "o": ["Septiembre", "Octubre", "Diciembre"], "r": "Octubre"},
                {"p": "7. ¿Cuál de estos meses tiene solo 30 días?", "o": ["Enero", "Abril", "Marzo"], "r": "Abril"},
                {"p": "8. ¿Qué mes es el octavo (8°) del calendario?", "o": ["Julio", "Agosto", "Septiembre"], "r": "Agosto"},
                {"p": "9. ¿En qué mes comienza el año?", "o": ["Enero", "Junio", "Diciembre"], "r": "Enero"},
                {"p": "10. ¿Cuál es el último mes del año?", "o": ["Octubre", "Noviembre", "Diciembre"], "r": "Diciembre"}
            ],
            "completar": [
                {"p": "11. El mes que está entre marzo y mayo se llama __________.", "r": "Abril"},
                {"p": "12. Si hoy es el último día de junio, mañana empieza __________.", "r": "Julio"},
                {"p": "13. El mes número 5, famoso por las flores, es __________.", "r": "Mayo"},
                {"p": "14. El décimo mes, entre septiembre y noviembre, es __________.", "r": "Octubre"},
                {"p": "15. Un año completo tiene un total de __________ meses.", "r": "doce"},
                {"p": "16. El mes que sigue después de enero es __________.", "r": "Febrero"},
                {"p": "17. El mes número tres del año se llama __________.", "r": "Marzo"},
                {"p": "18. Antes de diciembre, estamos en el mes de __________.", "r": "Noviembre"},
                {"p": "19. El noveno mes del año es __________.", "r": "Septiembre"},
                {"p": "20. El mes número siete del año es __________.", "r": "Julio"}
            ]
        }
    },
    "5. La Hora": {"video": "https://youtu.be/CbqNMMNza9w", "pdf": "Minilibro Hora.pdf"},
    "12. Comida y Bebidas": {"video": "https://www.youtube.com/watch?v=9iPhcCg64j8", "pdf": "Minilibro Comida.pdf", "frases": ["Agua", "Manzana"]}
}

# --- 3. SEGURIDAD ---
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

# --- 4. MENÚ LATERAL ---
with st.sidebar:
    st.title("Pao- Spanish")
    menu = st.radio("Navegación:", ["Inicio", "Gramática Española", "Lecciones A1", "Contacto"])
    if st.button("Cerrar Sesión"):
        st.session_state.auth = False
        st.rerun()

# --- 5. LÓGICA DE SECCIONES ---

if menu == "Inicio":
    st.title("¡Bienvenida a tu Academia! ✨")
    st.write("Selecciona una sección en el menú de la izquierda para comenzar.")

elif menu == "Gramática Española":
    st.title("📖 Gramática Española")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("1. El Alfabeto"); st.video("https://www.youtube.com/watch?v=NMgN5gsvhWk") 
        st.subheader("3. El Género"); st.video("https://www.youtube.com/watch?v=FSqRurjGIqw")
        st.subheader("5. Número Gramatical"); st.video("https://www.youtube.com/watch?v=VU5ylA-WjI8")
        st.subheader("7. Artículos"); st.video("https://www.youtube.com/watch?v=rLL0NWpz6IE")
        st.subheader("9. Pronombres"); st.video("https://www.youtube.com/watch?v=LorQtNAKeb4")
        st.subheader("11. Verbos Movimiento"); st.video("https://www.youtube.com/watch?v=2o4sO1IS3oM")
        st.subheader("13. Tiempos Verbales"); st.video("https://www.youtube.com/watch?v=KA2RryvqfIM")
    with c2:
        st.subheader("2. Preguntas Comunes"); st.video("https://www.youtube.com/watch?v=gLnuqh-CUNQ")
        st.subheader("4. Singular y Plural"); st.video("https://www.youtube.com/watch?v=h9pCzNZ1jTI")
        st.subheader("6. Opuestos"); st.video("https://youtu.be/fADLwhd43ac")
        st.subheader("8. Opuestos 1"); st.video("https://www.youtube.com/watch?v=icJML1BE9qA")
        st.subheader("10. Viajes"); st.video("https://www.youtube.com/watch?v=UI1Bmk3_q08")
        st.subheader("12. Oraciones"); st.video("https://www.youtube.com/watch?v=JKt16i6BwkM")

elif menu == "Lecciones A1":
    st.title("📚 Lecciones Nivel A1")
    tema = st.selectbox("Selecciona un tema:", ["Selecciona..."] + list(DATOS_TEMAS.keys()))
    
    if tema != "Selecciona...":
        d = DATOS_TEMAS[tema]
        tab1, tab2, tab3, tab4 = st.tabs(["📺 Clase", "🎧 Dictado", "📖 Cuento", "📄 Material"])
        
        with tab1:
            if "video" in d: st.video(d["video"])
        
        with tab2:
            st.subheader("🎧 Dictado Interactivo")
            frases = d.get("frases", [])
            if frases:
                if 'it' not in st.session_state: st.session_state.it = 0
                if st.session_state.it < len(frases):
                    txt = frases[st.session_state.it]
                    if st.button("🔊 Escuchar"):
                        gTTS(text=txt, lang='es').save("s.mp3")
                        st.audio("s.mp3")
                    u_in = st.text_input("Escribe lo que oyes:", key=f"in_{tema}_{st.session_state.it}")
                    if st.button("Comprobar"):
                        if u_in.lower().strip() == txt.lower().strip():
                            st.success("¡Muy bien!"); st.session_state.it += 1; st.rerun()
                        else: st.error("Error, intenta otra vez.")
                else:
                    st.success("¡Felicidades, terminaste el dictado!"); st.button("Reiniciar", on_click=lambda: st.session_state.update({"it":0}))
            else: st.info("Próximamente")

        with tab3:
            if "cuento" in d:
                st.video(d["cuento"])
                if "quiz_cuento" in d:
                    st.divider()
                    st.write("### ✍️ Parte I: Selección")
                    r_sel = {}
                    for i in d["quiz_cuento"]["seleccion"]:
                        r_sel[i["p"]] = st.radio(i["p"], i["o"], key=f"r_{i['p']}")
                    
                    st.write("### ✏️ Parte II: Completación")
                    r_comp = {}
                    for i in d["quiz_cuento"]["completar"]:
                        r_comp[i["p"]] = st.text_input(i["p"], key=f"c_{i['p']}")
                    
                    if st.button("Corregir"):
                        err = 0
                        for i in d["quiz_cuento"]["seleccion"]:
                            if r_sel[i["p"]] != i["r"]: err += 1
                        for i in d["quiz_cuento"]["completar"]:
                            if r_comp[i["p"]].lower().strip() != i["r"].lower(): err += 1
                        
                        if err == 0: st.balloons(); st.success("¡Excelente trabajo!")
                        else: st.warning(f"Tienes {err} errores. Revisa el video.")
            else: st.info("Aún no hay cuento para este tema.")

        with tab4:
            if "pdf" in d:
                st.write(f"Descargar material de: {tema}")
                st.info("Asegúrate de haber subido el archivo PDF a GitHub con el nombre correcto.")
            else: st.info("No hay archivos PDF aún.")

elif menu == "Contacto":
    st.title("📩 Contacto")
    st.write("Dudas o soporte: pao.mzh16@gmail.com")
