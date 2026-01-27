import streamlit as st
from gtts import gTTS
import os

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Pao- Spanish- Teacher", page_icon="🎓", layout="wide")

# --- 2. DICCIONARIO MAESTRO CON LOS 18 TEMAS ---
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
                {"p": "2. ¿Cuál es la primera palabra que usa Río?", "o": ["Adiós", "Gracias", "Hola"], "r": "Hola"},
                {"p": "3. ¿Qué edad mencionan tener ambos niños?", "o": ["5 años", "7 años", "10 años"], "r": "5 años"},
                {"p": "4. ¿Qué frase de cortesía usan después de presentarse?", "o": ["De nada", "Mucho gusto", "Perdón"], "r": "Mucho gusto"},
                {"p": "5. ¿Qué palabra usan para despedirse?", "o": ["Hola", "Adiós", "Por favor"], "r": "Adiós"},
                {"p": "6. ¿Qué estaba construyendo Brisa?", "o": ["Una casa", "Un castillo de arena", "Un túnel"], "r": "Un castillo de arena"},
                {"p": "7. ¿En qué lugar se encuentran los niños?", "o": ["En la escuela", "En un parque", "En la playa"], "r": "En un parque"},
                {"p": "8. Al saludarte, respondes:", "o": ["¡Qué mal!", "Estoy bien, gracias", "No quiero hablar"], "r": "Estoy bien, gracias"},
                {"p": "9. Por la mañana dices:", "o": ["Buenas noches", "Buenos días", "Hasta luego"], "r": "Buenos días"},
                {"p": "10. ¿Cómo se llama el niño?", "o": ["Mar", "Río", "Lago"], "r": "Río"}
            ],
            "completar": [
                {"p": "11. Río pregunta: '¿Cómo __________?'", "r": "estás"},
                {"p": "12. Río pregunta: '¿Cómo te __________?'", "r": "llamas"},
                {"p": "13. 'Yo vivo en la __________'", "r": "ciudad"},
                {"p": "14. Frase educada: '__________ favor'", "r": "Por"},
                {"p": "15. Despedida para mañana: 'Hasta __________'", "r": "mañana"},
                {"p": "16. Palabra mágica: '__________'", "r": "Gracias"},
                {"p": "17. Serían muy buenos __________", "r": "amigos"},
                {"p": "18. Saludo por la tarde: 'Buenas __________'", "r": "tardes"},
                {"p": "19. Feliz de conocerle: 'Mucho __________'", "r": "gusto"},
                {"p": "20. La niña es __________ y el niño es Río.", "r": "Brisa"}
            ]
        }
    },
    "2. Los Números (0-100)": {"video": "https://www.youtube.com/watch?v=nxMBJQAE2ZU", "video2": "https://www.youtube.com/watch?v=u_BAr1fjILU", "pdf": "Minilibros Los números en español (0-100).pdf", "frases": ["Diez", "Cincuenta", "Cien"]},
    "3. Los Colores": {"video": "https://www.youtube.com/watch?v=UF5HWnCrAU8", "pdf": "Minilibro Los colores en español.pdf", "frases": ["Rojo", "Azul", "Verde"]},
    "4. Días, Meses y Estaciones": {
        "video": "https://www.youtube.com/watch?v=T9fvfbMQn2I", 
        "video2": "https://www.youtube.com/watch?v=mhI73gkjtwk", 
        "cuento": "https://www.youtube.com/watch?v=h1K6BKCX6g8",
        "pdf": "Minilibro Los días, los meses y las estaciones.pdf", 
        "frases": ["Enero", "Lunes", "Verano"],
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. ¿Primer mes del año?", "o": ["Febrero", "Enero", "Marzo"], "r": "Enero"},
                {"p": "2. ¿Mes más corto?", "o": ["Abril", "Febrero", "Junio"], "r": "Febrero"},
                {"p": "3. ¿Cuándo es Navidad?", "o": ["Noviembre", "Octubre", "Diciembre"], "r": "Diciembre"},
                {"p": "4. ¿Qué mes sigue a agosto?", "o": ["Septiembre", "Julio", "Octubre"], "r": "Septiembre"},
                {"p": "5. ¿Mes número seis?", "o": ["Mayo", "Junio", "Julio"], "r": "Junio"}
            ],
            "completar": [
                {"p": "11. Entre marzo y mayo está __________.", "r": "Abril"},
                {"p": "15. El año tiene __________ meses.", "r": "doce"},
                {"p": "20. El mes siete es __________.", "r": "Julio"}
            ]
        }
    },
    "5. La Hora": {"video": "https://youtu.be/CbqNMMNza9w", "video2": "https://www.youtube.com/watch?v=xmeIIuBwxu4", "pdf": "Minilibro La Hora en Español.pdf"},
    "6. La Familia": {"video": "https://www.youtube.com/watch?v=4C9JiqgMt8o", "pdf": "minilibro La familia en español.pdf"},
    "7. Las Profesiones": {"video": "https://www.youtube.com/watch?v=szed1no5viA", "pdf": "Minilibro Las profesiones en español.pdf"},
    "8. Profesiones Técnicas": {"video": "https://www.youtube.com/watch?v=jnyMcesUtsI", "pdf": "Minilibro Las profesiones técnicas en español.pdf"},
    "9. Nacionalidad y Países": {"video": "https://www.youtube.com/watch?v=T2HVf4YqHZY", "pdf": "Minilibros Los países y nacionalidades en español.pdf"},
    "10. Partes del Cuerpo": {"video": "https://www.youtube.com/watch?v=OfX0hCFCdeA", "pdf": "Minilibro Las partes del cuerpo en español.pdf"},
    "11. La Ropa y Vestimenta": {"video": "https://www.youtube.com/watch?v=nOisiL-Pyak", "pdf": "Minilibro La ropa y la vestimenta en español.pdf"},
    "12. Comida y Bebidas": {"video": "https://www.youtube.com/watch?v=9iPhcCg64j8", "video2": "https://www.youtube.com/watch?v=LgpwYTK9RTc", "pdf": "Minilibro Comidas y Bebidas en Español..pdf"},
    "13. La Casa": {"video": "https://youtu.be/2Wz5yyw80gs", "pdf": "Minilibro La casa y sus partes en español.pdf"},
    "14. Objetos Cotidianos": {"video": "", "pdf": "Minilibros Los objetos cotidianos en español.pdf"},
    "15. Medios de Transporte": {"video": "", "pdf": "Minilibros Los medios de transporte en español.pdf"},
    "16. Los Lugares": {"video": "https://www.youtube.com/watch?v=DziT1MJLmk4", "video2": "https://www.youtube.com/watch?v=Ss_2il1-Sm8", "pdf": "Minilibro Los lugares en español.pdf"},
    "17. Animales Domésticos": {"video": "https://www.youtube.com/watch?v=G2n_FA_vhPU", "pdf": "Minilibro Los animales domésticos en español.pdf"},
    "18. Animales Salvajes": {"video": "", "pdf": "Minilibro Los animales salvajes en español.pdf"}
}

