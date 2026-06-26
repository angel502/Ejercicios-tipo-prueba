from funciones2 import menu,leer_opcion,agregar_cita,buscar_cita,eliminar_cita,actualizar_estado,mostrar_citas

citas = []

print("-"*60)
print("   BIENVENIDO AL SOFTWARE DE SEGUIMIENTO DE CITAS MEDICAS")
print("-"*60)

comenzar = False
while not comenzar:
    menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_cita(citas)
    elif opcion == 2:
        busqueda = input("Ingrese el nombre del paciente que desea buscar: ")

        posicion = buscar_cita(citas, busqueda)

        if posicion !=-1:
            print("cita encontrada correctamente")
            print(citas[posicion])
        else:
            print("No se encontro la cita que buscas, el nombre no coincide con ninguna cita agendada")

    elif opcion == 3:
        eliminar_cita(citas)
    elif opcion == 4:
        actualizar_estado(citas)
    elif opcion == 5:
        mostrar_citas(citas)
    elif opcion == 6:
        comenzar = True

print("MUCHAS GRACIAS POR UTILIZAR NUESTRO SOFTWARE")
