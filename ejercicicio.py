from funciones_ejercicio1 import menu,leer_opcion,agregar_curso,buscar_curso,eliminar_curso,actualizar_cursos,mostrar_cursos

cursos = []
print("-"*60)
print("BIENVENIDO AL SOFTWARE DE ADMINISTRACION DE CURSOS CORTOS")
print("-"*60)

comenzar = False
while not comenzar:
    menu()

    opcion = leer_opcion()

    if opcion == 1:
        agregar_curso(cursos)
    elif opcion == 2:
        busqueda = input("Ingrese el nombre del curso que desea buscar: ")
        
        posicion = buscar_curso(cursos, busqueda)

        if posicion != -1:
            print("Curso encontrado correctamente...")
            print(cursos[posicion])
        else:
            print("Error: no se a encontrado ningun curso con ese nombre")

    elif opcion == 3:
        eliminar_curso(cursos)
    elif opcion == 4:
        actualizar_cursos(cursos)
    elif opcion == 5:
        mostrar_cursos(cursos)
    elif opcion == 6:
        comenzar = True


print("Muchas gracias por ocupar nuestro software de administracion de cursos")

