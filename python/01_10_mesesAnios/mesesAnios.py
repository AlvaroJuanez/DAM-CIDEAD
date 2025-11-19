import sys  #Biblioteca standar

def mesesAnios():
    #Declaramos variables, inicializamos para usarlo como acumuladores
    mesPost = 0
    mesAnt = 0
    anioPost = 0
    anioAnt = 0

    #Obten los datos de usuario
    mes = int(input("Mes \n"))
    anio = int(input("Año \n"))

    #Condiciona los datos que se han de usuario
    if mes > 1 and mes < 12:
        mesAnt = mes - 1
        mesPost = mes + 1

        #Imprime por pantalla el resultado
        print(f"Anterior {mesAnt}/{anio} i Posterior {mesPost}/{anio}")

    elif mes == 1:
        #Anterior
        mesAnt = mes + 11
        anioAnt = anio - 1

        #Posterior
        mesPost = mes + 1

        #Imprime por pantalla
        print(f"Anterior {mesAnt}/{anioAnt} i Posterior {mesPost}/{anio}")

    elif mes == 12:
        #Anterior
        mesAnt = mes - 1
        anioAnt = anio - 1

        #Posterior
        mesPost = mes - 11
        anioPost = anio + 1

        #Imprime por pantalla
        print(f"Anterio {mesAnt}/{anioAnt} i Posterior {mesPost}/{anioPost}")
    else:
        print("Error")


mesesAnios()    #Llama a la función
