import streamlit as st
from gtts import gTTS
import os

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Pao- Spanish- Teacher", page_icon="🎓", layout="wide")

# --- 2. DICCIONARIO MAESTRO (TODOS LOS TEMAS 1-18) ---
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
                {"p": "1. ¿Cómo se llama la niña?", "o": ["María", "Brisa", "Ana"], "r": "Brisa"},
                {"p": "2. ¿Primer saludo de Río?", "o": ["Adiós", "Gracias", "Hola"], "r": "Hola"},
                {"p": "3. ¿Edad de los niños?", "o": ["5 años", "7 años", "10 años"], "r": "5 años"},
                {"p": "4. ¿Qué dicen al presentarse?", "o": ["De nada", "Mucho gusto", "Perdón"], "r": "Mucho gusto"},
                {"p": "5. ¿Cómo se despiden?", "o": ["Hola", "Adiós", "Por favor"], "r": "Adiós"}
            ],
            "completar": [
                {"p": "11. ¿Cómo __________?", "r": "estás"},
                {"p": "12. ¿Cómo te __________?", "r": "llamas"},
                {"p": "20. La niña es __________ y el niño es Río.", "r": "Brisa"}
            ]
        }
    },
    "2. Los Números (0-100)": {"video": "https://www.youtube.com/watch?v=nxMBJQAE2ZU", "video2": "https://www.youtube.com/watch?v=u_BAr1fjILU", "pdf": "Minilibros Los números en español (0-100).pdf", "frases": ["Diez", "Cincuenta", "Cien"]},
    "3. Los Colores": {"video": "https://www.youtube.com/watch?v=UF5HWnCrAU8", "pdf": "Minilibro Los colores en español.pdf", "frases": ["Rojo", "Verde", "Azul"]},
    "4. Días, Meses y Estaciones": {
        "video": "https://www.youtube.com/watch?v=T9fvfbMQn2I", 
        "cuento": "https://www.youtube.com/watch?v=h1K6BKCX6g8",
        "pdf": "Minilibro Los días, los meses y las estaciones.pdf", 
        "frases": ["Lunes", "Enero", "Verano"],
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. ¿Primer mes del año?", "o": ["Febrero", "Enero", "Marzo"], "r": "Enero"},
                {"p": "2. ¿Mes más corto?", "o": ["Abril", "Febrero", "Junio"], "r": "Febrero"},
                {"p": "3. ¿Cuándo es Navidad?", "o": ["Octubre", "Noviembre", "Diciembre"], "r": "Diciembre"}
            ],
            "completar": [
                {"p": "11. Entre marzo y mayo está __________.", "r": "Abril"},
                {"p": "15. El año tiene __________ meses.", "r": "doce"}
            ]
        }
    },
    "5. La Hora": {"video": "https://youtu.be/CbqNMMNza9w", "video2": "https://www.youtube.com/watch?v=xmeIIuBwxu4", "pdf": "Minilibro La Hora en Español.pdf", "frases": ["Es la una", "Son las tres"]},
    "6. La Familia": {"video": "https://www.youtube.com/watch?v=4C9JiqgMt8o", "pdf": "minilibro La familia en español.pdf", "frases": ["Mi madre", "Mi abuelo"]},
    "7. Las Profesiones": {"video": "https://www.youtube.com/watch?v=szed1no5viA", "pdf": "Minilibro Las profesiones en español.pdf", "frases": ["Bombero", "Doctora"]},
    "8. Profesiones Técnicas": {"video": "https://www.youtube.com/watch?v=jnyMcesUtsI", "pdf": "Minilibro Las profesiones técnicas en español.pdf", "frases": ["Electricista", "Soldador"]},
    "9. Nacionalidad y Países": {"video": "https://www.youtube.com/watch?v=T2HVf4YqHZY", "pdf": "Minilibros Los países y nacionalidades en español.pdf", "frases": ["España", "Japón"]},
    "10. Partes del Cuerpo": {"video": "https://www.youtube.com/watch?v=OfX0hCFCdeA", "pdf": "Minilibro Las partes del cuerpo en español.pdf", "frases": ["La cabeza", "La mano"]},
    "11. La Ropa y Vestimenta": {"video": "https://www.youtube.com/watch?v=nOisiL-Pyak", "pdf": "Minilibro La ropa y la vestimenta en español.pdf", "frases": ["La falda", "El sombrero"]},
    "12. Comida y Bebidas": {"video": "https://www.youtube.com/watch?v=9iPhcCg64j8", "video2": "https://www.youtube.com/watch?v=LgpwYTK9RTc", "pdf": "Minilibro Comidas y Bebidas en Español..pdf", "frases": ["Leche", "Arroz"]},
    "13. La Casa": {"video": "https://youtu.be/2Wz5yyw80gs", "pdf": "Minilibro La casa y sus partes en español.pdf", "frases": ["El baño", "El jardín"]},
    "14. Objetos Cotidianos": {"video": "", "pdf": "Minilibros Los objetos cotidianos en español.pdf", "frases": ["La llave", "El reloj"]},
    "15. Medios de Transporte": {"video": "", "pdf": "Minilibros Los medios de transporte en español.pdf", "frases": ["El avión", "La moto"]},
    "16. Los Lugares": {"video": "https://www.youtube.com/watch?v=DziT1MJLmk4", "video2": "https://www.youtube.com/watch?v=Ss_2il1-Sm8", "pdf": "Minilibro Los lugares en español.pdf", "frases": ["La playa", "El banco"]},
    "17. Animales Domésticos": {"video": "https://www.youtube.com/watch?v=G2n_FA_vhPU", "pdf": "Minilibro Los animales domésticos en español.pdf", "frases": ["El conejo", "El hámster"]},
    "18. Animales Salvajes": {"video": "", "pdf": "Minilibro Los animales salvajes en español.pdf", "frases": ["El tigre", "La cebra"]}
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

