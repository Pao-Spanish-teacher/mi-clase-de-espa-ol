import streamlit as st
from gtts import gTTS
import os

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Pao- Spanish- Teacher", page_icon="🎓", layout="wide")

# --- 2. DICCIONARIO MAESTRO CON LOS 18 TEMAS ---
DATOS_TEMAS = {
    "1. Saludos y Despedidas": {
        "clase": ["https://www.youtube.com/watch?v=hll10VBLFoQ", "https://www.youtube.com/watch?v=84FNM-Ni-6U"],
        "dictado": ["Buenos días", "¿Cómo estás?", "Mucho gusto", "Hasta mañana", "Hola", "Adiós"],
        "cuento_v": "https://www.youtube.com/watch?v=yhH8rwpEHRo",
        "pdf": "minilibro Saludos.pdf",
        "quiz": {
            "sel": [
                {"p": "1. ¿Cómo se llama la niña?", "o": ["María", "Brisa", "Ana"], "r": "Brisa"},
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
                {"p": "11. ¿Cómo __________? (sentimiento)", "r": "estás"},
                {"p": "12. ¿Cómo te __________? (nombre)", "r": "llamas"},
                {"p": "13. Yo vivo en la __________", "r": "ciudad"},
                {"p": "14. __________ favor", "r": "Por"},
                {"p": "15. Hasta __________", "r": "mañana"},
                {"p": "16. Palabra mágica: __________", "r": "Gracias"},
                {"p": "17. Serían muy buenos __________", "r": "amigos"},
                {"p": "18. Buenas __________ (tarde)", "r": "tardes"},
                {"p": "19. Mucho __________", "r": "gusto"},
                {"p": "20. La niña es __________", "r": "Brisa"}
            ]
        }
    },
    "2. El Alfabeto": {
        "clase": ["https://www.youtube.com/watch?v=NMgN5gsvhWk"],
        "dictado": ["Abeja", "Casa", "Elefante"],
        "cuento_v": "", "pdf": "", "quiz": {"sel": [], "comp": []}
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
                {"p": "3. Rojo + Azul =", "o": ["Violeta", "Verde", "Marrón"], "r": "Violeta / Morado"},
                {"p": "5. Colores neutros:", "o": ["Blanco y Negro", "Rojo y Azul"], "r": "Blanco y Negro"}
            ],
            "comp": [
                {"p": "11. Rojo, azul y amarillo son colores __________", "r": "primarios"},
                {"p": "13. Color neutro para dar luz: __________", "r": "blanco"},
                {"p": "18. Blanco + Negro = __________", "r": "gris"}
            ]
        }
    },
    "4. Días, Meses y Estaciones": {
        "clase": ["https://www.youtube.com/watch?v=T9fvfbMQn2I"],
        "dictado": ["Lunes", "Martes", "Enero", "Diciembre"],
        "cuento_v": "https://www.youtube.com/watch?v=h1K6BKCX6g8",
        "pdf": "Minilibro Los días, los meses y las estaciones.pdf",
        "quiz": {
            "sel": [
                {"p": "1. ¿Primer mes?", "o": ["Enero", "Febrero", "Marzo"], "r": "Enero"},
                {"p": "2. ¿Mes más corto?", "o": ["Abril", "Febrero", "Junio"], "r": "Febrero"},
                {"p": "3. ¿Cuándo es Navidad?", "o": ["Noviembre", "Diciembre"], "r": "Diciembre"},
                {"p": "10. ¿Último mes?", "o": ["Noviembre", "Diciembre"], "r": "Diciembre"}
            ],
            "comp": [
                {"p": "11. Entre marzo y mayo está __________", "r": "Abril"},
                {"p": "15. El año tiene __________ meses", "r": "doce"}
            ]
        }
    },
    "5. Las Estaciones": {
        "clase": ["https://www.youtube.com/watch?v=mhI73gkjtwk"],
        "dictado": ["Primavera", "Verano", "Otoño", "Invierno"],
        "cuento_v": "https://www.youtube.com/watch?v=nqv12fATbOQ",
        "quiz": {
            "sel": [
                {"p": "1. ¿Flores brotan?", "o": ["Invierno", "Primavera", "Otoño"], "r": "Primavera"},
                {"p": "2. ¿Estación calurosa?", "o": ["Verano", "Invierno"], "r": "Verano"},
                {"p": "4. ¿Estación fría?", "o": ["Invierno", "Primavera"], "r": "Invierno"}
            ],
            "comp": [
                {"p": "11. Época del renacimiento: __________", "r": "Primavera"},
                {"p": "14. Guantes y gorros para el __________", "r": "Invierno"}
            ]
        }
    },
    "6. La Familia": {"clase": [], "dictado": [], "cuento_v": "", "quiz": {"sel": [], "comp": []}},
    "7. Profesiones y Oficios": {
        "clase": ["https://www.youtube.com/watch?v=szed1no5viA"],
        "dictado": ["Maestra", "Doctor", "Bombero"],
        "cuento_v": "https://www.youtube.com/watch?v=smnwY7G3VUQ",
        "pdf": "Minilibro Las profesiones en español.pdf",
        "quiz": {
            "sel": [
                {"p": "1. ¿Enseña en la escuela?", "o": ["Policía", "Maestra", "Cocinero"], "r": "Maestra"},
                {"p": "2. Apaga incendios:", "o": ["Bombero", "Médico"], "r": "Bombero"},
                {"p": "10. Arregla tuberías:", "o": ["Policía", "Fontanero"], "r": "Fontanero"}
            ],
            "comp": [
                {"p": "11. Escribe en la pizarra la __________", "r": "maestra"},
                {"p": "13. Si tengo fiebre voy al __________", "r": "doctor"}
            ]
        }
    },
    "8. Los Números": {"clase": [], "dictado": [], "cuento_v": "", "quiz": {"sel": [], "comp": []}},
    "9. Las Prendas de Vestir": {"clase": [], "dictado": [], "cuento_v": "", "quiz": {"sel": [], "comp": []}},
    "10. Partes del Cuerpo": {
        "clase": ["https://www.youtube.com/watch?v=OfX0hCFCdeA"],
        "dictado": ["Ojos", "Boca", "Piernas", "Manos"],
        "cuento_v": "https://www.youtube.com/watch?v=JyedWS0rQ5s",
        "pdf": "Minilibro Las partes del cuerpo en español.pdf",
        "quiz": {
            "sel": [
                {"p": "1. ¿Para ver?", "o": ["Oídos", "Ojos", "Nariz"], "r": "Ojos"},
                {"p": "2. ¿Para correr?", "o": ["Manos", "Piernas"], "r": "Piernas"},
                {"p": "5. ¿Cerebro?", "o": ["Cabeza", "Estómago"], "r": "Cabeza"}
            ],
            "comp": [
                {"p": "12. __________ para comer y hablar", "r": "boca"},
                {"p": "18. Para oler usamos la __________", "r": "nariz"}
            ]
        }
    },
    "11. Los Animales": {
        "clase": ["https://www.youtube.com/watch?v=G2n_FA_vhPU"],
        "dictado": ["Vaca", "Perro", "Gato", "Pato"],
        "cuento_v": "https://www.youtube.com/watch?v=WsPVCwvWsiw",
        "pdf": "Minilibro Los animales domésticos en español.pdf",
        "quiz": {
            "sel": [
                {"p": "1. Dice 'muuu':", "o": ["Perro", "Vaca", "Gato"], "r": "Vaca"},
                {"p": "2. Dice 'guau':", "o": ["Pato", "Perro"], "r": "Perro"},
                {"p": "3. Hace 'miau':", "o": ["Conejo", "Gato"], "r": "Gato"}
            ],
            "comp": [
                {"p": "11. Tomamos leche de la __________", "r": "vaca"},
                {"p": "12. El __________ ladra de alegría", "r": "perro"}
            ]
        }
    },
    "12. Alimentos y Bebidas": {
        "clase": ["https://www.youtube.com/watch?v=9iPhcCg64j8"],
        "dictado": ["Manzana", "Leche", "Café", "Arroz"],
        "cuento_v": "https://www.youtube.com/watch?v=SyraFpsEFls",
        "pdf": "Minilibro Comidas y Bebidas en Español..pdf",
        "quiz": {
            "sel": [
                {"p": "1. Mateo desayuna:", "o": ["Galletas", "Pan tostado"], "r": "Pan tostado"},
                {"p": "3. Taza de Mateo:", "o": ["Roja", "Azul"], "r": "Azul"},
                {"p": "6. Frutas de Elena:", "o": ["Manzana y banana", "Pera"], "r": "Manzana y banana"}
            ],
            "comp": [
                {"p": "13. Hermana de Mateo: __________", "r": "Elena"},
                {"p": "19. Arroz de color __________", "r": "blanco"}
            ]
        }
    },
    "13. La Casa": {
        "clase": ["https://youtu.be/2Wz5yyw80gs"],
        "dictado": ["Cocina", "Baño", "Jardín", "Cama"],
        "cuento_v": "https://www.youtube.com/watch?v=yHd_5EQuIN0",
        "pdf": "Minilibro La casa y sus partes en español.pdf",
        "quiz": {
            "sel": [
                {"p": "1. Color de la casa:", "o": ["Verde", "Amarilla", "Blanca"], "r": "Amarilla"},
                {"p": "3. Mesa de:", "o": ["Plástico", "Madera"], "r": "Madera"},
                {"p": "4. Cama de color:", "o": ["Rojo", "Azul"], "r": "Azul"}
            ],
            "comp": [
                {"p": "11. Resalta por ser de color __________", "r": "amarillo"},
                {"p": "15. El baño es de color __________", "r": "blanco"}
            ]
        }
    },
    "14. Las Frutas y Verduras": {"clase": [], "dictado": [], "cuento_v": "", "quiz": {"sel": [], "comp": []}},
    "15. Medios de Transporte": {
        "clase": ["https://www.youtube.com/watch?v=9Lv9Ih46MxA"],
        "dictado": ["Carro", "Tren", "Avión", "Moto"],
        "cuento_v": "https://www.youtube.com/watch?v=9Lv9Ih46MxA",
        "pdf": "Minilibros Los medios de transporte en español.pdf",
        "quiz": {
            "sel": [
                {"p": "1. Color del carro:", "o": ["Azul", "Rojo", "Blanco"], "r": "Rojo"},
                {"p": "2. Vuela por el cielo:", "o": ["Tren", "Avión"], "r": "Avión"},
                {"p": "3. Dos ruedas azul:", "o": ["Carro", "Moto"], "r": "Moto"}
            ],
            "comp": [
                {"p": "11. El __________ rojo va por la calle", "r": "carro"},
                {"p": "13. El __________ corre sobre rieles", "r": "tren"}
            ]
        }
    },
    "16. Lugares de la Ciudad": {"clase": [], "dictado": [], "cuento_v": "", "quiz": {"sel": [], "comp": []}},
    "17. La Rutina Diaria": {
        "clase": [],
        "dictado": ["Despertarse", "Almorzar", "Dormir"],
        "cuento_v": "https://www.youtube.com/watch?v=2BOKYde4vNM",
        "quiz": {
            "sel": [
                {"p": "1. Despierta a las:", "o": ["7:00", "8:00", "9:00"], "r": "8:00"},
                {"p": "4. Clase a las:", "o": ["8:30", "9:00"], "r": "9:00"},
                {"p": "10. Duerme a las:", "o": ["10:00", "11:00"], "r": "10:00"}
            ],
            "comp": [
                {"p": "11. Despierta a las __________ de la mañana", "r": "8"},
                {"p": "16. A las 5 va al __________", "r": "parque"}
            ]
        }
    },
    "18. Los Verbos Ser y Estar": {"clase": [], "dictado": [], "cuento_v": "", "quiz": {"sel": [], "comp": []}}
}

