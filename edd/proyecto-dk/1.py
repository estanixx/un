import random
import datetime

# Guardamos un banco de preguntas: Diccionario con Preguntas, opciones, respuesta.
preguntas = [
    {
        "pregunta": "¿Cuál es la capital de Francia?",
        "opciones": {"A": "Madrid", "B": "París", "C": "Berlín", "D": "Roma"},
        "respuesta": "B"
    },
    {
        "pregunta": "¿Cuántos planetas hay en el sistema solar?",
        "opciones": {"A": "7", "B": "8", "C": "9", "D": "10"},
        "respuesta": "B"
    },
    {
        "pregunta": "¿Quién escribió 'Cien años de soledad'?",
        "opciones": {"A": "Pablo Neruda", "B": "Gabriel García Márquez", "C": "Julio Cortázar", "D": "Mario Vargas Llosa"},
        "respuesta": "B"
    },
    {
        "pregunta": "¿Cuál es el río más largo del mundo?",
        "opciones": {"A": "Nilo", "B": "Amazonas", "C": "Yangtsé", "D": "Misisipi"},
        "respuesta": "B"
    },
    {
        "pregunta": "¿En qué año llegó el hombre a la Luna?",
        "opciones": {"A": "1965", "B": "1969", "C": "1972", "D": "1980"},
        "respuesta": "B"
    },
    {
        "pregunta": "¿Cuál es el metal más conductor de electricidad?",
        "opciones": {"A": "Oro", "B": "Plata", "C": "Cobre", "D": "Aluminio"},
        "respuesta": "B"
    },
    {
        "pregunta": "¿Cuál es el país más grande del mundo por área?",
        "opciones": {"A": "China", "B": "Estados Unidos", "C": "Rusia", "D": "Canadá"},
        "respuesta": "C"
    },
    {
        "pregunta": "¿Cuál es el océano más grande del mundo?",
        "opciones": {"A": "Atlántico", "B": "Índico", "C": "Pacífico", "D": "Ártico"},
        "respuesta": "C"
    },
    {
        "pregunta": "¿Quién pintó 'La Mona Lisa'?",
        "opciones": {"A": "Vincent van Gogh", "B": "Pablo Picasso", "C": "Leonardo da Vinci", "D": "Claude Monet"},
        "respuesta": "C"
    },
    {
        "pregunta": "¿Cuál es el elemento químico con el símbolo 'O'?",
        "opciones": {"A": "Oro", "B": "Oxígeno", "C": "Osmio", "D": "Oganesón"},
        "respuesta": "B"
    },
    {
        "pregunta": "¿Cuál es la capital de Japón?",
        "opciones": {"A": "Pekín", "B": "Seúl", "C": "Tokio", "D": "Bangkok"},
        "respuesta": "C"
    },
    {
        "pregunta": "¿Quién fue el primer presidente de Estados Unidos?",
        "opciones": {"A": "Thomas Jefferson", "B": "George Washington", "C": "Abraham Lincoln", "D": "John Adams"},
        "respuesta": "B"
    },
    {
        "pregunta": "¿Cuál es el planeta más cercano al Sol?",
        "opciones": {"A": "Venus", "B": "Mercurio", "C": "Tierra", "D": "Marte"},
        "respuesta": "B"
    },
    {
        "pregunta": "¿Cuál es el idioma más hablado del mundo?",
        "opciones": {"A": "Inglés", "B": "Español", "C": "Chino Mandarín", "D": "Hindi"},
        "respuesta": "C"
    },
    {
        "pregunta": "¿Quién escribió '1984'?",
        "opciones": {"A": "Aldous Huxley", "B": "George Orwell", "C": "Ray Bradbury", "D": "Isaac Asimov"},
        "respuesta": "B"
    },
    {
        "pregunta": "¿Cuál es la montaña más alta del mundo?",
        "opciones": {"A": "K2", "B": "Monte Everest", "C": "Kilimanjaro", "D": "Aconcagua"},
        "respuesta": "B"
    },
    {
        "pregunta": "¿Cuál es el país más poblado del mundo?",
        "opciones": {"A": "India", "B": "Estados Unidos", "C": "China", "D": "Indonesia"},
        "respuesta": "C"
    },
    {
        "pregunta": "¿Quién descubrió la penicilina?",
        "opciones": {"A": "Louis Pasteur", "B": "Alexander Fleming", "C": "Marie Curie", "D": "Robert Koch"},
        "respuesta": "B"
    },
    {
        "pregunta": "¿Cuál es el hueso más largo del cuerpo humano?",
        "opciones": {"A": "Fémur", "B": "Tibia", "C": "Húmero", "D": "Radio"},
        "respuesta": "A"
    },
    {
        "pregunta": "¿Cuál es el símbolo químico del oro?",
        "opciones": {"A": "Au", "B": "Ag", "C": "Fe", "D": "Cu"},
        "respuesta": "A"
    },
    {
        "pregunta": "¿Quién escribió 'Don Quijote de la Mancha'?",
        "opciones": {"A": "Miguel de Cervantes", "B": "Federico García Lorca", "C": "Pablo Neruda", "D": "Gabriel García Márquez"},
        "respuesta": "A"
    },
    {
        "pregunta": "¿Cuál es la capital de Australia?",
        "opciones": {"A": "Sídney", "B": "Melbourne", "C": "Canberra", "D": "Brisbane"},
        "respuesta": "C"
    },
    {
        "pregunta": "¿Cuál es el animal más grande del mundo?",
        "opciones": {"A": "Elefante africano", "B": "Ballena azul", "C": "Tiburón ballena", "D": "Jirafa"},
        "respuesta": "B"
    },
    {
        "pregunta": "¿Quién fue el primer hombre en pisar la Luna?",
        "opciones": {"A": "Neil Armstrong", "B": "Buzz Aldrin", "C": "Yuri Gagarin", "D": "Michael Collins"},
        "respuesta": "A"
    },
    {
        "pregunta": "¿Cuál es el país conocido como 'La tierra del sol naciente'?",
        "opciones": {"A": "China", "B": "Corea del Sur", "C": "Japón", "D": "Tailandia"},
        "respuesta": "C"
    },
    {
        "pregunta": "¿Cuál es el planeta más grande del sistema solar?",
        "opciones": {"A": "Tierra", "B": "Júpiter", "C": "Saturno", "D": "Neptuno"},
        "respuesta": "B"
    },
    {
        "pregunta": "¿Quién pintó 'La noche estrellada'?",
        "opciones": {"A": "Pablo Picasso", "B": "Vincent van Gogh", "C": "Claude Monet", "D": "Salvador Dalí"},
        "respuesta": "B"
    },
    {
        "pregunta": "¿Cuál es la capital de Italia?",
        "opciones": {"A": "Milán", "B": "Roma", "C": "Venecia", "D": "Florencia"},
        "respuesta": "B"
    },
    {
        "pregunta": "¿Cuál es el símbolo químico del agua?",
        "opciones": {"A": "H2O", "B": "CO2", "C": "NaCl", "D": "O2"},
        "respuesta": "A"
    }
]


