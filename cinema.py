# Función que mostrará el menú en la consola, sin recibir ni retornar nada
def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar películas")
    print("6. Salir")
    print("=====================================")

# Función que valida la opción seleccionada, sin recibir, retornando número validado
def seleccionar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción (1/2/3/4/5/6): "))
            if opcion in (1,2,3,4,5,6):
                break
        except ValueError:
            print("Ha ingresado una opción inválida, vuelva a intentarlo")
    return opcion

# Función agregar película, recibe lista
def agregar_pelicula(pelicula):
    # Variables
    titulo = validación_titulo()
    duracion = validación_duracion()
    calificacion = validación_calificacion()

    # Condiciones de aceptación
    mensajes_condiciones = []

    if titulo == "":
        mensajes_condiciones.append("El título no puede estar vacío")
    
    if titulo != "" and titulo.strip() == "":
        mensajes_condiciones.append("El título no puede ser solo espacios en blanco")
    
    if duracion <= 0:
        mensajes_condiciones.append("La duración debe ser mayor a cero")
    
    if calificacion <= 0.0  or calificacion >= 10.0:
        mensajes_condiciones.append("La calificación debe ser un número decimal entre 0.0 y 10.0")
    
    # Validamos si cumplen con los criterios
    if len(mensajes_condiciones) == 0:
        pelicula["titulo"] = titulo
        pelicula["duracion"] = duracion
        pelicula["calificacion"] = calificacion

        print("Se ha registrado correctamente la película:")
        print(f"Título: {pelicula.get("titulo")}")
        print(f"Duración: {pelicula.get("duracion")}")
        print(f"Calificación: {pelicula.get("calificacion")}")

        return pelicula
    else:
        for mensaje in mensajes_condiciones:
            print(mensaje)
        print("No se ha podido registrar la película")
        return None


# Validación título
def validación_titulo():
    while True:
        titulo = input("Ingrese el nombre de la película a agregar: ")
        if titulo.isdigit():
            print("Debe ingresar un nombre valido")
        else:
            break
    return titulo
# Validación duración
def validación_duracion():
    while True:
        try:
            duracion = int(input("Ingrese la duración de la película: "))
            if isinstance(duracion, int):
                break
        except ValueError:
            print("Debe ingresar un número válido")
    return duracion
# Validación Calificación
def validación_calificacion():
    while True:
        try:
            calificacion = float(input("Ingrese la calificación de la película: "))
            if isinstance(calificacion, float):
                break
        except ValueError:
            print("Debe ingresar un número válido")
    return calificacion

# Función Buscar película
def buscar_pelicula(lista_pelicula, titulo):
    posicion = -1
    for pelicula in lista_pelicula:
        posicion += 1
        if pelicula.get("titulo") == titulo:
            break
    if posicion < 0:
        return -1
    else:
        return posicion


# Función Eliminar película
def eliminar_pelicula(lista_pelicula, posicion):
    lista_pelicula.pop(posicion)
    print("Se eliminó la película")

# Función Actualizar dispónibilidad
def actualizar_disponibilidad(lista_pelicula):
    for pelicula in lista_pelicula:
        if pelicula.get("calificacion") >= 7.0:
            pelicula["disponible"] = True
        else:
            pelicula["disponible"] = False

# Función Mostrar películas
def mostrar_peliculas(lista_pelicula):
    print("=== LISTA DE PELICULAS ===")
    if len(lista_pelicula) == 0:
        print("No hay películas para mostrar.")
    for pelicula in lista_pelicula:
        print(f"Título: {pelicula.get("titulo")}")
        print(f"Duración: {pelicula.get("duracion")}")
        print(f"Calificación: {pelicula.get("calificacion")}")
        if pelicula.get("disponible"):
            print(f"Estado: DISPONIBLE")
        else:
            print("Estado: NO RECOMENDAD")
        print("*********************************************\n")


# Sistema cinema
def cinema():
    # Inicializamos variable opcion
    opcion = 0
    lista_peliculas = []

    while opcion != 6:
        mostrar_menu()
        opcion = seleccionar_opcion()

        # Inicializamos variable película
        # titulo -> Ni vacío ni espacios en blanco
        # duracion -> Entero mayor a cero
        # calificacion -> Decimal entre 0.0 y 10.0 incluidos
        # disponible -> el sistema lo asigna
        pelicula_default = {
            "titulo": "",
            "duracion": 0,
            "calificacion": 0.0,
            "disponible": False
        }

        # Opciones
        match opcion:
            case 1:
                pelicula = agregar_pelicula(pelicula_default)
                if pelicula is not None:
                    lista_peliculas.append(pelicula)
            case 2:
                titulo = input("Ingrese el título a buscar: ")
                posicion = buscar_pelicula(lista_peliculas, titulo)
                if posicion < 0:
                    print("Película no encontrada")
                else:
                    print("Película encontrada")
                    print(f"Título: {lista_peliculas[posicion].get("titulo")}")
                    print(f"Duración: {lista_peliculas[posicion].get("duracion")}")
                    print(f"Calificación: {lista_peliculas[posicion].get("calificacion")}")
            case 3:
                titulo = input("Ingrese el título a buscar: ")
                posicion = buscar_pelicula(lista_peliculas, titulo)
                if posicion < 0:
                    print(f"La película {titulo} no se encuentra registrada.")
                else:
                    eliminar_pelicula(lista_peliculas, posicion)
            case 4:
                if len(lista_peliculas) == 0:
                    print("No hay peliculas para actualizar")
                else:
                    actualizar_disponibilidad(lista_peliculas)
                    print("Se han actualizado todas las películas correctamente")
            case 5:
                actualizar_disponibilidad(lista_peliculas)
                mostrar_peliculas(lista_peliculas)
            case 6:
                print("Gracias por usar el sistema. Vuelva Pronto")

cinema()