# --- 3. SEGURIDAD ---
if "auth" not in st.session_state: st.session_state.auth = False
if not st.session_state.auth:
    st.title("🎓 Academia Pao- Spanish- Teacher")
    clave = st.text_input("Clave:", type="password")
    if st.button("Entrar") and clave == "pao_premium":
        st.session_state.auth = True
        st.rerun()
    st.stop()

# --- 4. MENÚ ---
with st.sidebar:
    st.title("Pao- Spanish")
    menu = st.radio("Secciones:", ["Inicio", "Gramática Española", "Lecciones A1", "Contacto"])
    st.divider()
    if st.button("Salir"): st.session_state.auth = False; st.rerun()

# --- 5. SECCIONES ---
if menu == "Inicio":
    st.title("¡Bienvenida a tu Academia! ✨")
    st.image("https://images.unsplash.com/photo-1543165365-07232ed12fad?auto=format&fit=crop&q=80&w=1000")

elif menu == "Gramática Española":
    st.title("📖 Gramática Española")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("1. Alfabeto"); st.video("https://www.youtube.com/watch?v=NMgN5gsvhWk")
        st.subheader("3. Género"); st.video("https://www.youtube.com/watch?v=FSqRurjGIqw")
        st.subheader("5. Número"); st.video("https://www.youtube.com/watch?v=VU5ylA-WjI8")
        st.subheader("7. Artículos"); st.video("https://www.youtube.com/watch?v=rLL0NWpz6IE")
        st.subheader("9. Pronombres"); st.video("https://www.youtube.com/watch?v=LorQtNAKeb4")
        st.subheader("11. Movimiento"); st.video("https://www.youtube.com/watch?v=2o4sO1IS3oM")
    with c2:
        st.subheader("2. Preguntas"); st.video("https://www.youtube.com/watch?v=gLnuqh-CUNQ")
        st.subheader("4. Singular/Plural"); st.video("https://www.youtube.com/watch?v=h9pCzNZ1jTI")
        st.subheader("6. Opuestos"); st.video("https://youtu.be/fADLwhd43ac")
        st.subheader("8. Opuestos II"); st.video("https://www.youtube.com/watch?v=icJML1BE9qA")
        st.subheader("10. Viajes"); st.video("https://www.youtube.com/watch?v=UI1Bmk3_q08")
        st.subheader("12. Oraciones"); st.video("https://www.youtube.com/watch?v=JKt16i6BwkM")