# Función para guardar el nombre y la fecha de nacimiento del jugador en un archivo
def guardar_jugador(nombre, fecha_nacimiento, puntaje):
    # Escribe en la última línea el nombre, la fecha y el puntaje.
    with open("jugadores.txt", "a") as archivo:
        archivo.write(f"{nombre},{fecha_nacimiento},{puntaje}\n")


# Función para cargar los jugadores desde el archivo
def cargar_jugadores():
    with open("jugadores.txt", "r") as archivo:       
        lista_jugadores = []
        for linea in archivo.readlines():
            # Por cada linea obtiene los valores separados por comas y los guarda.
            nombre, cumple, puntaje = linea.split(',')
            lista_jugadores.append((
                nombre,
                datetime.datetime.strptime(cumple, '%Y-%m-%d').date(),
                int(puntaje),
            ))
    return lista_jugadores

# Función para el juego de trivia
def juego_trivia():
    # Reorganiza las preguntas e inicializa el puntaje
    random.shuffle(preguntas)
    puntaje = 0

    # Obtiene las primeras 5 preguntas
    for pregunta in preguntas[:5]:
        # Imprime la pregunta y por cada opción, la imprime 
        print(pregunta["pregunta"])
        for letra, texto in pregunta["opciones"].items():
            print(f"{letra}. {texto}")

        respuesta = input("Tu respuesta (A, B, C o D): ").upper()

        if respuesta == pregunta["respuesta"]:
            print("¡Correcto! (+1pts)\n")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta es: {pregunta['respuesta']}\n")

    return puntaje



