import streamlit as st
from gtts import gTTS
import os

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Pao- Spanish- Teacher", page_icon="🎓", layout="wide")

# --- 2. DICCIONARIO MAESTRO (Estructura Completa) ---
DATOS_TEMAS = {
    "1. Saludos y Despedidas": {
        "videos_clase": ["https://www.youtube.com/watch?v=hll10VBLFoQ", "https://www.youtube.com/watch?v=84FNM-Ni-6U", "https://www.youtube.com/watch?v=4txmiiR10wM"],
        "frases_dictado": ["Buenos días", "¿Cómo estás?", "Mucho gusto", "Hasta mañana"],
        "video_cuento": "https://www.youtube.com/watch?v=yhH8rwpEHRo",
        "quiz_cuento": {
            "titulo": "Ejercicios de Comprensión: Saludos y Despedidas (Brisa y Río)",
            "seleccion": [
                {"p": "1. ¿Cómo se llama la niña que juega en la arena?", "o": ["María", "Brisa", "Ana"], "r": "Brisa"},
                {"p": "2. ¿Primera palabra que usa Río?", "o": ["Adiós", "Gracias", "Hola"], "r": "Hola"},
                {"p": "3. ¿Qué edad mencionan tener?", "o": ["5 años", "7 años", "10 años"], "r": "5 años"},
                {"p": "4. ¿Frase después de presentarse?", "o": ["De nada", "Mucho gusto", "Perdón"], "r": "Mucho gusto"},
                {"p": "5. ¿Palabra para despedirse?", "o": ["Hola", "Adiós", "Por favor"], "r": "Adiós"},
                {"p": "6. ¿Qué construía Brisa?", "o": ["Casa", "Castillo de arena", "Túnel"], "r": "Castillo de arena"},
                {"p": "7. ¿Lugar del encuentro?", "o": ["Escuela", "Parque", "Playa"], "r": "Parque"},
                {"p": "8. Respuesta a ¿cómo estás?", "o": ["¡Qué mal!", "Estoy bien, gracias", "No hablar"], "r": "Estoy bien, gracias"},
                {"p": "9. Saludo de mañana:", "o": ["Buenas noches", "Buenos días", "Hasta luego"], "r": "Buenos días"},
                {"p": "10. ¿Cómo se llama el niño?", "o": ["Mar", "Río", "Lago"], "r": "Río"}
            ],
            "completar": [
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
        },
        "pdf_mini": "minilibro Saludos.pdf"
    },
    "3. Los Colores": {
        "videos_clase": ["https://www.youtube.com/watch?v=UF5HWnCrAU8"],
        "frases_dictado": ["Rojo", "Verde", "Azul", "Amarillo"],
        "video_cuento": "https://www.youtube.com/watch?v=BDN7ST1YwcE",
        "quiz_cuento": {
            "titulo": "Los Colores Primarios, Secundarios y Neutros",
            "seleccion": [
                {"p": "1. Colores primarios:", "o": ["Verde, naranja", "Amarillo, azul y rojo", "Blanco, negro"], "r": "Amarillo, azul y rojo"},
                {"p": "2. Azul + Amarillo =", "o": ["Morado", "Verde", "Naranja"], "r": "Verde"},
                {"p": "3. Rojo + Azul =", "o": ["Violeta", "Verde", "Marrón"], "r": "Violeta"},
                {"p": "4. Rojo + Amarillo =", "o": ["Rosa", "Naranja", "Celeste"], "r": "Naranja"},
                {"p": "5. Colores neutros:", "o": ["Rojo/Azul", "Blanco y Negro", "Amarillo/Verde"], "r": "Blanco y Negro"}
            ],
            "completar": [
                {"p": "11. Colores puros: __________", "r": "primarios"},
                {"p": "13. Da luz a los colores: El __________", "r": "blanco"},
                {"p": "18. Blanco + Negro = __________", "r": "gris"}
            ]
        },
        "pdf_mini": "Minilibro Los colores en español.pdf"
    }
    # (Aquí se agregarían los otros 16 temas con la misma estructura)
}

# --- 3. LÓGICA DE ACCESO ---
if "auth" not in st.session_state: st.session_state.auth = False
if not st.session_state.auth:
    st.title("🎓 Academia Pao- Spanish- Teacher")
    if st.text_input("Clave:", type="password") == "pao_premium":
        if st.button("Entrar"):
            st.session_state.auth = True
            st.rerun()
    st.stop()

# --- 4. MENÚ ---
with st.sidebar:
    st.title("Navegación")
    menu = st.radio("Secciones:", ["Inicio", "Gramática Española", "Lecciones A1", "Contacto"])

# --- 5. SECCIONES ---
if menu == "Gramática Española":
    st.title("📖 Gramática Española")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("1. El Alfabeto"); st.video("https://www.youtube.com/watch?v=NMgN5gsvhWk")
        st.subheader("3. El Género"); st.video("https://www.youtube.com/watch?v=FSqRurjGIqw")
    with c2:
        st.subheader("2. Preguntas Comunes"); st.video("https://www.youtube.com/watch?v=gLnuqh-CUNQ")
        st.subheader("4. Singular y Plural"); st.video("https://www.youtube.com/watch?v=h9pCzNZ1jTI")

elif menu == "Lecciones A1":
    tema_sel = st.selectbox("Selecciona un tema:", ["Selecciona..."] + list(DATOS_TEMAS.keys()))
    
    if tema_sel != "Selecciona...":
        d = DATOS_TEMAS[tema_sel]
        t1, t2, t3, t4 = st.tabs(["📺 Clase", "🎧 Dictado", "📖 Cuento", "📄 Material"])

        with t1:
            for v in d.get("videos_clase", []):
                st.video(v)
        
        with t2:
            st.subheader("🎧 Dictado Interactivo")
            frases = d.get("frases_dictado", [])
            if 'idx' not in st.session_state: st.session_state.idx = 0
            if st.session_state.idx < len(frases):
                f_actual = frases[st.session_state.idx]
                if st.button("🔊 Escuchar"):
                    gTTS(text=f_actual, lang='es').save("s.mp3")
                    st.audio("s.mp3")
                resp = st.text_input("Escribe lo que oyes:", key=f"dic_{st.session_state.idx}")
                if st.button("Check"):
                    if resp.lower().strip() == f_actual.lower().strip():
                        st.success("¡Bien!"); st.session_state.idx += 1; st.rerun()
            else: st.success("¡Dictado completado!"); st.button("Reiniciar", on_click=lambda: st.session_state.update({"idx":0}))

        with t3:
            st.video(d.get("video_cuento", ""))
            q = d.get("quiz_cuento", {})
            st.subheader(q.get("titulo", "Ejercicios"))
            
            # Selección
            res_s = {i["p"]: st.radio(i["p"], i["o"], key=f"s_{i['p']}") for i in q.get("seleccion", [])}
            # Completación
            res_c = {i["p"]: st.text_input(i["p"], key=f"c_{i['p']}") for i in q.get("completar", [])}
            
            if st.button("Corregir Cuento"):
                err = sum(1 for i in q["seleccion"] if res_s[i["p"]] != i["r"])
                err += sum(1 for i in q["completar"] if res_c[i["p"]].lower().strip() != i["r"].lower())
                if err == 0: st.balloons(); st.success("¡Perfecto!")
                else: st.error(f"Tienes {err} errores.")

        with t4:
            st.subheader("📄 Material para Imprimir")
            st.write("Imprimir y escribir a mano te ayudará a memorizar mejor.")
            col_a, col_b = st.columns(2)
            with col_a:
                st.write("#### 📘 Minilibro")
                if d.get("pdf_mini"):
                    with open(d["pdf_mini"], "rb") as f:
                        st.download_button("📥 Descargar Minilibro", f, file_name=d["pdf_mini"])
            with col_b:
                st.write("#### 📝 Fichas")
                st.info("Próximamente")
