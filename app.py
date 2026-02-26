import streamlit as st
from gtts import gTTS
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Pao-Spanish-Teacher Academy", page_icon="🎓", layout="wide")

# --- 2. DICCIONARIO MAESTRO COMPLETO (16 TEMAS) ---
DATOS_TEMAS = {
    "1. Saludos y Despedidas": {
        "videos": [
            "https://www.youtube.com/watch?v=hll10VBLFoQ",
            "https://www.youtube.com/watch?v=84FNM-Ni-6U",
            "https://www.youtube.com/watch?v=4txmiiR10wM"
        ],
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
        "videos": [
            "https://www.youtube.com/watch?v=nxMBJQAE2ZU",
            "https://www.youtube.com/watch?v=u_BAr1fjILU"
        ],
        "cuento": "https://www.youtube.com/watch?v=D88ftO3xU30",
        "pdf": "Minilibros Los números en español (0-100).pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. ¿En qué lugar es la carrera?", "o": ["Ciudad", "Bosque", "Playa"], "r": "Bosque"},
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
        "videos": ["https://www.youtube.com/watch?v=UF5HWnCrAU8"],
        "cuento": "https://www.youtube.com/watch?v=BDN7ST1YwcE",
        "pdf": "Minilibro Los colores en español.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. Colores primarios:", "o": ["Verde, naranja y violeta", "Amarillo, azul y rojo", "Blanco y Negro"], "r": "Amarillo, azul y rojo"},
                {"p": "2. Azul + Amarillo =", "o": ["Morado", "Verde", "Naranja"], "r": "Verde"},
                {"p": "3. Rojo + Azul =", "o": ["Violeta / Morado", "Verde", "Marrón"], "r": "Violeta / Morado"},
                {"p": "4. Rojo + Amarillo =", "o": ["Rosa", "Naranja", "Celeste"], "r": "Naranja"},
                {"p": "5. Colores neutros:", "o": ["Rojo y Azul", "Blanco y Negro", "Verde y Amarillo"], "r": "Blanco y Negro"},
                {"p": "6. Mezcla con Blanco:", "o": ["Oscurece", "Aclara (pasteles)", "Desaparece"], "r": "El color se vuelve más claro (pasteles)"},
                {"p": "7. Ausencia total de luz:", "o": ["Gris", "Negro", "Blanco"], "r": "Negro"},
                {"p": "8. Mezcla de dos primarios:", "o": ["Terceros", "Secundarios", "Básicos"], "r": "Colores Secundarios"},
                {"p": "9. Blanco + Negro =", "o": ["Marrón", "Gris", "Crema"], "r": "Gris"},
                {"p": "10. ¿Cuál es un color primario?", "o": ["Naranja", "Amarillo", "Verde"], "r": "Amarillo"}
            ],
            "completar": [
                {"p": "11. Rojo, azul y amarillo son colores __________.", "r": "primarios"},
                {"p": "12. Azul + Rojo = color __________.", "r": "violeta / morado"},
                {"p": "13. El __________ es neutro y aclara.", "r": "blanco"},
                {"p": "14. El verde es un color __________.", "r": "secundario"},
                {"p": "15. Rojo + Amarillo = color de la __________.", "r": "naranja"},
                {"p": "16. Blanco y negro son colores __________.", "r": "neutros"},
                {"p": "17. El __________ recuerda al cielo despejado.", "r": "azul"},
                {"p": "18. Mezcla de blanco y negro: __________.", "r": "gris"},
                {"p": "19. El __________ recuerda al sol.", "r": "amarillo"},
                {"p": "20. Para oscurecer uso el color __________.", "r": "negro"}
            ]
        }
    },
    "4. Días, Meses y Estaciones": {
        "videos": [
            "https://www.youtube.com/watch?v=T9fvfbMQn2I",
            "https://www.youtube.com/watch?v=mhI73gkjtwk",
            "https://www.youtube.com/watch?v=nqv12fATbOQ"
        ],
        "cuento": "https://www.youtube.com/watch?v=h1K6BKCX6g8",
        "pdf": "Minilibro Los días, los meses y las estaciones.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. ¿Primer mes del año?", "o": ["Febrero", "Enero", "Marzo"], "r": "Enero"},
                {"p": "2. ¿Estación de flores?", "o": ["Invierno", "Primavera", "Otoño"], "r": "Primavera"},
                {"p": "3. ¿Estación calurosa (playa)?", "o": ["Verano", "Invierno", "Otoño"], "r": "Verano"},
                {"p": "4. ¿Estación de hojas caídas?", "o": ["Verano", "Primavera", "Otoño"], "r": "Otoño"},
                {"p": "5. ¿Estación fría/nieve?", "o": ["Invierno", "Primavera", "Verano"], "r": "Invierno"},
                {"p": "6. ¿Mes de Navidad?", "o": ["Noviembre", "Octubre", "Diciembre"], "r": "Diciembre"},
                {"p": "7. ¿Mes más corto?", "o": ["Abril", "Febrero", "Junio"], "r": "Febrero"},
                {"p": "8. ¿Cuántas estaciones hay?", "o": ["2", "4", "6"], "r": "4"},
                {"p": "9. ¿Qué sigue a Agosto?", "o": ["Septiembre", "Julio", "Octubre"], "r": "Septiembre"},
                {"p": "10. Ropa de Verano:", "o": ["Abrigos", "Camisetas/Shorts", "Botas"], "r": "Camisetas de manga corta y pantalones cortos"}
            ],
            "completar": [
                {"p": "11. Entre marzo y mayo está __________.", "r": "Abril"},
                {"p": "12. El año tiene __________ meses.", "r": "doce"},
                {"p": "13. Mes de las flores (5): __________.", "r": "Mayo"},
                {"p": "14. Estación 'renacimiento': __________.", "r": "Primavera"},
                {"p": "15. En __________ los días son más largos.", "r": "Verano"},
                {"p": "16. Hojas secas en el __________.", "r": "Otoño"},
                {"p": "17. Guantes y gorros en el __________.", "r": "Invierno"},
                {"p": "18. El ciclo se repite cada __________ meses.", "r": "doce"},
                {"p": "19. Diciembre inicia el __________ (Norte).", "r": "Invierno"},
                {"p": "20. Mes número siete: __________.", "r": "Julio"}
            ]
        }
    },
    "5. La Hora y Rutina Diaria": {
        "videos": [
            "https://youtu.be/CbqNMMNza9w",
            "https://www.youtube.com/watch?v=xmeIIuBwxu4"
        ],
        "cuento": "https://www.youtube.com/watch?v=2BOKYde4vNM",
        "pdf": "Minilibro La Hora en Español.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. ¿A qué hora despierta Pedro?", "o": ["7:00", "8:00", "9:00"], "r": "A las 8:00"},
                {"p": "2. ¿Hora del desayuno?", "o": ["8:00", "8:30", "9:00"], "r": "A las 8:30"},
                {"p": "3. ¿Qué bebe Pedro?", "o": ["Jugo", "Café con leche", "Chocolate"], "r": "Café con leche muy caliente"},
                {"p": "4. ¿Hora de entrada a clase?", "o": ["8:30", "9:00", "10:00"], "r": "A las 9:00"},
                {"p": "5. ¿Hora del almuerzo?", "o": ["12:00", "1:15", "2:30"], "r": "A la 1:15"},
                {"p": "6. ¿Qué hace a las 5:00 PM?", "o": ["Lee", "Deporte en el parque", "Duerme"], "r": "Hacer deporte"},
                {"p": "7. ¿A qué hora cena?", "o": ["7:00", "8:00", "9:00"], "r": "A las 8:00"},
                {"p": "8. ¿Qué cena Pedro?", "o": ["Pizza", "Ensalada y pescado", "Arroz"], "r": "Ensalada de tomate y un poco de pescado"},
                {"p": "9. Actividad relajante antes de dormir:", "o": ["Ver TV", "Leer un libro", "Cocinar"], "r": "Leer un libro"},
                {"p": "10. ¿A qué hora se duerme?", "o": ["9:00", "10:00", "11:00"], "r": "A las 10:00"}
            ],
            "completar": [
                {"p": "11. Despierta a las __________ de la mañana.", "r": "8"},
                {"p": "12. Desayuna pan con __________.", "r": "mantequilla"},
                {"p": "13. El café está muy __________.", "r": "caliente"},
                {"p": "14. A las __________ entra a clase.", "r": "9"},
                {"p": "15. Come con sus __________.", "r": "amigos"},
                {"p": "16. A las 5 va al __________.", "r": "parque"},
                {"p": "17. El deporte lo hace antes de ir a su __________.", "r": "casa"},
                {"p": "18. La cena incluye un poco de __________.", "r": "pescado"},
                {"p": "19. Antes de apagar la luz le gusta __________.", "r": "leer"},
                {"p": "20. Se duerme a las __________ de la noche.", "r": "10"}
            ]
        }
    },
    "6. La Familia": {
        "videos": ["https://www.youtube.com/watch?v=4C9JiqgMt8o"],
        "pdf": "minilibro La familia en español.pdf"
    },
    "7. Profesiones (Generales y Técnicas)": {
        "videos": [
            "https://www.youtube.com/watch?v=szed1no5viA",
            "https://www.youtube.com/watch?v=jnyMcesUtsI"
        ],
        "cuento": "https://www.youtube.com/watch?v=smnwY7G3VUQ",
        "pdf": "Minilibro Las profesiones en español.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. ¿Quién enseña en la escuela?", "o": ["Policía", "Maestra", "Cocinero"], "r": "La maestra"},
                {"p": "2. Apaga incendios (uniforme rojo):", "o": ["Bombero", "Médico", "Piloto"], "r": "El bombero"},
                {"p": "3. Cura personas enfermas:", "o": ["Veterinario", "Doctor", "Fotógrafo"], "r": "El doctor"},
                {"p": "4. Cuida a los animales:", "o": ["Doctor", "Veterinario", "Enfermera"], "r": "El veterinario"},
                {"p": "5. Usa gorro blanco y prepara comida:", "o": ["Fontanero", "Cocinero", "Policía"], "r": "El cocinero"},
                {"p": "6. Dirige el tráfico y nos cuida:", "o": ["Bombero", "Policía", "Piloto"], "r": "El policía"},
                {"p": "7. Vuela el avión:", "o": ["Fotógrafo", "Piloto", "Fontanero"], "r": "El piloto"},
                {"p": "8. Ayuda al doctor con pacientes:", "o": ["Enfermera", "Maestra", "Cocinero"], "r": "La enfermera"},
                {"p": "9. Toma fotos importantes:", "o": ["Fotógrafo", "Veterinario", "Bombero"], "r": "El fotógrafo"},
                {"p": "10. Arregla tuberías de agua:", "o": ["Policía", "Fontanero", "Doctor"], "r": "El fontanero"}
            ],
            "completar": [
                {"p": "11. La __________ escribe en la pizarra.", "r": "maestra"},
                {"p": "12. El __________ usa una manguera.", "r": "bombero"},
                {"p": "13. Si tengo fiebre voy al __________.", "r": "doctor"},
                {"p": "14. El __________ cuida a mi perrito.", "r": "veterinario"},
                {"p": "15. El __________ cocina en el restaurante.", "r": "cocinero"},
                {"p": "16. El __________ lleva una placa.", "r": "policía"},
                {"p": "17. El __________ está en la cabina del avión.", "r": "piloto"},
                {"p": "18. La __________ cura una herida.", "r": "enfermera"},
                {"p": "19. El __________ usa una cámara.", "r": "fotógrafo"},
                {"p": "20. El __________ arregla el lavabo.", "r": "fontanero"}
            ]
        }
    },
    "8. Nacionalidad y Países": {
        "videos": ["https://www.youtube.com/watch?v=T2HVf4YqHZY"],
        "pdf": "Minilibros Los países y nacionalidades en español.pdf"
    },
    "9. Partes del Cuerpo": {
        "videos": ["https://www.youtube.com/watch?v=OfX0hCFCdeA"],
        "cuento": "https://www.youtube.com/watch?v=JyedWS0rQ5s",
        "pdf": "Minilibro Las partes del cuerpo en español.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. Para ver colores y formas:", "o": ["Oídos", "Ojos", "Nariz"], "r": "Los ojos"},
                {"p": "2. Para caminar y correr:", "o": ["Manos", "Brazos", "Piernas"], "r": "Las piernas"},
                {"p": "3. Para escuchar sonidos:", "o": ["Ojos", "Orejas / oídos", "Pies"], "r": "Los orejas / oídos"},
                {"p": "4. Para agarrar objetos:", "o": ["Pies", "Manos", "Hombros"], "r": "Las manos"},
                {"p": "5. ¿Dónde está el cerebro?", "o": ["Pecho", "Cabeza", "Estómago"], "r": "En la cabeza"},
                {"p": "6. Para oler flores:", "o": ["Boca", "Nariz", "Cuello"], "r": "La nariz"},
                {"p": "7. Articulación del brazo:", "o": ["Tobillo", "Rodilla", "Codo"], "r": "El codo"},
                {"p": "8. Los dedos con uñas están en:", "o": ["Manos", "Pies", "Manos y Pies"], "r": "En las manos y en los pies"},
                {"p": "9. Protege corazón y pulmones:", "o": ["Abdomen", "Torso", "Espalda"], "r": "El torso / caja torácica"},
                {"p": "10. Une cabeza y cuerpo:", "o": ["Hombro", "Cuello", "Cintura"], "r": "El cuello"}
            ],
            "completar": [
                {"p": "11. Dedo más pequeño: el __________.", "r": "meñique"},
                {"p": "12. Uso la __________ para hablar.", "r": "boca"},
                {"p": "13. Doblo la pierna con la __________.", "r": "rodilla"},
                {"p": "14. Sostienen el cuerpo al caminar: los __________.", "r": "pies"},
                {"p": "15. En la cara hay nariz, ojos y __________.", "r": "boca"},
                {"p": "16. Están al final de los brazos: las __________.", "r": "manos"},
                {"p": "17. Nos mantiene rectos: la __________.", "r": "espalda"},
                {"p": "18. Huelo perfume con la __________.", "r": "nariz"},
                {"p": "19. El tacto está en la __________.", "r": "piel"},
                {"p": "20. Al final de las piernas: los __________.", "r": "pies"}
            ]
        }
    },
    "10. La Ropa y Vestimenta": {
        "videos": ["https://www.youtube.com/watch?v=nOisiL-Pyak"],
        "pdf": "Minilibro La ropa y la vestimenta en español.pdf"
    },
    "11. Comida y Bebidas": {
        "videos": [
            "https://www.youtube.com/watch?v=9iPhcCg64j8",
            "https://www.youtube.com/watch?v=LgpwYTK9RTc"
        ],
        "cuento": "https://www.youtube.com/watch?v=SyraFpsEFls",
        "pdf": "Minilibro Comidas y Bebidas en Español..pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. Desayuno de Mateo:", "o": ["Galletas", "Pan tostado", "Frutas"], "r": "Pan tostado"},
                {"p": "2. Bebida caliente de Mateo:", "o": ["Chocolate", "Té", "Café"], "r": "Café"},
                {"p": "3. Color de la taza:", "o": ["Roja", "Blanca", "Azul"], "r": "Azul"},
                {"p": "4. Color de la leche:", "o": ["Amarilla", "Blanca", "Crema"], "r": "Blanca"},
                {"p": "5. Elena prefiere comida:", "o": ["Rápida", "Sana", "Dulces"], "r": "Comida sana"},
                {"p": "6. Frutas de Elena:", "o": ["Pera y uva", "Manzana y banana", "Sandía y melón"], "r": "Manzana y banana"},
                {"p": "7. ¿A qué hora cocina Mateo?", "o": ["Noche", "Mediodía", "Mañana"], "r": "Al mediodía"},
                {"p": "8. ¿Qué usa para cocinar el almuerzo?", "o": ["Sartén", "Olla grande", "Horno"], "r": "Una olla grande"},
                {"p": "9. ¿Qué prepara en la olla?", "o": ["Sopa", "Arroz blanco", "Espaguetis"], "r": "Arroz blanco"},
                {"p": "10. El arroz está:", "o": ["Picante", "Delicioso", "Salado"], "r": "Delicioso"}
            ],
            "completar": [
                {"p": "11. Desayuno: pan __________.", "r": "tostado"},
                {"p": "12. El café está muy __________.", "r": "caliente"},
                {"p": "13. Hermana de Mateo: __________.", "r": "Elena"},
                {"p": "14. Elena elige comida __________.", "r": "sana"},
                {"p": "15. Come una __________ roja.", "r": "manzana"},
                {"p": "16. Come una __________ amarilla.", "r": "banana"},
                {"p": "17. Cocina al __________.", "r": "mediodía"},
                {"p": "18. Usa una __________ grande.", "r": "olla"},
                {"p": "19. El arroz es de color __________.", "r": "blanco"},
                {"p": "20. El arroz resultó muy __________.", "r": "delicioso"}
            ]
        }
    },
    "12. La Casa": {
        "videos": ["https://youtu.be/2Wz5yyw80gs"],
        "cuento": "https://www.youtube.com/watch?v=yHd_5EQuIN0",
        "pdf": "Minilibro La casa y sus partes en español.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. Color de la casa:", "o": ["Verde", "Amarilla", "Blanca"], "r": "Amarilla"},
                {"p": "2. ¿Cómo es la cocina?", "o": ["Pequeña", "Grande y moderna", "Oscura"], "r": "Grande y moderna"},
                {"p": "3. Material de la mesa:", "o": ["Plástico", "Madera", "Vidrio"], "r": "De madera"},
                {"p": "4. Objeto azul en el dormitorio:", "o": ["Silla", "Cama", "Cortina"], "r": "Una cama"},
                {"p": "5. ¿Cómo es el baño?", "o": ["Grande", "Pequeño, limpio y blanco", "Ruidoso"], "r": "Pequeño, limpio y de color blanco"},
                {"p": "6. ¿Qué hay en el jardín?", "o": ["Solo pasto", "Flores y un árbol alto", "Una piscina"], "r": "Muchas flores de colores y un árbol alto"},
                {"p": "7. ¿Dónde está la cama azul?", "o": ["Cocina", "Dormitorio", "Baño"], "r": "En el dormitorio"},
                {"p": "8. Característica del árbol:", "o": ["Pequeño", "Alto", "Frutal"], "r": "Alto"},
                {"p": "9. Color del baño limpio:", "o": ["Amarillo", "Blanco", "Gris"], "r": "Blanco"},
                {"p": "10. Diseño de la cocina:", "o": ["Tradicional", "Moderno", "Rústico"], "r": "Moderno"}
            ],
            "completar": [
                {"p": "11. La casa es de color __________.", "r": "amarillo"},
                {"p": "12. La cocina es __________ y moderna.", "r": "grande"},
                {"p": "13. La mesa es de __________.", "r": "madera"},
                {"p": "14. Cómoda __________ de color azul.", "r": "cama"},
                {"p": "15. El baño es de color __________.", "r": "blanco"},
                {"p": "16. El árbol es muy __________.", "r": "alto"},
                {"p": "17. El jardín tiene muchas __________.", "r": "flores"},
                {"p": "18. Veo afuera por la __________.", "r": "ventana"},
                {"p": "19. El baño es __________, pero limpio.", "r": "pequeño"},
                {"p": "20. Lugar más moderno: la __________.", "r": "cocina"}
            ]
        }
    },
    "13. Objetos Cotidianos": {
        "videos": [],
        "pdf": "Minilibros Los objetos cotidianos en español.pdf"
    },
    "14. Medios de Transporte": {
        "videos": [],
        "cuento": "https://www.youtube.com/watch?v=9Lv9Ih46MxA",
        "pdf": "Minilibros Los medios de transporte en español.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. Color del carro:", "o": ["Azul", "Rojo", "Blanco"], "r": "Rojo"},
                {"p": "2. Vuela y es blanco:", "o": ["Tren", "Avión", "Carro"], "r": "El avión"},
                {"p": "3. Azul con 2 ruedas:", "o": ["Carro", "Moto", "Tren"], "r": "La moto"},
                {"p": "4. Color del tren:", "o": ["Blanco", "Gris", "Rojo"], "r": "Gris"},
                {"p": "5. Tiene alas y es blanco:", "o": ["Moto", "Avión", "Tren"], "r": "El avión"},
                {"p": "6. Rojo con 4 ruedas:", "o": ["Carro", "Avión", "Moto"], "r": "El carro"},
                {"p": "7. Sonido fuerte, gris y largo:", "o": ["Avión", "Tren", "Carro"], "r": "El tren"},
                {"p": "8. Necesita casco (moto):", "o": ["Gris", "Azul", "Rojo"], "r": "Azul (La moto)"},
                {"p": "9. Despega hacia las nubes:", "o": ["Tren", "Avión", "Carro"], "r": "El avión"},
                {"p": "10. Si es rojo es un:", "o": ["Moto", "Carro", "Tren"], "r": "El carro"}
            ],
            "completar": [
                {"p": "11. El cuento muestra un __________ rojo.", "r": "carro / coche"},
                {"p": "12. La moto es de color __________.", "r": "azul"},
                {"p": "13. El __________ corre sobre rieles.", "r": "tren"},
                {"p": "14. El avión es de color __________.", "r": "blanco"},
                {"p": "15. Carro rojo de __________ ruedas.", "r": "cuatro"},
                {"p": "16. La __________ tiene 2 ruedas.", "r": "moto"},
                {"p": "17. El tren es de color __________.", "r": "gris"},
                {"p": "18. El __________ cruza el cielo.", "r": "avión"},
                {"p": "19. Carro rojo y moto __________.", "r": "azul"},
                {"p": "20. Transporte más largo: __________.", "r": "tren"}
            ]
        }
    },
    "15. Los Lugares de la Ciudad": {
        "videos": [
            "https://www.youtube.com/watch?v=DziT1MJLmk4",
            "https://www.youtube.com/watch?v=Ss_2il1-Sm8"
        ],
        "pdf": "Minilibro Los lugares en español.pdf"
    },
    "16. Los Animales (Domésticos y Salvajes)": {
        "videos": ["https://www.youtube.com/watch?v=G2n_FA_vhPU"],
        "cuento": "https://www.youtube.com/watch?v=WsPVCwvWsiw",
        "pdf": "Minilibro Los animales domésticos en español.pdf",
        "quiz_cuento": {
            "seleccion": [
                {"p": "1. Dice 'muuu' y da leche:", "o": ["Perro", "Vaca", "Gato"], "r": "La vaca"},
                {"p": "2. Dice 'guau', mejor amigo:", "o": ["Pato", "Perro", "Cerdo"], "r": "El perro"},
                {"p": "3. Dice 'miau' y caza ratones:", "o": ["Conejo", "Gato", "Pollito"], "r": "El gato"},
                {"p": "4. Dice 'cuac' y nada:", "o": ["Pato", "Gallo", "Oveja"], "r": "El pato"},
                {"p": "5. Pollito dice:", "o": ["Miau", "Pío pío", "Oink"], "r": "El pollito"},
                {"p": "6. Orejas largas y zanahorias:", "o": ["Perro", "Conejo", "Caballo"], "r": "El conejo"},
                {"p": "7. Da lana y dice 'beee':", "o": ["Cabra", "Oveja", "Vaca"], "r": "La oveja"},
                {"p": "8. Gallo dice:", "o": ["Cuac", "Kikirikí", "Muuu"], "r": "El gallo"},
                {"p": "9. Grande, podemos montar:", "o": ["Elefante", "Caballo", "Cerdo"], "r": "El caballo"},
                {"p": "10. Rosa, cola rizada, 'oink':", "o": ["Hipopótamo", "Cerdo", "Oso"], "r": "El cerdo"}
            ],
            "completar": [
                {"p": "11. Tomamos leche de la __________.", "r": "vaca"},
                {"p": "12. El __________ mueve la cola.", "r": "perro"},
                {"p": "13. El __________ ronronea.", "r": "gato"},
                {"p": "14. El __________ tiene pico plano.", "r": "pato"},
                {"p": "15. Canta al amanecer: el __________.", "r": "gallo"},
                {"p": "16. La __________ nos da lana.", "r": "oveja"},
                {"p": "17. El __________ relincha.", "r": "caballo"},
                {"p": "18. Juega en el lodo: el __________.", "r": "cerdo"},
                {"p": "19. El __________ vive en madrigueras.", "r": "conejo"},
                {"p": "20. El __________ nace de un huevo.", "r": "pollito"}
            ]
        }
    }
}

