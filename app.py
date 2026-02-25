import streamlit as st
from gtts import gTTS
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Pao-Spanish-Teacher Academy", page_icon="🎓", layout="wide")

# --- 2. DICCIONARIO MAESTRO ACTUALIZADO ---
DATOS_TEMAS = {
    "1. Saludos y Despedidas": {
        "video": "https://www.youtube.com/watch?v=hll10VBLFoQ",
        "cuento": "https://www.youtube.com/watch?v=yhH8rwpEHRo",
        "pdf": "minilibro Saludos.pdf",
        "frases": ["Buenos días", "¿Cómo estás?", "Mucho gusto", "Hasta mañana"],
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. ¿Cómo se llama la niña?", "o": ["María", "Brisa", "Ana"], "r": "Brisa"},
                {"p": "2. ¿Primera palabra de Río?", "o": ["Adiós", "Gracias", "Hola"], "r": "Hola"},
                {"p": "3. ¿Qué edad tienen?", "o": ["5 años", "7 años", "10 años"], "r": "5 años"},
                {"p": "4. Frase tras presentarse:", "o": ["De nada", "Mucho gusto", "Perdón"], "r": "Mucho gusto"},
                {"p": "5. Palabra para despedirse:", "o": ["Hola", "Adiós", "Por favor"], "r": "Adiós"},
                {"p": "6. ¿Qué construía Brisa?", "o": ["Una casa", "Un castillo de arena", "Un túnel"], "r": "Un castillo de arena"},
                {"p": "7. ¿Dónde están?", "o": ["En la escuela", "En un parque", "En la playa"], "r": "En un parque"},
                {"p": "8. Respuesta a ¿cómo estás?", "o": ["¡Qué mal!", "Estoy bien, gracias", "No quiero hablar"], "r": "Estoy bien, gracias"},
                {"p": "9. Saludo por la mañana:", "o": ["Buenas noches", "Buenos días", "Hasta luego"], "r": "Buenos días"},
                {"p": "10. ¿Cómo se llama el niño?", "o": ["Mar", "Río", "Lago"], "r": "Río"}
            ],
            "completar": [
                {"p": "11. Río pregunta: '¿Cómo __________?'", "r": "estás"},
                {"p": "12. El niño pregunta: '¿Cómo te __________?'", "r": "llamas"},
                {"p": "13. Río: 'Yo vivo en la __________'", "r": "ciudad"},
                {"p": "14. '__________ favor' (frase educada)", "r": "Por"},
                {"p": "15. 'Hasta __________' (para verse mañana)", "r": "mañana"},
                {"p": "16. Palabra mágica: '__________'", "r": "Gracias"},
                {"p": "17. Serían muy buenos __________", "r": "amigos"},
                {"p": "18. Saludo por la tarde: 'Buenas __________'", "r": "tardes"},
                {"p": "19. Encantado o 'Mucho __________'", "r": "gusto"},
                {"p": "20. La niña es __________ y el niño es Río.", "r": "Brisa"}
            ]
        }
    },
    "2. Los Números (Naturales y Ordinales)": {
        "video": "https://www.youtube.com/watch?v=nxMBJQAE2ZU",
        "cuento": "https://www.youtube.com/watch?v=D88ftO3xU30",
        "pdf": "Minilibros Los números en español (0-100).pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. ¿Dónde es la carrera?", "o": ["Ciudad", "Bosque", "Playa"], "r": "Bosque"},
                {"p": "2. ¿Quién ganó (1° lugar)?", "o": ["Elara", "Mateo", "Renardo"], "r": "Mateo el conejo"},
                {"p": "3. ¿Lugar de la tortuga Elara?", "o": ["1°", "2°", "3°"], "r": "2° lugar"},
                {"p": "4. ¿Quién quedó 3°?", "o": ["Oswaldo", "Renardo", "Pip"], "r": "Renardo"},
                {"p": "5. ¿Quién quedó 4°?", "o": ["Silvi", "Oswaldo", "Mateo"], "r": "Oswaldo el oso"},
                {"p": "6. ¿Qué hacía Silvi (5°)?", "o": ["Dormía", "Buscaba nueces", "Volaba"], "r": "Buscaba nueces"},
                {"p": "7. ¿Quién quedó 6°?", "o": ["Pip", "Feliz", "Renardo"], "r": "Pip"},
                {"p": "8. ¿Quién quedó 7°?", "o": ["Perro", "Feliz", "Oso"], "r": "Feliz el gato"},
                {"p": "9. ¿Qué hacía Feliz el gato?", "o": ["Corría", "Dormía", "Comía"], "r": "Dormía un poco"},
                {"p": "10. ¿Cómo se movía Pip?", "o": ["Corriendo", "Volando bajo", "Saltando"], "r": "Volando bajo"}
            ],
            "completar": [
                {"p": "11. El ganador fue el conejo __________", "r": "Mateo"},
                {"p": "12. La tortuga llegó en el __________ lugar.", "r": "2°"},
                {"p": "13. El zorro __________ fue el tercero.", "r": "Renardo"},
                {"p": "14. El oso __________ llegó de 4°.", "r": "Oswaldo"},
                {"p": "15. La ardilla __________ ocupa el quinto lugar.", "r": "Silvi"},
                {"p": "16. Pip es un __________ que vuela bajo.", "r": "pájaro"},
                {"p": "17. El gato __________ llegó de séptimo.", "r": "Feliz"},
                {"p": "18. Mateo llegó en el __________ lugar.", "r": "1°"},
                {"p": "19. El animal de 5° lugar es la __________ Silvi.", "r": "ardilla"},
                {"p": "20. El gato quedó en el __________ lugar.", "r": "7°"}
            ]
        }
    },
    "3. Los Colores": {
        "video": "https://www.youtube.com/watch?v=UF5HWnCrAU8",
        "cuento": "https://www.youtube.com/watch?v=BDN7ST1YwcE",
        "pdf": "Minilibro Los colores en español.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. Colores primarios:", "o": ["Verde/Naranja/Violeta", "Amarillo/Azul/Rojo", "Blanco/Negro"], "r": "Amarillo, azul y rojo"},
                {"p": "2. Azul + Amarillo =", "o": ["Morado", "Verde", "Naranja"], "r": "Verde"},
                {"p": "3. Rojo + Azul =", "o": ["Violeta", "Verde", "Marrón"], "r": "Violeta / Morado"},
                {"p": "4. Rojo + Amarillo =", "o": ["Rosa", "Naranja", "Celeste"], "r": "Naranja"},
                {"p": "5. Colores neutros:", "o": ["Rojo/Azul", "Blanco/Negro", "Verde/Amarillo"], "r": "Blanco y Negro"},
                {"p": "6. Mezcla con Blanco:", "o": ["Oscurece", "Aclara (pasteles)", "Desaparece"], "r": "El color se vuelve más claro (pasteles)"},
                {"p": "7. Ausencia de luz:", "o": ["Gris", "Negro", "Blanco"], "r": "Negro"},
                {"p": "8. Mezcla de dos primarios:", "o": ["Terceros", "Secundarios", "Básicos"], "r": "Colores Secundarios"},
                {"p": "9. Blanco + Negro =", "o": ["Marrón", "Gris", "Crema"], "r": "Gris"},
                {"p": "10. ¿Cuál es primario?", "o": ["Naranja", "Amarillo", "Verde"], "r": "Amarillo"}
            ],
            "completar": [
                {"p": "11. Rojo, azul y amarillo son colores __________.", "r": "primarios"},
                {"p": "12. Azul + Rojo = __________.", "r": "morado"},
                {"p": "13. El __________ es neutro y aclara.", "r": "blanco"},
                {"p": "14. El verde es un color __________.", "r": "secundario"},
                {"p": "15. Rojo + Amarillo = color de la __________.", "r": "naranja"},
                {"p": "16. Negro y blanco son colores __________.", "r": "neutros"},
                {"p": "17. El __________ es primario como el cielo.", "r": "azul"},
                {"p": "18. Blanco + Negro = __________.", "r": "gris"},
                {"p": "19. El __________ recuerda al sol.", "r": "amarillo"},
                {"p": "20. Para oscurecer uso el color __________.", "r": "negro"}
            ]
        }
    },
    "4. Días, Meses y Estaciones": {
        "video": "https://www.youtube.com/watch?v=T9fvfbMQn2I",
        "cuento": "https://www.youtube.com/watch?v=h1K6BKCX6g8",
        "video_estaciones": "https://www.youtube.com/watch?v=nqv12fATbOQ",
        "pdf": "Minilibro Los días, los meses y las estaciones.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. ¿Primer mes?", "o": ["Febrero", "Enero", "Marzo"], "r": "Enero"},
                {"p": "2. ¿Mes más corto?", "o": ["Abril", "Febrero", "Junio"], "r": "Febrero"},
                {"p": "3. ¿Mes de Navidad?", "o": ["Noviembre", "Octubre", "Diciembre"], "r": "Diciembre"},
                {"p": "4. ¿Qué sigue a Agosto?", "o": ["Septiembre", "Julio", "Octubre"], "r": "Septiembre"},
                {"p": "5. ¿Mes número seis?", "o": ["Mayo", "Junio", "Julio"], "r": "Junio"},
                {"p": "6. ¿Estación de flores?", "o": ["Invierno", "Primavera", "Otoño"], "r": "Primavera"},
                {"p": "7. ¿Estación calurosa?", "o": ["Verano", "Invierno", "Otoño"], "r": "Verano"},
                {"p": "8. ¿Estación de hojas caídas?", "o": ["Verano", "Primavera", "Otoño"], "r": "Otoño"},
                {"p": "9. ¿Estación fría/nieve?", "o": ["Invierno", "Primavera", "Verano"], "r": "Invierno"},
                {"p": "10. ¿Cuántas estaciones hay?", "o": ["Dos", "Cuatro", "Seis"], "r": "Cuatro"}
            ],
            "completar": [
                {"p": "11. Entre marzo y mayo está __________.", "r": "Abril"},
                {"p": "12. El año tiene __________ meses.", "r": "doce"},
                {"p": "13. Mes de las flores (5): __________.", "r": "Mayo"},
                {"p": "14. Estación del 'renacimiento': __________.", "r": "Primavera"},
                {"p": "15. En __________ los días son más largos.", "r": "Verano"},
                {"p": "16. Hojas secas en el __________.", "r": "Otoño"},
                {"p": "17. Gorro y guantes en el __________.", "r": "Invierno"},
                {"p": "18. Sigue a la primavera: __________.", "r": "Verano"},
                {"p": "19. Diciembre inicia el __________ (Norte).", "r": "Invierno"},
                {"p": "20. Mes número siete: __________.", "r": "Julio"}
            ]
        }
    },
    "5. La Hora y Rutina Diaria": {
        "video": "https://youtu.be/CbqNMMNza9w",
        "cuento": "https://www.youtube.com/watch?v=2BOKYde4vNM",
        "pdf": "Minilibro La Hora en Español.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. ¿A qué hora despierta Pedro?", "o": ["7:00", "8:00", "9:00"], "r": "A las 8:00"},
                {"p": "2. ¿A qué hora desayuna?", "o": ["8:00", "8:30", "9:00"], "r": "A las 8:30"},
                {"p": "3. ¿Qué bebe Pedro?", "o": ["Jugo", "Café con leche", "Chocolate"], "r": "Café con leche muy caliente"},
                {"p": "4. ¿A qué hora empieza clase?", "o": ["8:30", "9:00", "10:00"], "r": "A las 9:00"},
                {"p": "5. ¿A qué hora almuerza?", "o": ["12:00", "1:15", "2:30"], "r": "A la 1:15"},
                {"p": "6. ¿Qué hace a las 5:00 PM?", "o": ["Lee", "Deporte", "Duerme"], "r": "Hacer deporte"},
                {"p": "7. ¿Hora de cena?", "o": ["7:00", "8:00", "9:00"], "r": "A las 8:00"},
                {"p": "8. ¿Qué cena Pedro?", "o": ["Pizza", "Ensalada y pescado", "Arroz"], "r": "Ensalada de tomate y un poco de pescado"},
                {"p": "9. Actividad antes de dormir:", "o": ["TV", "Leer un libro", "Cocinar"], "r": "Leer un libro"},
                {"p": "10. ¿A qué hora se duerme?", "o": ["9:00", "10:00", "11:00"], "r": "A las 10:00"}
            ],
            "completar": [
                {"p": "11. Despierta a las __________ de la mañana.", "r": "8"},
                {"p": "12. Desayuna pan con __________.", "r": "mantequilla"},
                {"p": "13. El café está muy __________.", "r": "caliente"},
                {"p": "14. A las __________ entra a clase.", "r": "9"},
                {"p": "15. Come con sus __________.", "r": "amigos"},
                {"p": "16. A las 5 va al __________.", "r": "parque"},
                {"p": "17. El deporte lo hace antes de ir a __________.", "r": "casa"},
                {"p": "18. La cena incluye un poco de __________.", "r": "pescado"},
                {"p": "19. Antes de dormir le gusta __________.", "r": "leer"},
                {"p": "20. Se duerme a las __________ de la noche.", "r": "10"}
            ]
        }
    },
    "6. La Familia": {
        "video": "https://www.youtube.com/watch?v=4C9JiqgMt8o",
        "pdf": "minilibro La familia en español.pdf"
    },
    "7. Profesiones (Generales y Técnicas)": {
        "video": "https://www.youtube.com/watch?v=szed1no5viA",
        "cuento": "https://www.youtube.com/watch?v=smnwY7G3VUQ",
        "pdf": "Minilibro Las profesiones en español.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. ¿Quién enseña en la escuela?", "o": ["Policía", "Maestra", "Cocinero"], "r": "La maestra"},
                {"p": "2. Apaga incendios (uniforme rojo):", "o": ["Bombero", "Médico", "Piloto"], "r": "El bombero"},
                {"p": "3. Cura personas enfermas:", "o": ["Veterinario", "Doctor", "Fotógrafo"], "r": "El doctor"},
                {"p": "4. Cuida a los animales:", "o": ["Doctor", "Veterinario", "Enfermera"], "r": "El veterinario"},
                {"p": "5. Usa gorro blanco y sartén:", "o": ["Fontanero", "Cocinero", "Policía"], "r": "El cocinero"},
                {"p": "6. Dirige el tráfico:", "o": ["Bombero", "Policía", "Piloto"], "r": "El policía"},
                {"p": "7. Vuela el avión:", "o": ["Fotógrafo", "Piloto", "Fontanero"], "r": "El piloto"},
                {"p": "8. Ayuda al doctor:", "o": ["Enfermera", "Maestra", "Cocinero"], "r": "La enfermera"},
                {"p": "9. Toma fotos:", "o": ["Fotógrafo", "Veterinario", "Bombero"], "r": "El fotógrafo"},
                {"p": "10. Arregla tuberías:", "o": ["Policía", "Fontanero", "Doctor"], "r": "El fontanero"}
            ],
            "completar": [
                {"p": "11. La __________ escribe en la pizarra.", "r": "maestra"},
                {"p": "12. El __________ usa manguera y agua.", "r": "bombero"},
                {"p": "13. Si tengo fiebre voy al __________.", "r": "doctor"},
                {"p": "14. El __________ cuida a mi perrito.", "r": "veterinario"},
                {"p": "15. El __________ prepara comida rica.", "r": "cocinero"},
                {"p": "16. El __________ lleva una placa.", "r": "policía"},
                {"p": "17. El __________ está en la cabina.", "r": "piloto"},
                {"p": "18. La __________ cura heridas.", "r": "enfermera"},
                {"p": "19. El __________ usa una cámara.", "r": "fotógrafo"},
                {"p": "20. El __________ arregla el lavabo.", "r": "fontanero"}
            ]
        }
    },
    "8. Nacionalidad y Países": {
        "video": "https://www.youtube.com/watch?v=T2HVf4YqHZY",
        "pdf": "Minilibros Los países y nacionalidades en español.pdf"
    },
    "9. Partes del Cuerpo": {
        "video": "https://www.youtube.com/watch?v=OfX0hCFCdeA",
        "cuento": "https://www.youtube.com/watch?v=JyedWS0rQ5s",
        "pdf": "Minilibro Las partes del cuerpo en español.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. Para ver colores:", "o": ["Oídos", "Ojos", "Nariz"], "r": "Los ojos"},
                {"p": "2. Para caminar:", "o": ["Manos", "Brazos", "Piernas"], "r": "Las piernas"},
                {"p": "3. Para escuchar:", "o": ["Ojos", "Orejas", "Pies"], "r": "Los orejas / oídos"},
                {"p": "4. Para agarrar/escribir:", "o": ["Pies", "Manos", "Hombros"], "r": "Las manos"},
                {"p": "5. ¿Dónde está el cerebro?", "o": ["Pecho", "Cabeza", "Estómago"], "r": "En la cabeza"},
                {"p": "6. Para oler flores:", "o": ["Boca", "Nariz", "Cuello"], "r": "La nariz"},
                {"p": "7. Articulación del brazo:", "o": ["Tobillo", "Rodilla", "Codo"], "r": "El codo"},
                {"p": "8. Dedos con uñas en:", "o": ["Manos", "Pies", "Manos y Pies"], "r": "En las manos y en los pies"},
                {"p": "9. Protege el corazón:", "o": ["Abdomen", "Torso", "Espalda"], "r": "El torso / caja torácica"},
                {"p": "10. Une cabeza y cuerpo:", "o": ["Hombro", "Cuello", "Cintura"], "r": "El cuello"}
            ],
            "completar": [
                {"p": "11. El dedo más pequeño: __________.", "r": "meñique"},
                {"p": "12. Uso la __________ para hablar.", "r": "boca"},
                {"p": "13. Doblo la pierna con la __________.", "r": "rodilla"},
                {"p": "14. Camino con los __________.", "r": "pies"},
                {"p": "15. En la cara hay una nariz y una __________.", "r": "boca"},
                {"p": "16. Las __________ tienen palmas.", "r": "manos"},
                {"p": "17. La __________ nos mantiene rectos.", "r": "espalda"},
                {"p": "18. Huelo perfume con la __________.", "r": "nariz"},
                {"p": "19. El tacto está en la __________.", "r": "piel"},
                {"p": "20. Al final de las piernas están los __________.", "r": "pies"}
            ]
        }
    },
    "10. La Ropa y Vestimenta": {
        "video": "https://www.youtube.com/watch?v=nOisiL-Pyak",
        "pdf": "Minilibro La ropa y la vestimenta en español.pdf"
    },
    "11. Comida y Bebidas": {
        "video": "https://www.youtube.com/watch?v=9iPhcCg64j8",
        "cuento": "https://www.youtube.com/watch?v=SyraFpsEFls",
        "pdf": "Minilibro Comidas y Bebidas en Español..pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. Desayuno de Mateo:", "o": ["Galletas", "Pan tostado", "Frutas"], "r": "Pan tostado"},
                {"p": "2. Bebida caliente de Mateo:", "o": ["Chocolate", "Té", "Café"], "r": "Café"},
                {"p": "3. Color de la taza:", "o": ["Roja", "Blanca", "Azul"], "r": "Azul"},
                {"p": "4. Color de la leche:", "o": ["Amarilla", "Blanca", "Crema"], "r": "Blanca"},
                {"p": "5. Elena prefiere comida:", "o": ["Rápida", "Sana", "Dulces"], "r": "Comida sana"},
                {"p": "6. Frutas de Elena:", "o": ["Pera/Uva", "Manzana/Banana", "Sandía/Melón"], "r": "Manzana y banana"},
                {"p": "7. ¿A qué hora cocina Mateo?", "o": ["Noche", "Mediodía", "Mañana"], "r": "Al mediodía"},
                {"p": "8. ¿Qué usa para cocinar?", "o": ["Sartén", "Olla grande", "Horno"], "r": "Una olla grande"},
                {"p": "9. ¿Qué prepara Mateo?", "o": ["Sopa", "Arroz blanco", "Espaguetis"], "r": "Arroz blanco"},
                {"p": "10. El arroz está:", "o": ["Picante", "Delicioso", "Salado"], "r": "Delicioso"}
            ],
            "completar": [
                {"p": "11. Mateo come pan __________.", "r": "tostado"},
                {"p": "12. El café está muy __________.", "r": "caliente"},
                {"p": "13. Su hermana se llama __________.", "r": "Elena"},
                {"p": "14. Elena elige comida __________.", "r": "sana"},
                {"p": "15. Come una __________ roja.", "r": "manzana"},
                {"p": "16. Come una __________ amarilla.", "r": "banana"},
                {"p": "17. Cocina al __________.", "r": "mediodía"},
                {"p": "18. Usa una __________ grande.", "r": "olla"},
                {"p": "19. El arroz es de color __________.", "r": "blanco"},
                {"p": "20. El arroz es __________ para todos.", "r": "delicioso"}
            ]
        }
    },
    "12. La Casa": {
        "video": "https://youtu.be/2Wz5yyw80gs",
        "cuento": "https://www.youtube.com/watch?v=yHd_5EQuIN0",
        "pdf": "Minilibro La casa y sus partes en español.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. Color de la casa:", "o": ["Verde", "Amarilla", "Blanca"], "r": "Amarilla"},
                {"p": "2. ¿Cómo es la cocina?", "o": ["Pequeña", "Grande y moderna", "Oscura"], "r": "Grande y moderna"},
                {"p": "3. Material de la mesa:", "o": ["Plástico", "Madera", "Vidrio"], "r": "De madera"},
                {"p": "4. Objeto azul en el cuarto:", "o": ["Silla", "Cama", "Cortina"], "r": "Una cama"},
                {"p": "5. ¿Cómo es el baño?", "o": ["Grande", "Pequeño y blanco", "Ruidoso"], "r": "Pequeño, limpio y de color blanco"},
                {"p": "6. ¿Qué hay en el jardín?", "o": ["Pasto", "Flores y un árbol", "Piscina"], "r": "Muchas flores de colores y un árbol alto"},
                {"p": "7. ¿Dónde está la cama azul?", "o": ["Cocina", "Dormitorio", "Baño"], "r": "En el dormitorio"},
                {"p": "8. El árbol es:", "o": ["Pequeño", "Alto", "Frutal"], "r": "Alto"},
                {"p": "9. Color del baño limpio:", "o": ["Amarillo", "Blanco", "Gris"], "r": "Blanco"},
                {"p": "10. Diseño de la cocina:", "o": ["Tradicional", "Moderno", "Rústico"], "r": "Moderno"}
            ],
            "completar": [
                {"p": "11. La casa es de color __________.", "r": "amarillo"},
                {"p": "12. La cocina es __________ y moderna.", "r": "grande"},
                {"p": "13. Mesa de __________.", "r": "madera"},
                {"p": "14. Cama de color __________.", "r": "azul"},
                {"p": "15. Baño de color __________.", "r": "blanco"},
                {"p": "16. Árbol muy __________.", "r": "alto"},
                {"p": "17. Jardín con muchas __________.", "r": "flores"},
                {"p": "18. Veo afuera por la __________.", "r": "ventana"},
                {"p": "19. El baño es __________, pero funcional.", "r": "pequeño"},
                {"p": "20. Lugar moderno: la __________.", "r": "cocina"}
            ]
        }
    },
    "13. Objetos Cotidianos": {
        "pdf": "Minilibros Los objetos cotidianos en español.pdf"
    },
    "14. Medios de Transporte": {
        "cuento": "https://www.youtube.com/watch?v=9Lv9Ih46MxA",
        "pdf": "Minilibros Los medios de transporte en español.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. Color del carro:", "o": ["Azul", "Rojo", "Blanco"], "r": "Rojo"},
                {"p": "2. Transporte blanco que vuela:", "o": ["Tren", "Avión", "Carro"], "r": "El avión"},
                {"p": "3. Transporte azul de 2 ruedas:", "o": ["Carro", "Moto", "Tren"], "r": "La moto"},
                {"p": "4. Color del tren:", "o": ["Blanco", "Gris", "Rojo"], "r": "Gris"},
                {"p": "5. Tiene alas y es blanco:", "o": ["Moto", "Avión", "Tren"], "r": "El avión"},
                {"p": "6. Rojo y 4 ruedas:", "o": ["Carro", "Avión", "Moto"], "r": "El carro"},
                {"p": "7. Sonido fuerte, gris y largo:", "o": ["Avión", "Tren", "Carro"], "r": "El tren"},
                {"p": "8. Necesita casco (es azul):", "o": ["Gris", "Moto azul", "Rojo"], "r": "Azul (La moto)"},
                {"p": "9. Despega hacia las nubes:", "o": ["Tren", "Avión", "Carro"], "r": "El avión"},
                {"p": "10. Si es rojo es un:", "o": ["Moto", "Carro", "Tren"], "r": "El carro"}
            ],
            "completar": [
                {"p": "11. Carro de color __________.", "r": "rojo"},
                {"p": "12. La moto es de color __________.", "r": "azul"},
                {"p": "13. El __________ corre en rieles.", "r": "tren"},
                {"p": "14. El avión es de color __________.", "r": "blanco"},
                {"p": "15. El carro rojo tiene __________ ruedas.", "r": "cuatro"},
                {"p": "16. La __________ tiene 2 ruedas.", "r": "moto"},
                {"p": "17. El tren es de color __________.", "r": "gris"},
                {"p": "18. El __________ cruza el cielo.", "r": "avión"},
                {"p": "19. Carro rojo y moto __________.", "r": "azul"},
                {"p": "20. Transporte más largo: __________.", "r": "tren"}
            ]
        }
    },
    "15. Los Lugares de la Ciudad": {
        "video": "https://www.youtube.com/watch?v=DziT1MJLmk4",
        "pdf": "Minilibro Los lugares en español.pdf"
    },
    "16. Los Animales (Domésticos y Salvajes)": {
        "video": "https://www.youtube.com/watch?v=G2n_FA_vhPU",
        "cuento": "https://www.youtube.com/watch?v=WsPVCwvWsiw",
        "pdf": "Minilibro Los animales domésticos en español.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. Dice 'muuu' y da leche:", "o": ["Perro", "Vaca", "Gato"], "r": "La vaca"},
                {"p": "2. Dice 'guau', mejor amigo:", "o": ["Pato", "Perro", "Cerdo"], "r": "El perro"},
                {"p": "3. Dice 'miau':", "o": ["Conejo", "Gato", "Pollito"], "r": "El gato"},
                {"p": "4. Dice 'cuac' y nada:", "o": ["Pato", "Gallo", "Oveja"], "r": "El pato"},
                {"p": "5. Pollito dice:", "o": ["Miau", "Pío pío", "Oink"], "r": "El pollito"},
                {"p": "6. Orejas largas y zanahorias:", "o": ["Perro", "Conejo", "Caballo"], "r": "El conejo"},
                {"p": "7. Da lana y dice 'beee':", "o": ["Cabra", "Oveja", "Vaca"], "r": "La oveja"},
                {"p": "8. Gallo dice:", "o": ["Cuac", "Kikirikí", "Muuu"], "r": "El gallo"},
                {"p": "9. Grande y podemos montar:", "o": ["Elefante", "Caballo", "Cerdo"], "r": "El caballo"},
                {"p": "10. Rosa, cola rizada, 'oink':", "o": ["Hipopótamo", "Cerdo", "Oso"], "r": "El cerdo"}
            ],
            "completar": [
                {"p": "11. Tomamos leche de la __________.", "r": "vaca"},
                {"p": "12. El __________ mueve la cola.", "r": "perro"},
                {"p": "13. El __________ ronronea.", "r": "gato"},
                {"p": "14. El __________ tiene pico plano.", "r": "pato"},
                {"p": "15. Canta al amanecer: el __________.", "r": "gallo"},
                {"p": "16. Abrigos de lana de la __________.", "r": "oveja"},
                {"p": "17. El __________ relincha.", "r": "caballo"},
                {"p": "18. Juega en lodo: el __________.", "r": "cerdo"},
                {"p": "19. Vive en madrigueras: el __________.", "r": "conejo"},
                {"p": "20. El __________ nace de huevo.", "r": "pollito"}
            ]
        }
    }
}

