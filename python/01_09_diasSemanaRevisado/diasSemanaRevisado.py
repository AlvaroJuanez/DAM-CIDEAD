import sys  #Biblioteca standar

def diasSemanaRevisado():
    #Obten los datos como argumento
    argNumero = sys.argv[1]
    numero = int(argNumero) #Convertimos a entero

    #Condiciona el numero introducido como argumento para darles un valor a los     #días de la semana.
    match numero:
        case 1:
            print("Lunes")
        case 2:
            print("Martes")
        case 3:
            print("Miercoles")
        case 4:
            print("Jueves")
        case 5:
            print("Viernes")
        case 6:
            print("Sabado")
        case 7:
            print("Domingo")
        case _:
            # EL guión bajo es equivalente a default
            print(f"El número {numero} no corresponde a un número valido (1-7)")

diasSemanaRevisado() #Llama a la función
