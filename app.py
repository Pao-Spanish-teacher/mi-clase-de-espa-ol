
import streamlit as st
from gtts import gTTS
import os

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Pao- Spanish- Teacher", page_icon="🎓", layout="wide")

# --- 2. BASE DE DATOS DE LECCIONES (ESTRUCTURA COMPLETA) ---
# He configurado los temas con los datos que me pasaste. 
# Para los temas restantes (5-18), solo debes rellenar los links siguiendo este mismo formato.
DATOS_TEMAS = {
    "1. Saludos y Despedidas": {
        "clase": ["https://www.youtube.com/watch?v=hll10VBLFoQ", "https://www.youtube.com/watch?v=84FNM-Ni-6U"],
        "dictado": ["Buenos días", "¿Cómo estás?", "Mucho gusto", "Hasta mañana"],
        "cuento_v": "https://www.youtube.com/watch?v=yhH8rwpEHRo",
        "pdf": "minilibro Saludos.pdf",
        "quiz": {
            "sel": [
                {"p": "1. ¿Niña en la arena?", "o": ["María", "Brisa", "Ana"], "r": "Brisa"},
                {"p": "2. ¿Primera palabra de Río?", "o": ["Adiós", "Gracias", "Hola"], "r": "Hola"},
                {"p": "3. ¿Edad de los niños?", "o": ["5 años", "7 años", "10 años"], "r": "5 años"},
                {"p": "4. ¿Frase después de presentarse?", "o": ["De nada", "Mucho gusto", "Perdón"], "r": "Mucho gusto"},
                {"p": "5. ¿Palabra para despedirse?", "o": ["Hola", "Adiós", "Por favor"], "r": "Adiós"},
                {"p": "6. ¿Qué construía Brisa?", "o": ["Casa", "Castillo de arena", "Túnel"], "r": "Castillo de arena"},
                {"p": "7. ¿Lugar del encuentro?", "o": ["Escuela", "Parque", "Playa"], "r": "Parque"},
                {"p": "8. Respuesta a ¿cómo estás?", "o": ["Mal", "Estoy bien, gracias", "Nada"], "r": "Estoy bien, gracias"},
                {"p": "9. Saludo de mañana:", "o": ["Buenas noches", "Buenos días", "Adiós"], "r": "Buenos días"},
                {"p": "10. ¿Nombre del niño?", "o": ["Mar", "Río", "Lago"], "r": "Río"}
            ],
            "comp": [
                {"p": "11. ¿Cómo __________?", "r": "estás"},
                {"p": "12. ¿Cómo te __________?", "r": "llamas"},
                {"p": "13. Vivo en la __________", "r": "ciudad"},
                {"p": "14. __________ favor", "r": "Por"},
                {"p": "15. Hasta __________", "r": "mañana"},
                {"p": "16. Palabra mágica: __________", "r": "Gracias"},
                {"p": "17. Serían buenos __________", "r": "amigos"},
                {"p": "18. Buenas __________", "r": "tardes"},
                {"p": "19. Mucho __________", "r": "gusto"},
                {"p": "20. La niña es __________", "r": "Brisa"}
            ]
        }
    },
    "3. Los Colores": {
        "clase": ["https://www.youtube.com/watch?v=UF5HWnCrAU8"],
        "dictado": ["Rojo", "Verde", "Azul", "Amarillo"],
        "cuento_v": "https://www.youtube.com/watch?v=BDN7ST1YwcE",
        "pdf": "Minilibro Los colores en español.pdf",
        "quiz": {
            "sel": [
                {"p": "1. ¿Colores primarios?", "o": ["Verde, naranja", "Amarillo, azul y rojo", "Blanco, negro"], "r": "Amarillo, azul y rojo"},
                {"p": "2. Azul + Amarillo =", "o": ["Morado", "Verde", "Naranja"], "r": "Verde"},
                {"p": "3. Rojo + Azul =", "o": ["Violeta", "Verde", "Marrón"], "r": "Violeta"},
                {"p": "4. Rojo + Amarillo =", "o": ["Rosa", "Naranja", "Celeste"], "r": "Naranja"},
                {"p": "5. Colores neutros:", "o": ["Rojo/Azul", "Blanco y Negro", "Amarillo/Verde"], "r": "Blanco y Negro"}
            ],
            "comp": [
                {"p": "11. Los colores __________ son rojo, azul y amarillo.", "r": "primarios"},
                {"p": "13. El __________ sirve para dar luz.", "r": "blanco"},
                {"p": "18. Mezcla de blanco y negro: __________", "r": "gris"}
            ]
        }
    },
    "4. Días, Meses y Estaciones": {
        "clase": ["https://www.youtube.com/watch?v=T9fvfbMQn2I"],
        "dictado": ["Enero", "Lunes", "Verano", "Invierno"],
        "cuento_v": "https://www.youtube.com/watch?v=h1K6BKCX6g8",
        "pdf": "Minilibro Los días, los meses y las estaciones.pdf",
        "quiz": {
            "sel": [
                {"p": "1. ¿Primer mes?", "o": ["Febrero", "Enero", "Marzo"], "r": "Enero"},
                {"p": "2. ¿Mes más corto?", "o": ["Abril", "Febrero", "Junio"], "r": "Febrero"},
                {"p": "3. ¿Cuándo es Navidad?", "o": ["Noviembre", "Diciembre", "Octubre"], "r": "Diciembre"},
                {"p": "10. ¿Último mes?", "o": ["Octubre", "Noviembre", "Diciembre"], "r": "Diciembre"}
            ],
            "comp": [
                {"p": "11. Entre marzo y mayo: __________", "r": "Abril"},
                {"p": "15. El año tiene __________ meses", "r": "doce"},
                {"p": "20. Mes número siete: __________", "r": "Julio"}
            ]
        }
    },
    # Agrega aquí los temas del 5 al 18 siguiendo la misma estructura superior
}

