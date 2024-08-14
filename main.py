def getConceptandDef():
    concept = input("Ingrese el concepto: ")
    definition = input("Ingrese la definicion: ")

    with open("Conceptos y definiciones.txt", 'a') as file:
        file.write(f"{concept}:{definition}\n")

def showConcepts():
    file = open("Conceptos y definiciones.txt", 'r')
    content = file.read()
    file.close()

    if content:
        print("\n-----Conceptos y definiciones almacenados-----")
        print(content)
    else:
        print("No hay conceptos almacenados.")

def showQuantity():
    file = open("Conceptos y definiciones.txt", 'r')
    content = file.read()
    file.close()

    words = content.split()
    print(f"\nCantidad de palabras almacenadas: {len(words)}")

while True:
    print("-----Menú principal-----")
    print("1. Agregar concepto")
    print("2. Mostrar conceptos ")
    print("3. Mostrar la cantidad de palabras almacenadas en el archivo")
    print("4. Salir")

    main_menu = int(input("Ingrese una opcion: "))

    if main_menu == 1:
        getConceptandDef()

    elif main_menu == 2:
        showConcepts()

    elif main_menu == 3:
        showQuantity()

    elif main_menu == 4:
        print("Saliendo del programa...")
        break

    else:
        print("Intentelo de nuevo")