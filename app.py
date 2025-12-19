import streamlit as st
from gtts import gTTS
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Pao- Spanish- Teacher", page_icon="🎓", layout="wide")

# --- 2. DISEÑO VISUAL (CSS) ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #e0f2fe 0%, #fdfcfb 100%); }
    section[data-testid="stSidebar"] { background-color: #ffffff !important; border-right: 3px solid #1E88E5; }
    h1 { color: #1E88E5 !important; font-weight: 800; }
    .stTabs { background-color: rgba(255, 255, 255, 0.8); padding: 25px; border-radius: 20px; box-shadow: 0 10px 15px rgba(0,0,0,0.05); }
    .stButton>button { background-color: #1E88E5; color: white; border-radius: 12px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. CONTROL DE ACCESO ---
CONTRASEÑA = "pao_premium"
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("🔐 Acceso Privado - Pao- Spanish- Teacher")
    clave = st.text_input("Introduce tu clave de alumno:", type="password")
    if st.button("Ingresar a la Academia"):
        if clave == CONTRASEÑA:
            st.session_state.auth = True
            st.rerun()
        else: st.error("❌ Clave incorrecta")
    st.stop()

# --- 4. BARRA LATERAL ---
with st.sidebar:
    try: st.image("logo.png", width=180)
    except: st.warning("⚠️ Sube 'logo.png'")
    st.title("Pao- Spanish- Teacher")
    st.write("---")
    menu = st.radio("Navegación:", ["Inicio", "Lecciones", "Mi Progreso", "Contacto"])
    if st.button("Cerrar Sesión"):
        st.session_state.auth = False
        st.rerun()

# --- 5. LÓGICA DE SECCIONES ---

# --- INICIO ---
if menu == "Inicio":
    st.title("¡Bienvenida a tu Academia! ✨")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        try: 
            st.image("foto_pao.png", width=300)
        except: 
            st.info("ℹ️ Sube 'foto_pao.png'")
            
    with col2:
        st.subheader("Tu espacio de aprendizaje de español")
        
        # --- PAUTAS SIMPLES ---
        st.markdown("""
        ### 🚀 ¿Cómo aprovechar tus clases?
        1. **Mira el video:** Comienza siempre con la video-clase para entender el contexto.
        2. **Interactúa:** Escucha los cuentos y haz los dictados en voz alta.
        3. **Practica offline:** Descarga las fichas PDF para reforzar lo aprendido sin pantallas.
        
        ---
        """)

        # --- MENSAJE DE MOTIVACIÓN ---
        st.info("""
        **"El idioma es el mapa de una cultura. ¡Estoy aquí para ayudarte a recorrerlo con confianza!"** *No importa qué tan rápido vayas, lo importante es no detenerse. ¡Vamos a lograrlo juntos!*
        """)
        
        st.write("👈 Selecciona **'Lecciones'** en el menú para comenzar tu viaje.")
elif menu == "Lecciones":
    st.title("📚 Centro de Capacitación por Niveles")

    # 1. Selector de Nivel
    nivel = st.selectbox(
        "Primero, elige tu nivel de español:",
        ["Selecciona nivel...", "Nivel A1 (Principiante)", "Nivel A2 (Básico)", "Nivel B1 (Intermedio)"]
    )

    st.write("---")

    # 2. Lógica por Nivel
    if nivel == "Nivel A1 (Principiante)":
        st.subheader("🟢 Contenido Nivel A1")
        
        # Aquí salen los temas específicos de A1
        tema_a1 = st.selectbox(
            "¿Qué tema de A1 quieres estudiar?",
            ["Selecciona un tema...", "Saludos", "Los Números", "El Alfabeto"]
        )

        if tema_a1 == "Saludos":
            st.header("📍 Tema: Los Saludos")
            # AQUÍ PEGAS TODAS LAS PESTAÑAS (TABS) QUE YA HICIMOS
            t_video, t_dictado, t_cuento, t_nombres, t_quiz, t_print = st.tabs([
                "📺 Video Clase", "🎧 Dictado", "📖 El Cuento", 
                "🖼️ Vocabulario", "✍️ Selección Simple", "📄 Para Imprimir"
            ])
            # ... (Aquí va el resto del código de las pestañas que ya tienes)

    elif nivel == "Nivel A2 (Básico)":
        st.subheader("🟡 Contenido Nivel A2")
        tema_a2 = st.selectbox("¿Qué tema de A2 quieres estudiar?", ["Selecciona...", "Pasado Simple", "La Familia"])
        st.info("Próximamente contenido para A2...")

    elif nivel == "Nivel B1 (Intermedio)":
        st.subheader("🔴 Contenido Nivel B1")
        st.info("Próximamente contenido para B1...")
    # --- DESARROLLO DEL TEMA: SALUDOS ---
    if tema_seleccionado == "Saludos":
        st.header("📍 Tema: Los Saludos")
        
        # Aquí creamos todas las herramientas en pestañas para este tema
        t_video, t_dictado, t_cuento, t_nombres, t_quiz, t_print = st.tabs([
            "📺 Video Clase", 
            "🎧 Dictado", 
            "📖 El Cuento", 
            "🖼️ Vocabulario (Nombres)", 
            "✍️ Selección Simple", 
            "📄 Para Imprimir"
        ])

        with t_video:
            st.subheader("Video Principal de Saludos")
            try: st.video("saludos_clase.mp4")
            except: st.info("🎥 Sube 'saludos_clase.mp4' a GitHub")

        with t_dictado:
            st.subheader("🎧 Desafío de Dictado: 5 Frases")

            # 1. Lista de tus 5 frases
            lista_frases = [
                "Hola, ¿cómo estás?",
                "Buenos días",
                "Mucho gusto",
                "¿Cómo te llamas?",
                "Hasta mañana"
            ]

            # 2. Inicializar el contador de frases si no existe
            if 'indice_frase' not in st.session_state:
                st.session_state.indice_frase = 0

            # Verificamos si ya terminó todas las frases
            if st.session_state.indice_frase < len(lista_frases):
                frase_actual = lista_frases[st.session_state.indice_frase]
                
                st.write(f"### Frase {st.session_state.indice_frase + 1} de {len(lista_frases)}")
                
                # Botón para escuchar
                if st.button("🔊 Escuchar frase"):
                    tts = gTTS(text=frase_actual, lang='es')
                    tts.save("dictado.mp3")
                    st.audio("dictado.mp3")

                # Entrada de texto
                resp = st.text_input("Escribe lo que escuchaste:", key=f"input_{st.session_state.indice_frase}")

                if st.button("Comprobar"):
                    # Limpiamos espacios y mayúsculas para que no falle por un error simple
                    if resp.lower().strip().replace(",", "").replace("¿", "").replace("?", "") == \
                       frase_actual.lower().strip().replace(",", "").replace("¿", "").replace("?", ""):
                        
                        st.success("✨ ¡Correcto! Muy bien hecho.")
                        # Avanzar a la siguiente frase
                        st.session_state.indice_frase += 1
                        st.button("Siguiente frase ➡️")
                    else:
                        st.error("Todavía no es correcto. ¡Escucha de nuevo!")
            
            else:
                st.balloons()
                st.success("🎊 ¡Felicidades! Has completado el dictado de hoy.")
                if st.button("Repetir dictado desde el inicio"):
                    st.session_state.indice_frase = 0
                    st.rerun()

        with t_cuento:
            st.subheader("Videocuento Narrado")
            try: st.video("cuento_saludos.mp4")
            except: st.info("🎥 Sube 'cuento_saludos.mp4'")
            with st.expander("Leer texto del cuento"):
                st.write("Había una vez una niña llamada Ana que saludaba a todos...")

        with t_nombres:
            st.subheader("¿Cómo se llama?")
            st.write("Escribe el nombre correcto para cada imagen:")
            col_img1, col_img2 = st.columns(2)
            with col_img1:
                try: st.image("img_saludo1.png", width=200)
                except: st.info("Sube 'img_saludo1.png'")
                nombre1 = st.text_input("Nombre de la acción 1:", key="n1")
            with col_img2:
                try: st.image("img_saludo2.png", width=200)
                except: st.info("Sube 'img_saludo2.png'")
                nombre2 = st.text_input("Nombre de la acción 2:", key="n2")

        with t_quiz:
            st.subheader("Selección Simple")
            opcion = st.radio("¿Cuál es un saludo de mañana?", ["Buenas noches", "Buenos días", "Hola"], key="q_saludos")
            if st.button("Validar Respuesta"):
                if opcion == "Buenos días": st.success("✅ ¡Correcto!")
                else: st.error("❌ Intenta otra vez")

        with t_print:
            st.subheader("Material Descargable")
            st.write("Descarga la ficha de actividades para practicar en papel.")
            try:
                with open("ficha_saludos.pdf", "rb") as f:
                    st.download_button("📩 Descargar Ficha (PDF)", f, "Ficha_Saludos_Pao.pdf")
            except: st.warning("ℹ️ Sube 'ficha_saludos.pdf' para activar la descarga.")

    # --- ESPACIO PARA OTROS TEMAS ---
    elif tema_seleccionado == "Números":
        st.header("📍 Tema: Los Números")
        st.info("Contenido en construcción... pronto verás los videos y ejercicios aquí.")

    elif tema_seleccionado == "Alfabeto":
        st.header("📍 Tema: El Alfabeto")
        st.info("Contenido en construcción...")

elif menu == "Mi Progreso":
    st.title("🏆 Mi Progreso")
    st.progress(20)

elif menu == "Contacto":
    st.title("📩 Contacto")
    st.write("Si tienes alguna duda, escríbeme directamente:")
    
    # Esto crea un recuadro visualmente atractivo con el correo
    st.success("📧 **pao.mzh16@gmail.com**")
    
    st.write("Estaré encantada de ayudarte con tu proceso de aprendizaje.")
