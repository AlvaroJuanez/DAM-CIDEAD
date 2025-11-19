import sys #Biblioteca standar

def dosEnOrden():
     #Obten los datos del usuario
     num1 = int(input("Primer número? \n"))
     num2 = int(input("Primer número? \n"))

     #Ordena los numero de menor a mayor
     if num1 >= num2:
         print(num2, " i ", num1)
     else:
         print(num1, " i ", num2)


dosEnOrden() #Llama a la función
