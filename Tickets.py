import random

tickets = {}

def generar_numero_ticket():
    return random.randint(1000, 9999)

def alta_ticket():
    nombre = input("Ingrese su nombre: ")
    sector = input("Ingrese el sector: ")
    asunto = input("Ingrese el asunto: ")
    problema = input("Describa el problema: ")

    numero_ticket = generar_numero_ticket()
    tickets[numero_ticket] = {
        'nombre': nombre,
        'sector': sector,
        'asunto': asunto,
        'problema': problema
    }

    print(f"\nTicket generado con éxito!\nNúmero de ticket: {numero_ticket}")
    print("Acuérdese de este número para futuras consultas.\n")

    while True:
        respuesta = input("¿Desea crear otro ticket? (s/n): ").lower()
        if respuesta == 's':
            alta_ticket()
            break
        elif respuesta == 'n':
            mostrar_menu()
            break
        else:
            print("Respuesta no válida. Por favor ingrese 's' o 'n'.")

def leer_ticket():
    while True:
        try:
            numero_ticket = int(input("Ingrese el número de ticket: "))
            ticket = tickets.get(numero_ticket)

            if ticket:
                print("\nInformación del Ticket:")
                print(f"Nombre: {ticket['nombre']}")
                print(f"Sector: {ticket['sector']}")
                print(f"Asunto: {ticket['asunto']}")
                print(f"Problema: {ticket['problema']}\n")
            else:
                print("Número de ticket no encontrado.\n")

            respuesta = input("¿Desea leer otro ticket? (s/n): ").lower()
            if respuesta == 's':
                continue
            elif respuesta == 'n':
                mostrar_menu()
                break
            else:
                print("Respuesta no válida. Por favor ingrese 's' o 'n'.")
        except ValueError:
            print("Por favor, ingrese un número de ticket válido.")

def salir():
    while True:
        respuesta = input("¿Está seguro que desea salir? (s/n): ").lower()
        if respuesta == 's':
            print("Saliendo del programa. ¡Adiós!")
            exit()
        elif respuesta == 'n':
            mostrar_menu()
            break
        else:
            print("Respuesta no válida. Por favor ingrese 's' o 'n'.")

def mostrar_menu():
    while True:
        print("\nMenú:")
        print("1. Alta ticket")
        print("2. Leer ticket")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            alta_ticket()
            break
        elif opcion == '2':
            leer_ticket()
            break
        elif opcion == '3':
            salir()
            break
        else:
            print("Opción no válida. Por favor seleccione una opción del 1 al 3.")

# Inicia el programa mostrando el menú principal
mostrar_menu()
