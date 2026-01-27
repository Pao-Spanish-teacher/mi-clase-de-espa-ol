import streamlit as st
from gtts import gTTS
import os

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Pao- Spanish- Teacher", page_icon="🎓", layout="wide")

# --- 2. DICCIONARIO MAESTRO DE DATOS (Videos, Cuentos y Quices) ---
DATOS_TEMAS = {
    "1. Saludos y Despedidas": {
        "video": "https://www.youtube.com/watch?v=hll10VBLFoQ", 
        "cuento": "https://www.youtube.com/watch?v=yhH8rwpEHRo",
        "pdf": "minilibro Saludos.pdf",
        "quiz_cuento": {
            "titulo": "Ejercicios de Comprensión: Saludos y Despedidas (Brisa y Río)",
            "seleccion": [
                {"p": "1. ¿Cómo se llama la niña que está jugando en la arena?", "o": ["María", "Brisa", "Ana"], "r": "Brisa"},
                {"p": "2. ¿Cuál es la primera palabra que usa Río para saludar?", "o": ["Adiós", "Gracias", "Hola"], "r": "Hola"},
                {"p": "3. ¿Qué edad mencionan tener ambos niños?", "o": ["5 años", "7 años", "10 años"], "r": "5 años"},
                {"p": "4. ¿Qué frase de cortesía usan después de presentarse?", "o": ["De nada", "Mucho gusto", "Perdón"], "r": "Mucho gusto"},
                {"p": "5. ¿Qué palabra usan para despedirse al final?", "o": ["Hola", "Adiós", "Por favor"], "r": "Adiós"},
                {"p": "6. ¿Qué estaba construyendo Brisa?", "o": ["Casa de madera", "Castillo de arena", "Túnel de piedra"], "r": "Castillo de arena"},
                {"p": "7. ¿En qué lugar se encuentran los niños?", "o": ["Escuela", "Parque", "Playa"], "r": "Parque"},
                {"p": "8. Respuesta educada a ¿cómo estás?:", "o": ["¡Qué mal!", "Estoy bien, gracias", "No hablar"], "r": "Estoy bien, gracias"},
                {"p": "9. Saludo por la mañana:", "o": ["Buenas noches", "Buenos días", "Hasta luego"], "r": "Buenos días"},
                {"p": "10. ¿Cómo se llama el niño?", "o": ["Mar", "Río", "Lago"], "r": "Río"}
            ],
            "completar": [
                {"p": "11. ¿Cómo __________?", "r": "estás"},
                {"p": "12. ¿Cómo te __________?", "r": "llamas"},
                {"p": "13. Yo vivo en la __________", "r": "ciudad"},
                {"p": "14. __________ favor", "r": "Por"},
                {"p": "15. Hasta __________", "r": "mañana"},
                {"p": "16. La palabra mágica es __________", "r": "Gracias"},
                {"p": "17. Serían muy buenos __________", "r": "amigos"},
                {"p": "18. Buenas __________", "r": "tardes"},
                {"p": "19. Mucho __________", "r": "gusto"},
                {"p": "20. La niña es __________", "r": "Brisa"}
            ]
        }
    },
    "3. Los Colores": {
        "video": "https://www.youtube.com/watch?v=UF5HWnCrAU8",
        "cuento": "https://www.youtube.com/watch?v=BDN7ST1YwcE",
        "pdf": "Minilibro Los colores en español.pdf",
        "quiz_cuento": {
            "titulo": "Ejercicios: Los Colores Primarios, Secundarios y Neutros",
            "seleccion": [
                {"p": "1. ¿Cuáles son los tres colores primarios?", "o": ["Verde, naranja, azul", "Amarillo, azul, rojo", "Blanco, negro, gris"], "r": "Amarillo, azul, rojo"},
                {"p": "2. Azul + Amarillo =", "o": ["Morado", "Verde", "Naranja"], "r": "Verde"},
                {"p": "3. Rojo + Azul =", "o": ["Violeta / Morado", "Verde", "Marrón"], "r": "Violeta / Morado"},
                {"p": "4. Rojo + Amarillo =", "o": ["Rosa", "Naranja", "Celeste"], "r": "Naranja"},
                {"p": "5. Colores neutros:", "o": ["Rojo y Azul", "Blanco y Negro", "Amarillo y Verde"], "r": "Blanco y Negro"}
            ],
            "completar": [
                {"p": "11. Los colores __________ son rojo, azul y amarillo.", "r": "primarios"},
                {"p": "13. El __________ sirve para que los colores sean más claros.", "r": "blanco"},
                {"p": "18. Blanco + Negro =", "r": "gris"}
            ]
        }
    },
    "4. Días, Meses y Estaciones": {
        "video": "https://www.youtube.com/watch?v=T9fvfbMQn2I", 
        "cuento": "https://www.youtube.com/watch?v=h1K6BKCX6g8",
        "pdf": "Minilibro Los días, los meses y las estaciones.pdf",
        "quiz_cuento": {
            "titulo": "Ejercicios de Comprensión: Los Meses del Año",
            "seleccion": [
                {"p": "1. ¿Primer mes del año?", "o": ["Febrero", "Enero", "Marzo"], "r": "Enero"},
                {"p": "2. ¿Mes más corto?", "o": ["Abril", "Febrero", "Junio"], "r": "Febrero"},
                {"p": "3. ¿Cuándo es Navidad?", "o": ["Noviembre", "Octubre", "Diciembre"], "r": "Diciembre"},
                {"p": "4. ¿Qué mes sigue a agosto?", "o": ["Septiembre", "Julio", "Octubre"], "r": "Septiembre"},
                {"p": "10. ¿Último mes del año?", "o": ["Octubre", "Noviembre", "Diciembre"], "r": "Diciembre"}
            ],
            "completar": [
                {"p": "11. Entre marzo y mayo está __________.", "r": "Abril"},
                {"p": "15. Un año tiene __________ meses.", "r": "doce"},
                {"p": "17. El mes número tres es __________.", "r": "Marzo"}
            ]
        }
    },
    "4b. Las Estaciones": {
        "video": "https://www.youtube.com/watch?v=mhI73gkjtwk", 
        "cuento": "https://www.youtube.com/watch?v=nqv12fATbOQ",
        "quiz_cuento": {
            "titulo": "Ejercicios: Las Estaciones del Año",
            "seleccion": [
                {"p": "1. ¿En qué estación brotan las flores?", "o": ["Invierno", "Primavera", "Otoño"], "r": "Primavera"},
                {"p": "2. Estación más calurosa:", "o": ["Verano", "Invierno", "Otoño"], "r": "Verano"},
                {"p": "3. Las hojas caen en:", "o": ["Verano", "Primavera", "Otoño"], "r": "Otoño"},
                {"p": "4. Estación más fría:", "o": ["Invierno", "Primavera", "Verano"], "r": "Invierno"},
                {"p": "5. ¿Cuántas estaciones tiene un año?", "o": ["Dos", "Cuatro", "Seis"], "r": "Cuatro"}
            ],
            "completar": [
                {"p": "11. La __________ es el renacimiento de la naturaleza.", "r": "Primavera"},
                {"p": "14. Guantes y gorros para el __________.", "r": "Invierno"},
                {"p": "18. En el __________ disfrutamos del sol y vacaciones.", "r": "Verano"}
            ]
        }
    },
    "7. Las Profesiones": {
        "video": "https://www.youtube.com/watch?v=szed1no5viA",
        "cuento": "https://www.youtube.com/watch?v=smnwY7G3VUQ",
        "pdf": "Minilibro Las profesiones en español.pdf",
        "quiz_cuento": {
            "titulo": "Ejercicios: Las Profesiones y Oficios",
            "seleccion": [
                {"p": "1. ¿Quién enseña en la escuela?", "o": ["Policía", "Maestra", "Cocinero"], "r": "Maestra"},
                {"p": "2. Apaga incendios con uniforme rojo:", "o": ["Bombero", "Médico", "Piloto"], "r": "Bombero"},
                {"p": "3. Cura a las personas enfermas:", "o": ["Veterinario", "Doctor", "Fotógrafo"], "r": "Doctor"},
                {"p": "4. Cuida a los animales:", "o": ["Doctor", "Veterinario", "Enfermera"], "r": "Veterinario"},
                {"p": "10. Arregla tuberías de agua:", "o": ["Policía", "Fontanero", "Doctor"], "r": "Fontanero"}
            ],
            "completar": [
                {"p": "11. La __________ escribe en la pizarra.", "r": "maestra"},
                {"p": "13. Si tengo fiebre voy al __________.", "r": "doctor"},
                {"p": "20. El __________ arregla el lavabo.", "r": "fontanero"}
            ]
        }
    },
    "10. Partes del Cuerpo": {
        "video": "https://www.youtube.com/watch?v=OfX0hCFCdeA",
        "cuento": "https://www.youtube.com/watch?v=JyedWS0rQ5s",
        "pdf": "Minilibro Las partes del cuerpo en español.pdf",
        "quiz_cuento": {
            "titulo": "Ejercicios: Las Partes del Cuerpo",
            "seleccion": [
                {"p": "1. ¿Con qué vemos los colores?", "o": ["Oídos", "Ojos", "Nariz"], "r": "Ojos"},
                {"p": "2. Parte para caminar y correr:", "o": ["Manos", "Brazos", "Piernas"], "r": "Piernas"},
                {"p": "3. Para escuchar música usamos:", "o": ["Ojos", "Orejas / oídos", "Pies"], "r": "Orejas / oídos"},
                {"p": "4. Para agarrar objetos usamos:", "o": ["Pies", "Manos", "Hombros"], "r": "Manos"},
                {"p": "6. Para oler las flores:", "o": ["Boca", "Nariz", "Cuello"], "r": "Nariz"}
            ],
            "completar": [
                {"p": "12. Usamos la __________ para comer y hablar.", "r": "boca"},
                {"p": "13. La __________ nos permite doblar las piernas.", "r": "rodilla"},
                {"p": "18. Para oler usamos la __________.", "r": "nariz"}
            ]
        }
    },
    "12. Comida y Bebidas": {
        "video": "https://www.youtube.com/watch?v=9iPhcCg64j8",
        "cuento": "https://www.youtube.com/watch?v=SyraFpsEFls",
        "pdf": "Minilibro Comidas y Bebidas en Español..pdf",
        "quiz_cuento": {
            "titulo": "Ejercicios: Los Alimentos de Mateo y Elena",
            "seleccion": [
                {"p": "1. ¿Qué desayuna Mateo?", "o": ["Galletas", "Pan tostado", "Frutas"], "r": "Pan tostado"},
                {"p": "2. Bebida caliente de Mateo:", "o": ["Chocolate", "Té", "Café"], "r": "Café"},
                {"p": "3. Color de la taza de Mateo:", "o": ["Roja", "Blanca", "Azul"], "r": "Azul"},
                {"p": "6. Frutas que come Elena:", "o": ["Pera y uva", "Manzana y banana", "Sandía y melón"], "r": "Manzana y banana"},
                {"p": "9. Alimento que cocina Mateo en la olla:", "o": ["Sopa", "Arroz blanco", "Espaguetis"], "r": "Arroz blanco"}
            ],
            "completar": [
                {"p": "13. La hermana se llama __________.", "r": "Elena"},
                {"p": "18. Mateo usa una __________ grande.", "r": "olla"},
                {"p": "20. El arroz resulta muy __________.", "r": "delicioso"}
            ]
        }
    },
    "13. La Casa": {
        "video": "https://youtu.be/2Wz5yyw80gs",
        "cuento": "https://www.youtube.com/watch?v=yHd_5EQuIN0",
        "pdf": "Minilibro La casa y sus partes en español.pdf",
        "quiz_cuento": {
            "titulo": "Ejercicios: Las Partes de la Casa",
            "seleccion": [
                {"p": "1. ¿De qué color es la casa?", "o": ["Verde", "Amarilla", "Blanca"], "r": "Amarilla"},
                {"p": "2. ¿Cómo es la cocina?", "o": ["Pequeña", "Grande y moderna", "Sucia"], "r": "Grande y moderna"},
                {"p": "3. Material de la mesa:", "o": ["Plástico", "Madera", "Vidrio"], "r": "Madera"},
                {"p": "4. Objeto azul en el dormitorio:", "o": ["Silla", "Cama", "Cortina"], "r": "Cama"},
                {"p": "6. ¿Qué hay en el jardín?", "o": ["Pasto", "Flores y un árbol alto", "Piscina"], "r": "Flores y un árbol alto"}
            ],
            "completar": [
                {"p": "11. La casa es de color __________.", "r": "amarillo"},
                {"p": "15. El baño es de color __________.", "r": "blanco"},
                {"p": "20. El lugar más moderno es la __________.", "r": "cocina"}
            ]
        }
    },
    "15. Medios de Transporte": {
        "video": "https://www.youtube.com/watch?v=9Lv9Ih46MxA",
        "cuento": "https://www.youtube.com/watch?v=9Lv9Ih46MxA", # Es el mismo video
        "pdf": "Minilibros Los medios de transporte en español.pdf",
        "quiz_cuento": {
            "titulo": "Ejercicios: Los Medios de Transporte",
            "seleccion": [
                {"p": "1. Color del carro:", "o": ["Azul", "Rojo", "Blanco"], "r": "Rojo"},
                {"p": "2. Transporte blanco que vuela:", "o": ["Tren", "Avión", "Carro"], "r": "Avión"},
                {"p": "3. Transporte azul de dos ruedas:", "o": ["Carro", "Moto", "Tren"], "r": "Moto"},
                {"p": "4. Color del tren:", "o": ["Blanco", "Gris", "Rojo"], "r": "Gris"},
                {"p": "9. Despega hacia las nubes:", "o": ["Tren", "Avión", "Carro"], "r": "Avión"}
            ],
            "completar": [
                {"p": "11. El __________ rojo va por la calle.", "r": "carro"},
                {"p": "13. El __________ corre sobre rieles.", "r": "tren"},
                {"p": "16. La __________ azul tiene dos ruedas.", "r": "moto"}
            ]
        }
    },
    "17. Animales Domésticos": {
        "video": "https://www.youtube.com/watch?v=G2n_FA_vhPU",
        "cuento": "https://www.youtube.com/watch?v=WsPVCwvWsiw",
        "pdf": "Minilibro Los animales domésticos en español.pdf",
        "quiz_cuento": {
            "titulo": "Ejercicios: Los Animales del Cuento",
            "seleccion": [
                {"p": "1. Dice 'muuu' y da leche:", "o": ["Perro", "Vaca", "Gato"], "r": "Vaca"},
                {"p": "2. Dice 'guau' y es el mejor amigo:", "o": ["Pato", "Perro", "Cerdo"], "r": "Perro"},
                {"p": "3. Hace 'miau' y caza ratones:", "o": ["Conejo", "Gato", "Pollito"], "r": "Gato"},
                {"p": "5. Pequeñito y amarillo (pío pío):", "o": ["Pájaro", "Pollito", "Ratón"], "r": "Pollito"},
                {"p": "10. Rosa, cola rizada y hace 'oink':", "o": ["Hipopótamo", "Cerdo", "Oso"], "r": "Cerdo"}
            ],
            "completar": [
                {"p": "11. Gracias a la __________ comemos queso.", "r": "vaca"},
                {"p": "12. El __________ ladra de alegría.", "r": "perro"},
                {"p": "18. Al __________ le gusta jugar en el lodo.", "r": "cerdo"}
            ]
        }
    },
    "Extra: Rutina de Pedro": {
        "cuento": "https://www.youtube.com/watch?v=2BOKYde4vNM",
        "quiz_cuento": {
            "titulo": "Ejercicios: La Rutina Diaria de Pedro",
            "seleccion": [
                {"p": "1. ¿A qué hora despierta Pedro?", "o": ["7:00", "8:00", "9:00"], "r": "8:00"},
                {"p": "3. ¿Qué bebe Pedro?", "o": ["Jugo", "Café con leche", "Chocolate"], "r": "Café con leche"},
                {"p": "4. ¿A qué hora es su clase?", "o": ["8:30", "9:00", "10:00"], "r": "9:00"},
                {"p": "7. ¿A qué hora regresa a casa?", "o": ["7:00", "8:00", "9:00"], "r": "8:00"},
                {"p": "10. ¿A qué hora se duerme?", "o": ["9:00", "10:00", "11:00"], "r": "10:00"}
            ],
            "completar": [
                {"p": "11. Despierta a las __________.", "r": "8"},
                {"p": "16. A las 5 va al __________.", "r": "parque"},
                {"p": "19. Pedro aprovecha para __________ un libro.", "r": "leer"}
            ]
        }
    }
}

