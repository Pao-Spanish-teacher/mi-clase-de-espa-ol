# --- ACTUALIZACIÓN DEL DICCIONARIO DE DATOS PARA SALUDOS ---
# (Solo agrego la clave "cuento" y los datos del quiz para que el código sea inteligente)

DATOS_TEMAS["1. Saludos y Despedidas"]["cuento"] = "https://youtube.com/shorts/yhH8rwpEHRo"
DATOS_TEMAS["1. Saludos y Despedidas"]["quiz_cuento"] = {
    "seleccion": [
        {"p": "1. ¿Cómo se llama la niña que está jugando en la arena?", "o": ["María", "Brisa", "Ana"], "r": "Brisa"},
        {"p": "2. ¿Cuál es la primera palabra que usa Río?", "o": ["Adiós", "Gracias", "Hola"], "r": "Hola"},
        {"p": "3. ¿Qué edad mencionan tener ambos niños?", "o": ["5 años", "7 años", "10 años"], "r": "5 años"},
        {"p": "4. ¿Qué frase de cortesía usan después de presentarse?", "o": ["De nada", "Mucho gusto", "Perdón"], "r": "Mucho gusto"},
        {"p": "5. ¿Qué palabra usan para despedirse?", "o": ["Hola", "Adiós", "Por favor"], "r": "Adiós"},
        {"p": "6. ¿Qué estaba construyendo Brisa?", "o": ["Una casa", "Un castillo de arena", "Un túnel"], "r": "Un castillo de arena"},
        {"p": "7. ¿En qué lugar se encuentran los niños?", "o": ["Escuela", "Parque", "Playa"], "r": "Parque"},
        {"p": "8. Si alguien te pregunta cómo estás, respondes:", "o": ["¡Qué mal!", "Estoy bien, gracias", "No quiero hablar"], "r": "Estoy bien, gracias"},
        {"p": "9. Si es de mañana, debes decir:", "o": ["Buenas noches", "Buenos días", "Hasta luego"], "r": "Buenos días"},
        {"p": "10. ¿Cómo se llama el niño?", "o": ["Mar", "Río", "Lago"], "r": "Río"}
    ],
    "completar": [
        {"p": "11. ¿Cómo __________?", "r": "estás"},
        {"p": "12. ¿Cómo te __________?", "r": "llamas"},
        {"p": "13. Yo vivo en la __________", "r": "ciudad"},
        {"p": "14. __________ favor", "r": "Por"},
        {"p": "15. Hasta __________", "r": "mañana"},
        {"p": "16. Palabra mágica: __________", "r": "Gracias"},
        {"p": "17. Serían muy buenos __________", "r": "amigos"},
        {"p": "18. Por la tarde: Buenas __________", "r": "tardes"},
        {"p": "19. Encantado o Mucho __________", "r": "gusto"},
        {"p": "20. La niña se llama __________", "r": "Brisa"}
    ]
}

# --- DENTRO DE LA PESTAÑA t_story (Cuento y Práctica) ---
with t_story:
    st.subheader("🎬 Mira el cuento y resuelve")
    if "cuento" in datos:
        st.video(datos["cuento"])
        st.markdown("---")
        
        if "quiz_cuento" in datos:
            st.write("### ✍️ Parte I: Selección Múltiple")
            respuestas_usuario = {}
            for item in datos["quiz_cuento"]["seleccion"]:
                respuestas_usuario[item["p"]] = st.radio(item["p"], item["o"], key=f"sel_{tema_elegido}_{item['p']}")
            
            st.write("### ✏️ Parte II: Completación")
            completar_usuario = {}
            for item in datos["quiz_cuento"]["completar"]:
                completar_usuario[item["p"]] = st.text_input(item["p"], key=f"comp_{tema_elegido}_{item['p']}")
            
            if st.button("Verificar Respuestas"):
                errores = 0
                # Validar selección
                for item in datos["quiz_cuento"]["seleccion"]:
                    if respuestas_usuario[item["p"]] != item["r"]: errores += 1
                # Validar completación
                for item in datos["quiz_cuento"]["completar"]:
                    if completar_usuario[item["p"]].lower().strip() != item["r"].lower(): errores += 1
                
                if errores == 0:
                    st.balloons()
                    st.success("✨ ¡Perfecto! Has comprendido todo el cuento.")
                else:
                    st.warning(f"⚠️ Tienes {errores} respuesta(s) incorrecta(s). ¡Vuelve a ver el video para encontrar la respuesta correcta!")
    else:
        st.info("📌 El video del cuento estará disponible pronto.")
