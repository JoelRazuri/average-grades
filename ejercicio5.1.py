""" 
    Escribir un programa que permita al usuario ingresar un conjunto de notas, preguntando
    a cada paso si desea ingresar más notas, e imprimiendo el promedio correspondiente.
"""

def notas():
    # vos sabes 
    
    acumulador=0
    i=1
    condicion='si'

    while condicion=='si':
        nota=int(input("Ingrese una nota:"))
        
        acumulador=acumulador + nota
        promedio=acumulador/i
        i+=1
        
        print(f"Promedio: {promedio}")
        condicion=input("¿Desea ingresar más notas? (si/no): ")
        


notas()