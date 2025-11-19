import sys #Biblioteca estandar 
def adinivaNombre():

    #Obten datos del usuario
    adinivaNumero= int(input("El número pensado es: ")) #tipo de variable
    print(adinivaNumero)
    
    #Multiplicalo * 3
    numero: int = 0 #Especificamos que es un int
    numero = adinivaNumero * 3 #realiza una operación matematica
    print("Multiplicado por 3: " , numero) #imprime el resultado por pantalla

    #sumale + 6
    numero = numero + 6
    print("Sumados 6: " , numero)

    #Divido entre 3
    numero = numero / 3
    print("Divido entre 3: ", numero)

    #Restamos el numero pensado
    numero = numero - adinivaNumero
    print("a que el resultado es 2: ", numero)


adinivaNombre() #llama a la función sin esta linea no muestra nada por pantalla
