
import sys #biblioteca standar

def preso():

    #Obten los datos del usuario
    nombre = input("Como te llamas?: \n")
    edad = int(input("Cuantos años tienes?: \n"))

    #Condicionales
    if edad < 18:
        print("Ten cuidado ", nombre)
    else:
        print("Tu ya puedes ir a la prisión")


preso() #Llama a la función
