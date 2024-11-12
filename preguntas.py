import random  # para obtener un numero aleatorio

juegos = []
archivo = open("catalogo_juegos.txt", "r")
CANTIDAD_DE_JUEGOS = 10 #constante que sabe la cantidad de juegos disponibles

# carga de datos en lista de diccionarios
for i in range(CANTIDAD_DE_JUEGOS):
    nombre_juego = archivo.readline()
    fecha_publicacion = archivo.readline()
    publisher = archivo.readline()
    estudio = archivo.readline()
    engine = archivo.readline()
    
    # agregamos los datos a la lista de juegos
    juegos.append({
        "nombre": nombre_juego,
        "fecha_publicacion": fecha_publicacion,
        "publisher": publisher,
        "estudio": estudio,
        "engine": engine
    })


# obtener un juego random
valor_aleatorio = random.randint(0, CANTIDAD_DE_JUEGOS - 1) #obtener un valor entre 0 y CANTIDAD_DE_JUEGOS - 1
print("Tocó pregunta sobre:", juegos[valor_aleatorio]["nombre"])

#ahora preguntamos un dato random
valor_aleatorio_2 = random.randint(0, 3) #obtener un valor entre 0 y 3

if valor_aleatorio_2 == 0:
    respuesta = input("¿Cuál es la fecha de publicación de este juego? ")
    if respuesta == juegos[valor_aleatorio]["fecha_publicacion"]:
        print("Acertaste")
    else:
        print("Fallo")
elif valor_aleatorio_2 == 1:
    respuesta = input("¿Cuál es el publisher de este juego? ")
    if respuesta == juegos[valor_aleatorio]["publisher"]:
        print("Acertaste!")
    else:
        print("Fallo!")
elif valor_aleatorio_2 == 2:
    respuesta = input("¿Cuál es el estudio de este juego? ")
    if respuesta == juegos[valor_aleatorio]["estudio"]:
        print("Acertaste!")
    else:
        print("Fallo!")
elif valor_aleatorio_2 == 3:
    respuesta = input("¿Cuál es el engine de este juego? ")
    if respuesta == juegos[valor_aleatorio]["engine"]:
        print("Acertaste!")
    else:
        print("Fallo!")

