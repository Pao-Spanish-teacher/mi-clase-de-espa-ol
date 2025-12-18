from gtts import gTTS
import ipywidgets as widgets
from IPython.display import Audio, display, clear_output
import os

# 1. Tu lista de frases para el examen
examen_frases = [
    "La casa es grande",
    "El gato duerme en el sofá",
    "Mañana comeremos paella",
    "Me gusta aprender programación",
    "El español es un idioma hermoso"
]

# Variables de control
puntos = 0
indice_pregunta = 0

def generar_audio(texto):
    tts = gTTS(text=texto, lang='es', tld='com.mx') # Acento mexicano
    tts.save("dictado_examen.mp3")
    return "dictado_examen.mp3"

def verificar_y_avanzar(b):
    global puntos, indice_pregunta
    
    # Limpiar espacios y minúsculas
    respuesta_usuario = entrada_texto.value.lower().strip().rstrip('.')
    respuesta_correcta = examen_frases[indice_pregunta].lower().strip().rstrip('.')
    
    # Evaluar
    if respuesta_usuario == respuesta_correcta:
        puntos += 1
        mensaje = "✅ ¡Correcto!"
    else:
        mensaje = f"❌ Error. Era: '{examen_frases[indice_pregunta]}'"
    
    indice_pregunta += 1
    entrada_texto.value = "" # Limpiar el cuadro para la siguiente
    
    # Mostrar siguiente o resultado final
    clear_output(wait=True)
    if indice_pregunta < len(examen_frases):
        print(mensaje)
        mostrar_interfaz()
    else:
        print(f"--- EXAMEN FINALIZADO ---")
        print(f"Puntuación final: {puntos} de {len(examen_frases)}")
        if puntos == len(examen_frases):
            print("🏆 ¡Eres un experto en ortografía!")

def mostrar_interfaz():
    print(f"Frase {indice_pregunta + 1} de {len(examen_frases)}")
    audio_path = generar_audio(examen_frases[indice_pregunta])
    display(Audio(audio_path, autoplay=False))
    display(entrada_texto)
    display(boton_enviar)

# Crear componentes
entrada_texto = widgets.Text(placeholder='Escribe lo que escuchas...')
boton_enviar = widgets.Button(description="Siguiente frase", button_style='info')
boton_enviar.on_click(verificar_y_avanzar)

# Iniciar examen
mostrar_interfaz()
