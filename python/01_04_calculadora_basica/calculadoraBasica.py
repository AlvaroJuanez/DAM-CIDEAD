import sys #Biblioteca standar

def calculadoraBasica():

    #Obtenemos los datos necesarios
    operador1 = int(input("Primer operador: "))
    operador2 = int(input("Segundo operador: "))

    #Operaciones matematicas básicas
    suma = operador1 + operador2
    resta = operador1 - operador2
    multiplicacion = operador1 * operador2
    division = operador1 / operador2

    #Imprimer los resultados por pantalla
    #la concatenacion se la realiza con la (,) sin son datos numericos
    print(operador1, " + ", operador2, " = ", suma)
    print(operador1, " - ", operador2, " = ", resta)
    print(operador1, " * ", operador2, " = ", multiplicacion)
    print(operador1, " / ", operador2, " = ", division)


calculadoraBasica() #Llama a la función
