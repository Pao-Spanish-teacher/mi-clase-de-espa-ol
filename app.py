import streamlit as st
from gtts import gTTS
import os

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Pao- Spanish- Teacher", page_icon="🎓", layout="wide")

# --- 2. DICCIONARIO MAESTRO (16 TEMAS) ---
DATOS_TEMAS = {
    "1. Saludos y Despedidas": {
        "video": "https://www.youtube.com/watch?v=hll10VBLFoQ", 
        "video2": "https://www.youtube.com/watch?v=84FNM-Ni-6U", 
        "video3": "https://www.youtube.com/watch?v=4txmiiR10wM",
        "cuento": "https://youtube.com/shorts/yhH8rwpEHRo",
        "pdf": "minilibro Saludos.pdf", 
        "frases": ["Buenos días", "¿Cómo estás?", "Mucho gusto", "Hasta mañana"],
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. ¿Cómo se llama la niña?", "o": ["María", "Brisa", "Ana"], "r": "Brisa"},
                {"p": "2. ¿Primera palabra de Río?", "o": ["Adiós", "Gracias", "Hola"], "r": "Hola"},
                {"p": "3. ¿Qué edad tienen?", "o": ["5 años", "7 años", "10 años"], "r": "5 años"},
                {"p": "4. Frase tras presentarse:", "o": ["De nada", "Mucho gusto", "Perdón"], "r": "Mucho gusto"},
                {"p": "5. ¿Qué palabra usan para despedirse?", "o": ["Hola", "Adiós", "Por favor"], "r": "Adiós"},
                {"p": "6. ¿Qué construía Brisa?", "o": ["Casa", "Castillo de arena", "Túnel"], "r": "Castillo de arena"},
                {"p": "7. ¿Dónde están?", "o": ["Escuela", "Parque", "Playa"], "r": "Parque"},
                {"p": "8. Respuesta a ¿Cómo estás?", "o": ["¡Qué mal!", "Estoy bien, gracias", "No hablo"], "r": "Estoy bien, gracias"},
                {"p": "9. Saludo de mañana:", "o": ["Buenas noches", "Buenos días", "Hasta luego"], "r": "Buenos días"},
                {"p": "10. Nombre del niño:", "o": ["Mar", "Río", "Lago"], "r": "Río"}
            ],
            "completar": [
                {"p": "11. ¿Cómo __________?", "r": "estás"},
                {"p": "12. ¿Cómo te __________?", "r": "llamas"},
                {"p": "13. Vivo en la __________", "r": "ciudad"},
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
    "2. Los Números (0-100)": {"video": "https://www.youtube.com/watch?v=nxMBJQAE2ZU", "pdf": "Minilibros Números.pdf", "frases": ["Diez", "Cincuenta", "Cien"]},
    "3. Los Colores": {
        "video": "https://www.youtube.com/watch?v=UF5HWnCrAU8", 
        "cuento": "https://youtube.com/shorts/BDN7ST1YwcE",
        "pdf": "Minilibro Colores.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. Colores primarios:", "o": ["Verde, naranja y violeta", "Amarillo, azul y rojo", "Blanco, negro y gris"], "r": "Amarillo, azul y rojo"},
                {"p": "2. Azul + Amarillo:", "o": ["Morado", "Verde", "Naranja"], "r": "Verde"},
                {"p": "3. Rojo + Azul:", "o": ["Violeta / Morado", "Verde", "Marrón"], "r": "Violeta / Morado"},
                {"p": "5. Colores neutros:", "o": ["Rojo y Azul", "Blanco y Negro", "Amarillo y Verde"], "r": "Blanco y Negro"}
            ],
            "completar": [
                {"p": "11. Rojo, azul y amarillo son: __________", "r": "primarios"},
                {"p": "13. Para aclarar usamos el: __________", "r": "blanco"},
                {"p": "18. Mezcla de blanco y negro: __________", "r": "gris"}
            ]
        }
    },
    "4. Días, Meses y Estaciones": {
        "video": "https://www.youtube.com/watch?v=T9fvfbMQn2I", 
        "cuento": "https://youtube.com/shorts/h1K6BKCX6g8",
        "cuento2": "https://youtube.com/shorts/nqv12fATbOQ",
        "pdf": "Minilibro Meses Estaciones.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. Primer mes:", "o": ["Febrero", "Enero", "Marzo"], "r": "Enero"},
                {"p": "2. Mes más corto:", "o": ["Abril", "Febrero", "Junio"], "r": "Febrero"},
                {"p": "1. ¿En qué estación brotan flores?", "o": ["Invierno", "Primavera", "Otoño"], "r": "Primavera"},
                {"p": "2. Estación más calurosa:", "o": ["Verano", "Invierno", "Otoño"], "r": "Verano"}
            ],
            "completar": [
                {"p": "11. Mes entre marzo y mayo: __________", "r": "Abril"},
                {"p": "15. El año tiene __________ meses.", "r": "doce"},
                {"p": "11. Estación del 'renacimiento': __________", "r": "Primavera"}
            ]
        }
    },
    "5. La Hora y Rutina Diaria": {
        "video": "https://youtu.be/CbqNMMNza9w", 
        "cuento": "https://youtube.com/shorts/2BOKYde4vNM", 
        "pdf": "Minilibro La Hora.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. ¿A qué hora despierta Pedro?", "o": ["7:00", "8:00", "9:00"], "r": "8:00"},
                {"p": "4. ¿Hora de clase?", "o": ["8:30", "9:00", "10:00"], "r": "9:00"},
                {"p": "8. ¿Qué cena Pedro?", "o": ["Pizza", "Ensalada y pescado", "Arroz con pollo"], "r": "Ensalada y pescado"}
            ],
            "completar": [
                {"p": "11. Se despierta a las __________", "r": "ocho"},
                {"p": "12. Pan con __________", "r": "mantequilla"},
                {"p": "19. Antes de dormir le gusta __________", "r": "leer"}
            ]
        }
    },
    "6. La Familia": {"video": "https://www.youtube.com/watch?v=4C9JiqgMt8o", "pdf": "minilibro Familia.pdf"},
    "7. Profesiones (Generales y Técnicas)": {
        "video": "https://www.youtube.com/watch?v=szed1no5viA", 
        "cuento": "https://youtube.com/shorts/smnwY7G3VUQ",
        "pdf": "Minilibro Profesiones.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. ¿Quién enseña?", "o": ["Policía", "Maestra", "Cocinero"], "r": "Maestra"},
                {"p": "2. Uniforme rojo y apaga incendios:", "o": ["Bombero", "Médico", "Piloto"], "r": "Bombero"},
                {"p": "10. ¿Quién arregla tuberías?", "o": ["Policía", "Fontanero", "Doctor"], "r": "Fontanero"}
            ],
            "completar": [
                {"p": "11. La __________ escribe en la pizarra.", "r": "maestra"},
                {"p": "13. Si tengo fiebre voy al __________", "r": "doctor"}
            ]
        }
    },
    "8. Nacionalidad y Países": {"video": "https://www.youtube.com/watch?v=T2HVf4YqHZY", "pdf": "Minilibros Países.pdf"},
    "9. Partes del Cuerpo": {
        "video": "https://www.youtube.com/watch?v=OfX0hCFCdeA", 
        "cuento": "https://youtube.com/shorts/JyedWS0rQ5s",
        "pdf": "Minilibro Cuerpo.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. Para ver colores usamos:", "o": ["Oídos", "Ojos", "Nariz"], "r": "Ojos"},
                {"p": "2. Para caminar:", "o": ["Manos", "Brazos", "Piernas"], "r": "Piernas"},
                {"p": "5. ¿Dónde está el cerebro?", "o": ["Pecho", "Cabeza", "Estómago"], "r": "Cabeza"}
            ],
            "completar": [
                {"p": "12. Usamos la __________ para comer.", "r": "boca"},
                {"p": "18. Usamos la __________ para oler.", "r": "nariz"},
                {"p": "19. El tacto está en la __________", "r": "piel"}
            ]
        }
    },
    "10. La Ropa y Vestimenta": {"video": "https://www.youtube.com/watch?v=nOisiL-Pyak", "pdf": "Minilibro Ropa.pdf"},
    "11. Comida y Bebidas": {
        "video": "https://www.youtube.com/watch?v=9iPhcCg64j8", 
        "cuento": "https://youtube.com/shorts/SyraFpsEFls",
        "pdf": "Minilibro Comida.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. ¿Qué desayuna Mateo?", "o": ["Galletas", "Pan tostado", "Frutas"], "r": "Pan tostado"},
                {"p": "6. Frutas de Elena:", "o": ["Pera y uva", "Manzana y banana", "Sandía"], "r": "Manzana y banana"}
            ],
            "completar": [
                {"p": "12. El café está muy __________", "r": "caliente"},
                {"p": "19. El arroz es de color __________", "r": "blanco"}
            ]
        }
    },
    "12. La Casa": {
        "video": "https://youtu.be/2Wz5yyw80gs", 
        "cuento": "https://youtube.com/shorts/yHd_5EQuIN0",
        "pdf": "Minilibro Casa.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. Color de la casa:", "o": ["Verde", "Amarilla", "Blanca"], "r": "Amarilla"},
                {"p": "4. Objeto azul en dormitorio:", "o": ["Silla", "Cama", "Cortina"], "r": "Cama"}
            ],
            "completar": [
                {"p": "11. Resalta por ser de color __________", "r": "amarillo"},
                {"p": "13. Mesa fabricada de __________", "r": "madera"}
            ]
        }
    },
    "13. Objetos Cotidianos": {"video": "", "pdf": "Minilibros Objetos.pdf"},
    "14. Medios de Transporte": {
        "video": "", 
        "cuento": "https://youtube.com/shorts/9Lv9Ih46MxA",
        "pdf": "Minilibros Transporte.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. Color del carro:", "o": ["Azul", "Rojo", "Blanco"], "r": "Rojo"},
                {"p": "2. Transporte blanco que vuela:", "o": ["Tren", "Avión", "Carro"], "r": "Avión"}
            ],
            "completar": [
                {"p": "12. La moto es de color __________", "r": "azul"},
                {"p": "13. El __________ es gris y va en rieles", "r": "tren"}
            ]
        }
    },
    "15. Los Lugares de la Ciudad": {"video": "https://www.youtube.com/watch?v=DziT1MJLmk4", "pdf": "Minilibro Lugares.pdf"},
    "16. Los Animales (Domésticos y Salvajes)": {
        "video": "https://www.youtube.com/watch?v=G2n_FA_vhPU", 
        "cuento": "https://youtube.com/shorts/WsPVCwvWsiw",
        "pdf": "Minilibro Animales.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. Dice 'Muuu':", "o": ["Perro", "Vaca", "Gato"], "r": "Vaca"},
                {"p": "2. Dice 'Guau':", "o": ["Pato", "Perro", "Cerdo"], "r": "Perro"},
                {"p": "10. Rosa, cola rizada y hace 'Oink':", "o": ["Hipopótamo", "Cerdo", "Oso"], "r": "Cerdo"}
            ],
            "completar": [
                {"p": "12. El __________ mueve la cola.", "r": "perro"},
                {"p": "13. El __________ ronronea.", "r": "gato"},
                {"p": "20. Nace de un huevo: __________", "r": "pollito"}
            ]
        }
    }
}

