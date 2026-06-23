# Variable película
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

# Sistema cinema
def cinema():
    mostrar_menu()
    opcion = seleccionar_opcion()

    # Opciones
    match opcion:
        case 1:
            print("1")
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

print(seleccionar_opcion())