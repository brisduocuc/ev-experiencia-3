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
                print("2")
            case 3:
                print("3")
            case 4:
                print("4")
            case 5:
                print("5")
            case 6:
                print("Gracias por usar el sistema. Vuelva Pronto")

cinema()