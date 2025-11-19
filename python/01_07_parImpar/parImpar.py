import sys #Biblioteca standar

def parImpar():

    #Obten los datos necesarios
    numero = int(input("El numero es par o impar? \n"))

    #Verifica si el numero es par o no
    #si el residuo es 0 es un número par
    if numero % 2 == 0:
        print("El numero ", numero, " es par")
    else:
        print("El numero ", numero, " es impar")

parImpar() #Llama a la función