# --- 4. BARRA LATERAL ---
with st.sidebar:
    st.title("Pao- Spanish")
    menu = st.radio("Navegación:", ["Inicio", "Gramática Española", "Lecciones A1", "Contacto"])
    if st.button("Cerrar Sesión"):
        st.session_state.auth = False
        st.rerun()

# --- 5. SECCIONES ---

if menu == "Inicio":
    st.title("¡Bienvenida a tu Academia! ✨")
    st.write("Selecciona una sección en el menú lateral para comenzar a aprender.")

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
        tab1, tab2, tab3, tab4 = st.tabs(["📺 Clase", "🎧 Dictado", "📖 Cuento", "📄 Material para Imprimir"])
        
        with tab1:
            if d.get("video"): st.video(d["video"])
            if d.get("video2"): st.divider(); st.video(d["video2"])
            if d.get("video3"): st.divider(); st.video(d["video3"])
        
        with tab2:
            st.subheader("🎧 Dictado Interactivo")
            frases = d.get("frases", [])
            if frases:
                if 'it' not in st.session_state: st.session_state.it = 0
                if st.session_state.it < len(frases):
                    txt = frases[st.session_state.it]
                    st.write(f"Frase {st.session_state.it + 1} de {len(frases)}")
                    if st.button("🔊 Escuchar"):
                        gTTS(text=txt, lang='es').save("s.mp3")
                        st.audio("s.mp3")
                    u_in = st.text_input("Escribe lo que oyes:", key=f"in_{tema}_{st.session_state.it}")
                    if st.button("Comprobar"):
                        if u_in.lower().strip() == txt.lower().strip():
                            st.success("¡Muy bien!"); st.session_state.it += 1; st.rerun()
                else:
                    st.success("¡Terminaste!"); st.button("Reiniciar", on_click=lambda: st.session_state.update({"it":0}))
            else: st.info("Dictado próximamente.")

        with tab3:
            if d.get("cuento"):
                st.video(d["cuento"])
                if d.get("quiz_cuento"):
                    st.divider()
                    st.write("### ✍️ Parte I: Selección")
                    r_sel = {}
                    for i in d["quiz_cuento"]["seleccion"]:
                        r_sel[i["p"]] = st.radio(i["p"], i["o"], key=f"r_{tema}_{i['p']}")
                    st.write("### ✏️ Parte II: Completación")
                    r_comp = {}
                    for i in d["quiz_cuento"]["completar"]:
                        r_comp[i["p"]] = st.text_input(i["p"], key=f"c_{tema}_{i['p']}")
                    if st.button("Verificar Respuestas"):
                        err = 0
                        for i in d["quiz_cuento"]["seleccion"]:
                            if r_sel[i["p"]] != i["r"]: err += 1
                        for i in d["quiz_cuento"]["completar"]:
                            if r_comp[i["p"]].lower().strip() != i["r"].lower(): err += 1
                        if err == 0: st.balloons(); st.success("¡Perfecto!")
                        else: st.warning(f"Tienes {err} errores.")
            else: st.info("Cuento próximamente.")

        with tab4:
            st.subheader("📄 Material para Imprimir")
            st.markdown("Descarga el material para practicar fuera de línea.")
            c_m, c_f = st.columns(2)
            with c_m:
                st.write("#### 📘 Minilibro")
                if d.get("pdf"):
                    try:
                        with open(d["pdf"], "rb") as f:
                            st.download_button(f"📥 Descargar Minilibro", f, file_name=d["pdf"], key=f"dl_{tema}")
                    except: st.warning("PDF no encontrado.")
            with c_f:
                st.write("#### 📝 Fichas")
                st.info("Próximamente.")

elif menu == "Contacto":
    st.title("📩 Contacto")
    st.write("Soporte: pao.mzh16@gmail.com")