# --- 3. ACCESO (LOGIN) ---
CONTRASEÑA = "pao_premium"
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("🎓 Academia Pao-Spanish-Teacher")
    clave = st.text_input("Ingresa tu clave de acceso:", type="password")
    if st.button("Ingresar"):
        if clave == CONTRASEÑA:
            st.session_state.auth = True
            st.rerun()
        else: st.error("Clave incorrecta. Contacta a Pao.")
    st.stop()

# --- 4. NAVEGACIÓN (SIDEBAR) ---
with st.sidebar:
    st.title("Pao Spanish")
    st.write("¡Bienvenida!")
    menu = st.radio("Secciones:", ["Inicio", "Gramática Española", "Lecciones A1", "Contacto"])
    if st.button("Cerrar Sesión"):
        st.session_state.auth = False
        st.rerun()

# --- 5. CONTENIDO ---

if menu == "Inicio":
    st.title("¡Bienvenida a tu Academia! ✨")
    st.write("Hola, soy Pao. Aquí tienes todo el material organizado para dominar el español nivel A1.")

elif menu == "Gramática Española":
    st.title("📖 Gramática Esencial")
    c1, c2 = st.columns(2)
    gramatica_links = {
        "1. El Alfabeto": "https://www.youtube.com/watch?v=NMgN5gsvhWk",
        "2. Preguntas Comunes": "https://www.youtube.com/watch?v=gLnuqh-CUNQ",
        "3. El Género": "https://www.youtube.com/watch?v=FSqRurjGIqw",
        "4. Singular y Plural": "https://www.youtube.com/watch?v=h9pCzNZ1jTI",
        "5. Número Gramatical": "https://www.youtube.com/watch?v=VU5ylA-WjI8",
        "6. Opuestos": "https://youtu.be/fADLwhd43ac",
        "7. Artículos": "https://www.youtube.com/watch?v=rLL0NWpz6IE",
        "8. Pronombres": "https://www.youtube.com/watch?v=LorQtNAKeb4"
    }
    for i, (nombre, link) in enumerate(gramatica_links.items()):
        col = c1 if i % 2 == 0 else c2
        with col:
            st.subheader(nombre)
            st.video(link)

