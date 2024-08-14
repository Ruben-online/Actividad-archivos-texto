def getConceptandDef():
    concept = input("Ingrese el concepto: ")
    definition = input("Ingrese la definicion: ")

    with open("Conceptos y definiciones.txt", 'a') as file:
        file.write(f"{concept}:{definition}\n")



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
        pass

    elif main_menu == 3:
        pass

    elif main_menu == 4:
        print("Saliendo del programa...")
        break

    else:
        print("Intentelo de nuevo")