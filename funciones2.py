def menu():
    print("#####SEGUIMIENTO DE CITAS#####")
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
            opcion = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Error: no se identifico una variable que coincida con la opcion")
        else:
            if opcion < 1 or opcion > 6:
                print("Error, ingresa una opcion valida (del 1 al 6)")
            
    return opcion

def validar_paciente(paciente):
    return paciente.strip() != ""

def validar_urgencia(urgencia):
    return urgencia >= 1 and  urgencia <= 10

def validar_costo(costo):
    return costo > 0



def agregar_cita(citas):
    paciente = input("Ingrese el nombre del paciente que desea ingresar: ")

    try:
        urgencia = int(input("Ingrese el grado de urgencia de el paciente (del 1 al 10): "))
        costo = int(input("Ingrese el costo de la atencion del paciente: "))
    except ValueError:
        print("Error: no se identifico el valor numerico ingresado")
        return
    if not validar_paciente(paciente):
        print("Error: Recuerda que el nombre del paciente no debe contener espacios ni estar vacio")
    elif not validar_urgencia(urgencia):
        print("Error: Recuerda que la urgencia debe ser un numero entero positivo entre 1 y 10 ")
    elif not validar_costo(costo):
        print("Error: recuerde que el costo de la cita debe ser un numero mayor a 0 (son validos los decimales)")
    else:
        cita = {
            "paciente":paciente,
            "urgencia":urgencia,
            "costo":costo,
            "prioritaria":False
        }
        citas.append(cita)
        print("Cita agregada correctamente")


def buscar_cita(citas, busqueda):
    posicion = -1
    bucle = 0
    while bucle < len(citas) and posicion == -1:
        if citas[bucle]['paciente'] == busqueda:
            posicion = bucle
        bucle += 1

    return posicion



def eliminar_cita(citas):
    busqueda = input("Ingrese el nombre del paciente el cual quieres cancelar la cita: ")
    posicion = buscar_cita(citas, busqueda)

    if posicion != -1:
        citas.pop(posicion)
        print("Cita eliminada correctamente")
    else:
        print("No se encontro la cita la cual quieres eliminar, preocura que el nombre coincida con ek agendado en la cita")

def actualizar_estado(citas):
    if citas == []:
        print("No hay citas agendadas para actualizar")
    else:
        for cita in citas:
            if cita['urgencia'] >= 8:
                cita['prioritaria'] = True
            else:
                cita['prioritaria'] = False



def mostrar_citas(citas):
    if citas == []:
        print("No hay citas agendadas para mostrar, agende una y se mostrara posteriormente")
    else:
        for i, cita in enumerate(citas):
            print(f"cita numero {i}")
            print(f"Paciente: {cita['paciente']}")
            print(f"urgencia: {cita['urgencia']}")
            print(f"Costo: {cita['costo']}")
            if cita['prioritaria'] == True:
                print("Es Prioritario") 
            else:
                print("No es prioritario")