# --- 3. SISTEMA DE ACCESO ---
CONTRASEÑA = "pao_premium"
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("🎓 Academia Pao-Spanish-Teacher")
    clave = st.text_input("Ingresa tu clave de acceso:", type="password")
    if st.button("Ingresar"):
        if clave == CONTRASEÑA:
            st.session_state.auth = True
            st.rerun()
        else: st.error("Clave incorrecta.")
    st.stop()

# --- 4. INTERFAZ ---
with st.sidebar:
    st.title("Menú Académico")
    menu = st.radio("Secciones:", ["Inicio", "Gramática", "Lecciones A1", "Soporte"])
    if st.button("Cerrar Sesión"):
        st.session_state.auth = False
        st.rerun()

# --- 5. LÓGICA DE CONTENIDO ---

if menu == "Inicio":
    st.title("¡Bienvenida a tu Academia! ✨")
    st.write("Explora los temas y usa los videos interactivos para mejorar tu español.")

elif menu == "Gramática":
    st.title("📖 Gramática Esencial")
    gram_vids = {
        "Alfabeto": "https://www.youtube.com/watch?v=NMgN5gsvhWk",
        "Preguntas": "https://www.youtube.com/watch?v=gLnuqh-CUNQ",
        "Género": "https://www.youtube.com/watch?v=FSqRurjGIqw",
        "Singular/Plural": "https://www.youtube.com/watch?v=h9pCzNZ1jTI",
        "Artículos": "https://www.youtube.com/watch?v=rLL0NWpz6IE",
        "Pronombres": "https://www.youtube.com/watch?v=LorQtNAKeb4"
    }
    c1, c2 = st.columns(2)
    for i, (nom, link) in enumerate(gram_vids.items()):
        with (c1 if i % 2 == 0 else c2):
            st.subheader(nom); st.video(link)

