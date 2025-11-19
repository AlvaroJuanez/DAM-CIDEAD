import sys #Biblioteca standar python

def diasSemana():
    #Obtendremo el dato como argumento
    argNumero = sys.argv[1]

    #Convierte el argumento en un entero
    numero = int(argNumero)

    #Condiciona cada dia de la semana a un numero entero
    if numero == 1:
        print("Lunes")
    elif numero == 2:
        print("Martes")
    elif numero == 3:
        print("Miercoles")
    elif numero == 4:
        print("Jueves")
    elif numero == 5:
        print("Viernes")
    elif numero == 6:
        print("Sabado")
    elif numero == 7:
        print("Domingo")
    else:
        print("Error")


diasSemana()    #Llama a la función