# --- 3. ACCESO ---
if "auth" not in st.session_state: st.session_state.auth = False
if not st.session_state.auth:
    st.title("🎓 Academia Pao- Spanish- Teacher")
    clave = st.text_input("Ingresa tu clave:", type="password")
    if st.button("Ingresar"):
        if clave == "pao_premium":
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

# --- 5. CONTENIDO ---
if menu == "Inicio":
    st.title("¡Bienvenida a tu Academia! ✨")
    st.write("Explora las secciones para comenzar tu aprendizaje.")

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
        t1, t2, t3, t4 = st.tabs(["📺 Clase", "🎧 Dictado", "📖 Cuento", "📄 Material"])
        
        with t1:
            if d.get("video"): st.video(d["video"])
            if d.get("video2"): st.divider(); st.video(d["video2"])
        
        with t2:
            st.subheader("🎧 Practica tu oído")
            frases = d.get("frases", ["Hola", "Gracias"])
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

        with t3:
            if d.get("cuento"):
                st.video(d["cuento"])
                if d.get("cuento2"): st.divider(); st.video(d["cuento2"])
                
                if d.get("quiz_cuento"):
                    st.divider(); st.write("### ✍️ Ejercicios de Comprensión")
                    
                    # SELECCIÓN SIN OPCIÓN POR DEFECTO
                    r_sel = {}
                    for i in d["quiz_cuento"]["seleccion"]:
                        r_sel[i["p"]] = st.radio(i["p"], i["o"], index=None, key=f"sel_{tema}_{i['p']}")
                    
                    # COMPLETAR
                    r_comp = {}
                    for i in d["quiz_cuento"]["completar"]:
                        r_comp[i["p"]] = st.text_input(i["p"], key=f"comp_{tema}_{i['p']}")
                    
                    if st.button("Verificar"):
                        err = 0
                        for i in d["quiz_cuento"]["seleccion"]:
                            if r_sel[i["p"]] != i["r"]: err += 1
                        for i in d["quiz_cuento"]["completar"]:
                            if r_comp[i["p"]].lower().strip() != i["r"].lower(): err += 1
                        
                        if err == 0: st.balloons(); st.success("¡Perfecto!")
                        else: st.warning(f"Tienes {err} errores o campos vacíos.")
            else: st.info("Cuento próximamente.")

        with t4:
            st.subheader("📄 Descargas")
            if d.get("pdf"):
                st.info(f"Aquí puedes descargar el material de {tema} una vez subido.")

elif menu == "Contacto":
    st.write("Soporte: pao.mzh16@gmail.com")