# --- 3. SEGURIDAD ---
if "auth" not in st.session_state: st.session_state.auth = False
if not st.session_state.auth:
    st.title("🎓 Academia Pao- Spanish- Teacher")
    clave = st.text_input("Introduce la clave de alumno:", type="password")
    if st.button("Ingresar"):
        if clave == "pao_premium":
            st.session_state.auth = True
            st.rerun()
        else: st.error("Clave incorrecta")
    st.stop()

# --- 4. NAVEGACIÓN LATERAL ---
with st.sidebar:
    st.title("Pao- Spanish 🎓")
    menu = st.radio("Menú Principal:", ["Inicio", "Gramática Española", "Lecciones A1", "Contacto"])
    st.divider()
    if st.button("Cerrar Sesión"):
        st.session_state.auth = False
        st.rerun()

# --- 5. LÓGICA DE SECCIONES ---

if menu == "Inicio":
    st.title("¡Bienvenida a tu Academia de Español! ✨")
    st.write("Hola. Aquí encontrarás todo lo necesario para dominar el nivel A1.")
    st.image("https://images.unsplash.com/photo-1543165365-07232ed12fad?auto=format&fit=crop&q=80&w=1000")

elif menu == "Gramática Española":
    st.title("📖 Gramática Española")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("1. Alfabeto"); st.video("https://www.youtube.com/watch?v=NMgN5gsvhWk")
        st.subheader("3. El Género"); st.video("https://www.youtube.com/watch?v=FSqRurjGIqw")
        st.subheader("5. Número"); st.video("https://www.youtube.com/watch?v=VU5ylA-WjI8")
        st.subheader("7. Artículos"); st.video("https://www.youtube.com/watch?v=rLL0NWpz6IE")
        st.subheader("9. Pronombres"); st.video("https://www.youtube.com/watch?v=LorQtNAKeb4")
        st.subheader("11. Verbos de Movimiento"); st.video("https://www.youtube.com/watch?v=2o4sO1IS3oM")
        st.subheader("13. Tiempos Verbales"); st.video("https://www.youtube.com/watch?v=KA2RryvqfIM")
    with col2:
        st.subheader("2. Preguntas Comunes"); st.video("https://www.youtube.com/watch?v=gLnuqh-CUNQ")
        st.subheader("4. Singular y Plural"); st.video("https://www.youtube.com/watch?v=h9pCzNZ1jTI")
        st.subheader("6. Opuestos I"); st.video("https://youtu.be/fADLwhd43ac")
        st.subheader("8. Opuestos II"); st.video("https://www.youtube.com/watch?v=icJML1BE9qA")
        st.subheader("10. Viajes"); st.video("https://www.youtube.com/watch?v=UI1Bmk3_q08")
        st.subheader("12. Oraciones"); st.video("https://www.youtube.com/watch?v=JKt16i6BwkM")

