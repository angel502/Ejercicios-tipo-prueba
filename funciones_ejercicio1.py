def menu():
    print("#####ADMINISTRAR CURSOS#####")
    print("1. Agregar")
    print("2. Buscar")
    print("3. Eliminar")
    print("4. Actualizar Estado")
    print("5. Mostrar Registros")
    print("6. Salir")

def leer_opcion():
    
    opcion = 0
    while opcion < 1 or opcion > 6:
        try:
            opcion = int(input("Ingresa una opcion: "))
        except ValueError:
            print("Error: no se identifico un valor numerico entero positivo")
        else:
            if opcion < 1 or opcion > 6:
                print("Error, se ingreso un numero menor a 1 o mayor a 6")

    return opcion

def agregar_curso(cursos):
    nombre = input("Ingrese elnombre del curso: ")
    try:
        cupos = int(input("Ingrese los cupos que tendra este curso: "))
        duracion_horas = float(input("Ingrese la duracion en horas que tendra este curso: "))
    except ValueError:
        print("Error: no se identifico ningun valor quecoincida con lo pedido")
        return
    if not validacion_nombre(nombre):
        print("error: Recuerda que el nombre no puede tener epacios ni estar vacio.")
    elif not validacion_cupos(cupos):
        print("Error: Recuerda que los cupos no pueden ser menor a 0 ni mayor a 40")
    elif not validacion_duracion_horas(duracion_horas):
        print("Error: Recuerda que debe ser un numero decimal mayor a 0")
    else:
        curso = {
            "nombre":nombre,
            "cupos":cupos,
            "duracion_horas":duracion_horas,
            "abierto":False
        }
        cursos.append(curso)
        print("Curso agregado correctamente")
    
def validacion_nombre(nombre):
    return nombre.strip() != ""

def validacion_cupos(cupos):
    return cupos > 0 and cupos <= 40

def validacion_duracion_horas(duracion_horas):
    return duracion_horas > 0



def buscar_curso(cursos, busqueda):
    posicion = -1
    bucle = 0
    while bucle < len(cursos) and posicion == -1:
        if cursos[bucle]['nombre'] == busqueda:
            posicion = bucle

        bucle += 1
    return posicion


def eliminar_curso(cursos):

    busqueda = input("Ingresa el nombre del curso que deseas eliminar: ")
    posicion = buscar_curso(cursos, busqueda)

    if posicion != -1:
        cursos.pop(posicion)
        print("Curso encontrado y eliminado con exito")
    else:
        print("No se a encontrado el curso que deseas eliminar")


def actualizar_cursos(cursos):
    for curso in cursos:
        if curso['cupos'] > 0:
            curso['abierto'] = True
        else:
            curso['abierto'] = False

def mostrar_cursos(cursos):
    actualizar_cursos(cursos)
    print("---Lista de cursos---")
    if len(cursos) == 0:
        print("No hay cursos disponibles")
    else:
        for i, curso in enumerate(cursos, 1):
            print(f"curso {1}: {curso['nombre']}")
            print(f"cupos disponibles: {curso['cupos']}")
            print(f"duracion del curso: {curso['duracion_horas']}")
            if curso['abierto']:
                print("Estado: Abierto")
            else:
                print("Estado: Cerrado")
            print("******************************************************")