# --- 3. SEGURIDAD ---
CONTRASEÑA = "pao_premium"
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("🎓 Academia Pao- Spanish- Teacher")
    clave = st.text_input("Clave de acceso:", type="password")
    if st.button("Entrar"):
        if clave == CONTRASEÑA:
            st.session_state.auth = True
            st.rerun()
        else: st.error("Clave incorrecta")
    st.stop()

# --- 4. MENÚ LATERAL ---
with st.sidebar:
    st.title("Menú Principal")
    menu = st.radio("Ir a:", ["Inicio", "Gramática Española", "Lecciones A1", "Contacto"])
    if st.button("Salir"):
        st.session_state.auth = False
        st.rerun()

# --- 5. SECCIONES ---
if menu == "Inicio":
    st.title("¡Bienvenida a tu Academia de Español! ✨")
    st.write("Selecciona una lección para comenzar.")

elif menu == "Gramática Española":
    st.title("📖 Gramática Española")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("1. Alfabeto"); st.video("https://www.youtube.com/watch?v=NMgN5gsvhWk")
        st.subheader("3. El Género"); st.video("https://www.youtube.com/watch?v=FSqRurjGIqw")
    with col2:
        st.subheader("2. Preguntas"); st.video("https://www.youtube.com/watch?v=gLnuqh-CUNQ")
        st.subheader("4. Singular/Plural"); st.video("https://www.youtube.com/watch?v=h9pCzNZ1jTI")

