import sys    #Biblioteca standar      

def duplica():
    
    #Obten datos del usuario
    numDuplicado: int = 0

    numero = int(input("El doble de: "))    #Especificamos el tipo de dato
    numDuplicado = numero * 2

    #Imprime el resultado por pantalla
    print("El numero duplicado es: " + numDuplicado)

duplica()