# --- 3. ACCESO ---
CONTRASEÑA = "pao_premium"
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("🎓 Academia Pao- Spanish- Teacher")
    clave = st.text_input("Ingresa tu clave:", type="password")
    if st.button("Ingresar"):
        if clave == CONTRASEÑA:
            st.session_state.auth = True
            st.rerun()
        else: st.error("Clave incorrecta")
    st.stop()

# --- 4. NAVEGACIÓN ---
with st.sidebar:
    st.title("Menú")
    menu = st.radio("Secciones:", ["Inicio", "Gramática Española", "Lecciones A1", "Contacto"])
    if st.button("Cerrar Sesión"):
        st.session_state.auth = False
        st.rerun()

# --- 5. LÓGICA DE CONTENIDO ---
if menu == "Inicio":
    st.title("¡Bienvenida a tu Academia! ✨")
    st.write("Explora las secciones para comenzar tu viaje en el español.")

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
    st.title("📚 Temario Nivel A1")
    tema = st.selectbox("Elige un tema:", ["Selecciona..."] + list(DATOS_TEMAS.keys()))
    
    if tema != "Selecciona...":
        d = DATOS_TEMAS[tema]
        t1, t2, t3, t4 = st.tabs(["📺 Clase", "🎧 Dictado", "📖 Cuento", "📄 Material Imprimible"])
        
        with t1:
            if d.get("video"): st.video(d["video"])
            if d.get("video2"): st.divider(); st.video(d["video2"])
            if d.get("video3"): st.divider(); st.video(d["video3"])
        
        with t2:
            st.subheader("🎧 Practica tu oído")
            frases = d.get("frases", [])
            if frases:
                if 'it' not in st.session_state: st.session_state.it = 0
                if st.session_state.it < len(frases):
                    txt = frases[st.session_state.it]
                    if st.button("🔊 Escuchar"):
                        gTTS(text=txt, lang='es').save("s.mp3")
                        st.audio("s.mp3")
                    u = st.text_input("Escribe lo que escuchas:", key=f"d_{tema}_{st.session_state.it}")
                    if st.button("Comprobar"):
                        if u.lower().strip() == txt.lower().strip():
                            st.success("¡Excelente!"); st.session_state.it += 1; st.rerun()
                else:
                    st.success("¡Completado!"); st.button("Reiniciar", on_click=lambda: st.session_state.update({"it":0}))
            else: st.info("Dictado pronto.")

        with t3:
            if d.get("cuento"):
                st.video(d["cuento"])
                if d.get("quiz_cuento"):
                    st.divider()
                    st.write("### ✍️ Ejercicios de Comprensión")
                    r_sel = {}
                    for i in d["quiz_cuento"]["seleccion"]:
                        r_sel[i["p"]] = st.radio(i["p"], i["o"], key=f"sel_{tema}_{i['p']}")
                    r_comp = {}
                    for i in d["quiz_cuento"]["completar"]:
                        r_comp[i["p"]] = st.text_input(i["p"], key=f"comp_{tema}_{i['p']}")
                    if st.button("Verificar"):
                        err = sum(1 for i in d["quiz_cuento"]["seleccion"] if r_sel[i["p"]] != i["r"])
                        err += sum(1 for i in d["quiz_cuento"]["completar"] if r_comp[i["p"]].lower().strip() != i["r"].lower())
                        if err == 0: st.balloons(); st.success("¡Perfecto!")
                        else: st.warning(f"Tienes {err} errores. Revisa el video.")
            else: st.info("Cuento próximamente.")

        with t4:
            st.subheader("📄 Material para Imprimir")
            st.write("Refuerza lo aprendido escribiendo a mano. ¡Descarga tus archivos aquí!")
            c_m, c_f = st.columns(2)
            with c_m:
                st.write("#### 📘 Minilibros")
                if d.get("pdf"):
                    try:
                        with open(d["pdf"], "rb") as f:
                            st.download_button(f"📥 Descargar Minilibro", f, file_name=d["pdf"], key=f"pdf_{tema}")
                    except: st.warning("Archivo PDF no encontrado.")
            with c_f:
                st.write("#### 📝 Fichas")
                st.info("📌 Fichas disponibles pronto.")

elif menu == "Contacto":
    st.title("📩 Contacto")
    st.write("Soporte: pao.mzh16@gmail.com")