elif menu == "Lecciones A1":
    st.title("📚 Temario Nivel A1")
    tema = st.selectbox("Selecciona la lección:", ["Selecciona..."] + list(DATOS_TEMAS.keys()))
    
    if tema != "Selecciona...":
        d = DATOS_TEMAS[tema]
        tab1, tab2, tab3 = st.tabs(["📺 Clase y Cuento", "✍️ Ejercicios", "📄 Material"])
        
        with tab1:
            if d.get("video"):
                st.subheader("Video de la Clase")
                st.video(d["video"])
            if d.get("cuento"):
                st.divider()
                st.subheader("Video del Cuento")
                st.video(d["cuento"])
        
        with tab2:
            if d.get("quiz_cuento"):
                q = d["quiz_cuento"]
                st.header(q["titulo"])
                
                st.subheader("Parte I: Selección Múltiple")
                respuestas_usuario_sel = {}
                for item in q["seleccion"]:
                    respuestas_usuario_sel[item["p"]] = st.radio(item["p"], item["o"], key=f"sel_{tema}_{item['p']}")
                
                st.divider()
                st.subheader("Parte II: Completación")
                respuestas_usuario_comp = {}
                for item in q["completar"]:
                    respuestas_usuario_comp[item["p"]] = st.text_input(item["p"], key=f"comp_{tema}_{item['p']}")
                
                if st.button("Corregir Ejercicios"):
                    errores = 0
                    for item in q["seleccion"]:
                        if respuestas_usuario_sel[item["p"]] != item["r"]: errores += 1
                    for item in q["completar"]:
                        if respuestas_usuario_comp[item["p"]].lower().strip() != item["r"].lower(): errores += 1
                    
                    if errores == 0:
                        st.balloons()
                        st.success("¡Excelente! Todas tus respuestas son correctas.")
                    else:
                        st.warning(f"Tienes {errores} error(es). Revisa el video y vuelve a intentarlo.")
            else:
                st.info("Ejercicios próximamente.")

        with tab3:
            st.subheader("Material para Imprimir")
            if d.get("pdf"):
                try:
                    with open(d["pdf"], "rb") as f:
                        st.download_button(f"📥 Descargar Minilibro ({tema})", f, file_name=d["pdf"])
                except: st.warning("Archivo PDF no encontrado.")
            else: st.info("Material descargable pronto.")

elif menu == "Contacto":
    st.title("📩 Contacto")
    st.write("pao.mzh16@gmail.com")