elif menu == "Lecciones A1":
    tema = st.selectbox("Elige el tema:", ["Selecciona..."] + list(DATOS_TEMAS.keys()))
    if tema != "Selecciona...":
        d = DATOS_TEMAS[tema]
        tab1, tab2, tab3, tab4 = st.tabs(["📺 Clase", "🎧 Dictado", "📖 Cuento", "📄 Material"])

        with tab1:
            if d["clase"]:
                for v in d["clase"]: st.video(v)
            else: st.info("Clase en producción.")

        with tab2:
            st.subheader("🎧 Dictado")
            if d["dictado"]:
                if 'idx' not in st.session_state: st.session_state.idx = 0
                f = d["dictado"][st.session_state.idx]
                if st.button("🔊 Oír"):
                    gTTS(text=f, lang='es').save("s.mp3")
                    st.audio("s.mp3")
                res = st.text_input("Escribe:", key=f"d_{st.session_state.idx}")
                if st.button("Validar") and res.lower().strip() == f.lower().strip():
                    st.success("¡Bien!"); st.session_state.idx = (st.session_state.idx + 1) % len(d["dictado"])
                    st.rerun()
            else: st.info("No hay dictado para este tema.")

        with tab3:
            if d["cuento_v"]:
                st.video(d["cuento_v"])
                st.subheader("✍️ Ejercicios")
                q = d["quiz"]
                user_sel = {i["p"]: st.radio(i["p"], i["o"], key=f"s_{i['p']}") for i in q["sel"]}
                user_comp = {i["p"]: st.text_input(i["p"], key=f"c_{i['p']}") for i in q["comp"]}
                if st.button("Corregir"):
                    st.balloons(); st.success("¡Completado!")
            else: st.info("Cuento no disponible.")

        with tab4:
            st.subheader("📄 Material")
            if d["pdf"]:
                with open(d["pdf"], "rb") as f:
                    st.download_button("📥 Descargar Minilibro", f, file_name=d["pdf"])
            else: st.info("Sin archivos.")

elif menu == "Contacto":
    st.title("📩 Contacto")
    st.write("Profesora Pao: pao.mzh16@gmail.com")