elif menu == "Lecciones A1":
    st.title("📚 Temario A1")
    tema_sel = st.selectbox("Elige un tema para estudiar:", ["Selecciona..."] + list(DATOS_TEMAS.keys()))
    
    if tema_sel != "Selecciona...":
        d = DATOS_TEMAS[tema_sel]
        tab1, tab2, tab3, tab4 = st.tabs(["📺 Clase", "🎧 Dictado", "📖 Cuento", "📄 Material"])

        with tab1:
            st.subheader("Videos de la Clase")
            for v in d.get("clase", []): st.video(v)
        
        with tab2:
            st.subheader("🎧 Dictado Interactivo")
            frases = d.get("dictado", [])
            if 'idx' not in st.session_state: st.session_state.idx = 0
            if st.session_state.idx < len(frases):
                f_actual = frases[st.session_state.idx]
                if st.button("🔊 Escuchar frase"):
                    gTTS(text=f_actual, lang='es').save("temp.mp3")
                    st.audio("temp.mp3")
                entrada = st.text_input("Escribe lo que escuchaste:", key=f"dict_{tema_sel}_{st.session_state.idx}")
                if st.button("Validar"):
                    if entrada.lower().strip() == f_actual.lower().strip():
                        st.success("¡Excelente!")
                        st.session_state.idx += 1
                        st.rerun()
                    else: st.error("Inténtalo de nuevo.")
            else: 
                st.success("¡Has terminado el dictado!")
                if st.button("Reiniciar Dictado"): 
                    st.session_state.idx = 0
                    st.rerun()

        with tab3:
            st.subheader("📖 El Cuento del Tema")
            st.video(d.get("cuento_v", ""))
            st.divider()
            st.subheader("✍️ Ejercicios de Comprensión")
            q = d.get("quiz", {})
            
            st.write("#### Parte I: Selección Múltiple")
            resp_sel = {}
            for item in q.get("sel", []):
                resp_sel[item["p"]] = st.radio(item["p"], item["o"], key=f"sel_{tema_sel}_{item['p']}")
            
            st.write("#### Parte II: Completación")
            resp_comp = {}
            for item in q.get("comp", []):
                resp_comp[item["p"]] = st.text_input(item["p"], key=f"comp_{tema_sel}_{item['p']}")
            
            if st.button("Corregir Ejercicios"):
                errores = sum(1 for i in q["sel"] if resp_sel[i["p"]] != i["r"])
                errores += sum(1 for i in q["comp"] if resp_comp[i["p"]].lower().strip() != i["r"].lower())
                if errores == 0:
                    st.balloons()
                    st.success("¡Felicidades! Todo está perfecto.")
                else: st.warning(f"Tienes {errores} error(es). Revisa el cuento de nuevo.")

        with tab4:
            st.subheader("📄 Material Descargable")
            st.info("Imprimir y practicar a mano refuerza tu memoria.")
            c1, c2 = st.columns(2)
            with c1:
                st.write("#### 📘 Minilibro")
                if d.get("pdf"):
                    try:
                        with open(d["pdf"], "rb") as f:
                            st.download_button("📥 Descargar PDF", f, file_name=d["pdf"])
                    except: st.error("Archivo PDF no encontrado en el servidor.")
            with c2:
                st.write("#### 📝 Fichas")
                st.info("Próximamente disponibles.")

elif menu == "Contacto":
    st.title("📩 Contacto y Soporte")
    st.write("¿Tienes dudas o necesitas ayuda con tu curso?")
    st.markdown("""
    * **Profesora:** Pao
    * **Email:** pao.mzh16@gmail.com
    * **Horario:** Lunes a Viernes (9:00 - 18:00)
    """)
    st.image("https://images.unsplash.com/photo-1534536281715-e28d76689b4d?auto=format&fit=crop&q=80&w=1000")