# Función para el minijuego de adivinar la fecha
def adivinar_fecha():
    # Obtenemos la fecha aleatoria.
    fecha_actual = datetime.date.today()
    año_actual = fecha_actual.year
    fecha_aleatoria = datetime.date(
        random.randint(año_actual - 2, año_actual),
        random.randint(1, 12),
        random.randint(1, 28)
    )

    print(f"Adivina la fecha entre el 1 de enero de {año_actual - 2} y el 31 de diciembre del {año_actual }. (formato: YYYY-MM-DD):")
    intentos = 6

    while intentos > 0:
        try:
            fecha_usuario = input("Ingresa la fecha: ")
            fecha_usuario = datetime.datetime.strptime(fecha_usuario, "%Y-%m-%d").date()

            if fecha_usuario == fecha_aleatoria:
                print("¡Correcto! Has adivinado la fecha. (+3pts)")
                return 3
            elif fecha_usuario > fecha_aleatoria:
                intentos -= 1
                print(f"Incorrecto. Te quedan {intentos} intentos.\nPista: Es ANTES")
            else:
                intentos -= 1
                print(f"Incorrecto. Te quedan {intentos} intentos.\nPista: Es DESPUËS")
        except ValueError:
            print("Formato de fecha incorrecto. Usa el formato YYYY-MM-DD.\n\n")

    print(f"Lo siento, la fecha correcta era: {fecha_aleatoria}")
    return 0




# INICIO: Instrucciones y Datos personales
print("¡Bienvenido!")
print("Instrucciones:\nResponde correctamente las preguntas de selección múltiple, ganarás un punto\npor cada acierto y obtendrás tres puntos de bonus con el minijuego 'Adivina la Fecha'.")
# Preguntamos nombre hasta que ingrese uno válido
while True:
    nombre = input("Ingresa tu nickname (4 letras):").upper()
    if len(nombre) == 4:
        break
    else:
        print('Tu nickname debe de tener 4 letras.\n\n')
# Preguntamos fecha de nacimiento hasta que la ingrese bien.
while True:
    fecha_nacimiento = input("Ingresa tu fecha de nacimiento (YYYY-MM-DD): ")
    try:
        fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
        break
        # guardar_jugador(nombre, fecha_nacimiento)
    except ValueError:
        print("Formato de fecha incorrecto. Usa el formato YYYY-MM-DD.\n\n")
        
        
        
# Empiezan los juegos, el puntaje inicial es el que gane en la trivia
print(f"\n----------Juego de Trivia----------")
puntaje = juego_trivia()

# Sumamos el puntaje al adicional que gane en la fecha.
print(f"\n----------Minijuego: Adivinar la Fecha----------")
puntaje += adivinar_fecha()

print(f"\n----------Puntajes Globales----------")

# Obtenemos los jugadores y sus puntajes, añadimos al jugador actual.
guardar_jugador(nombre, fecha_nacimiento, puntaje)
jugadores = cargar_jugadores()

# Ordenamos e imprimimos uno por uno los jugadores.
jugadores = sorted(jugadores, key=lambda x: x[2], reverse=True)
print('nick\t|\tcumpleaños\t|\tpuntaje')
for nombre, nacimiento, puntaje in jugadores:
    fecha = datetime.date.strftime(nacimiento, '%Y-%m-%d')
    print(f'{nombre}\t|\t{fecha}\t|\t{puntaje}pts')