elif menu == "Lecciones A1":
    st.title("📚 Temario A1")
    tema_sel = st.selectbox("Elige un tema:", ["Selecciona..."] + list(DATOS_TEMAS.keys()))

    if tema_sel != "Selecciona...":
        d = DATOS_TEMAS[tema_sel]
        t1, t2, t3, t4 = st.tabs(["📺 Clases", "🎧 Dictado", "📖 Cuento + Ejercicios", "📄 Material"])

        with t1:
            st.subheader(f"Videos de {tema_sel}")
            if d.get("videos"):
                for idx, v_url in enumerate(d["videos"]):
                    st.write(f"**Video Parte {idx + 1}:**")
                    st.video(v_url)
            else: st.info("Videos disponibles próximamente.")

        with t2:
            st.subheader("🎧 Practica tu Oído")
            frases = d.get("frases", ["Hola", "Gracias"])
            if 'it' not in st.session_state: st.session_state.it = 0
            if st.session_state.it < len(frases):
                f_actual = frases[st.session_state.it]
                if st.button("🔊 Escuchar Palabra"):
                    gTTS(text=f_actual, lang='es').save("s.mp3")
                    st.audio("s.mp3")
                resp = st.text_input("¿Qué escuchaste?", key=f"d_{tema_sel}_{st.session_state.it}")
                if st.button("Verificar"):
                    if resp.lower().strip() == f_actual.lower().strip():
                        st.success("¡Muy bien!"); st.session_state.it += 1; st.rerun()
                    else: st.error("Intenta de nuevo.")
            else: 
                st.success("¡Dictado terminado!")
                if st.button("Reiniciar"): st.session_state.it = 0; st.rerun()

        with t3:
            if d.get("cuento"):
                st.video(d["cuento"])
                if d.get("quiz_cuento"):
                    st.divider(); st.subheader("📝 Evaluación interactiva")
                    # Selección
                    res_sel = {}
                    for q in d["quiz_cuento"]["seleccion"]:
                        res_sel[q["p"]] = st.radio(q["p"], q["o"], key=f"s_{tema_sel}_{q['p']}")
                    # Completación
                    res_comp = {}
                    for q in d["quiz_cuento"]["completar"]:
                        res_comp[q["p"]] = st.text_input(q["p"], key=f"c_{tema_sel}_{q['p']}")
                    
                    if st.button("Corregir Ejercicios"):
                        mal = sum(1 for q in d["quiz_cuento"]["seleccion"] if res_sel[q["p"]] != q["r"])
                        mal += sum(1 for q in d["quiz_cuento"]["completar"] if res_comp[q["p"]].lower().strip() != q["r"].lower())
                        if mal == 0: st.balloons(); st.success("¡Felicidades! 20/20 correctas.")
                        else: st.warning(f"Tienes {mal} error(es). ¡Tú puedes, revisa de nuevo!")
            else: st.info("Cuento próximamente.")

        with t4:
            if d.get("pdf"):
                try:
                    with open(d["pdf"], "rb") as f:
                        st.download_button(f"📥 Descargar {d['pdf']}", f, file_name=d["pdf"])
                except: st.error("PDF no encontrado. Contacta a Pao.")
            else: st.info("Material PDF en preparación.")

elif menu == "Soporte":
    st.title("📩 Contacto")
    st.write("Escríbeme para cualquier duda: pao.mzh16@gmail.com")
