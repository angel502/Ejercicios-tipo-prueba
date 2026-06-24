from funciones import menu

tickets = []

print("-" * 60)
print("Bienvenido al software de Gestión de tickets de soporte técnico")
print("-"*60)

ejercicio_ciclo = False
while not ejercicio_ciclo:
    menu()
    try:
        opcion = int(input("Ingresa una opcion: "))
    except ValueError:
        print("Error, solo se permiten numeros o una opcion que coincida con las ya mostradas, intente nuevamente")
    else:
        if opcion > 5 or opcion < 0:
            print("Error solo se ermiten numeros del 1 al 5, intente nuevamente")
        
        if opcion == 1:
            try:
                tickets_a_registrar = int(input("Cuantos tickets desea registrar: "))
            except ValueError:
                print("Solo se permiten numeros enteros positivos intente nuevamente")
            else:

                for i in range(tickets_a_registrar):

                    validar_asunto = False
                    while not validar_asunto:
                        asunto = input(f"Ingrese el asunto de el ticket numero {i + 1}: ").strip()

                        while asunto == "" or asunto == " ":
                            print("El asunto no puede estar vacio ni compuesto por espacios intente nuevamente")
                            asunto = input("Ingrese el asunto de este ticket: ").strip()

                        impacto = input(f"Ingrese el impacto de el ticket numero {i} (el impacto es en una escala del 1 al 10): ")

                        while impacto < 1 or impacto > 10:
                            print("Error, Recuerda que el impacto debe ser un numero del 1 al 10, intente nuevamente")
                            impacto = input(f"Ingrese el impacto de el ticket numero {i} (el impacto es en una escala del 1 al 10): ")
                        
                                
                        horas_estimadas = float(input("Ingrese las horas estimadas del ticket: "))

                        while horas_estimadas < 0 or horas_estimadas.isalpha():
                            print("error, las horas estimadas deben ser un numero decimal mayor a 0, INTENTE NUEVAMENTE")
                            horas_estimadas = float(input("Ingrese las horas estimadas del ticket: "))
                        
                        escalado = False
                        while not escalado:
                            if impacto >= 7:
                                escalado = True


                    
                        validar_asunto = True


                
                
                
                