elif menu == "Lecciones A1":
    st.title("📚 Temario Nivel A1")
    tema_sel = st.selectbox("Elige un tema:", ["Selecciona..."] + list(DATOS_TEMAS.keys()))

    if tema_sel != "Selecciona...":
        d = DATOS_TEMAS[tema_sel]
        t1, t2, t3, t4 = st.tabs(["📺 Clase", "🎧 Dictado", "📖 Cuento + Quiz", "📄 Material"])

        with t1:
            if d.get("video"): st.video(d["video"])
            if d.get("video_estaciones"): st.divider(); st.video(d["video_estaciones"])
            else: st.info("Video de clase próximamente.")

        with t2:
            st.subheader("🎧 Practica tu oído")
            frases = d.get("frases", ["Hola", "Gracias", "Por favor"])
            if 'it' not in st.session_state: st.session_state.it = 0
            if st.session_state.it < len(frases):
                txt = frases[st.session_state.it]
                if st.button("🔊 Escuchar"):
                    gTTS(text=txt, lang='es').save("s.mp3")
                    st.audio("s.mp3")
                u = st.text_input("Escribe lo que escuchas:", key=f"d_{tema_sel}_{st.session_state.it}")
                if st.button("Comprobar"):
                    if u.lower().strip() == txt.lower().strip():
                        st.success("¡Excelente!"); st.session_state.it += 1; st.rerun()
            else:
                st.success("¡Dictado completado!")
                if st.button("Reiniciar"): st.session_state.it = 0; st.rerun()

        with t3:
            if d.get("cuento"):
                st.video(d["cuento"])
                if d.get("quiz_cuento"):
                    st.divider(); st.subheader("✍️ Ejercicios de Comprensión")
                    r_sel = {}
                    for i in d["quiz_cuento"]["seleccion"]:
                        r_sel[i["p"]] = st.radio(i["p"], i["o"], key=f"sel_{tema_sel}_{i['p']}")
                    r_comp = {}
                    for i in d["quiz_cuento"]["completar"]:
                        r_comp[i["p"]] = st.text_input(i["p"], key=f"comp_{tema_sel}_{i['p']}")
                    
                    if st.button("Verificar Respuestas"):
                        err = sum(1 for i in d["quiz_cuento"]["seleccion"] if r_sel[i["p"]] != i["r"])
                        err += sum(1 for i in d["quiz_cuento"]["completar"] if r_comp[i["p"]].lower().strip() != i["r"].lower())
                        if err == 0: st.balloons(); st.success("¡Perfecto! Todo correcto.")
                        else: st.warning(f"Tienes {err} error(es). Revisa de nuevo.")
            else: st.info("Cuento próximamente.")

        with t4:
            st.subheader("📄 Descarga tu material")
            if d.get("pdf"):
                try:
                    with open(d["pdf"], "rb") as f:
                        st.download_button(f"📥 Descargar {d['pdf']}", f, file_name=d["pdf"])
                except: st.warning(f"Archivo {d['pdf']} no encontrado en el servidor.")
            else: st.info("Material PDF próximamente.")

elif menu == "Contacto":
    st.title("📩 Soporte")
    st.write("¿Tienes dudas? Escríbeme:")
    st.write("📧 pao.mzh16@gmail.com")
