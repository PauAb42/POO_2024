"""
 Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
  y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones
"""

lista=[5,6,7,8,9]
cadena="Cachimba"
entero= 27
logico= True

def imprimir_tipo(variable):
    if isinstance(variable, list):
        print("La variable es una lista.")
    elif isinstance(variable, str):
        print("La variable es una cadena.")
    elif isinstance(variable, int):
        print("La variable es un entero.")
    elif isinstance(variable, bool):
        print("La variable es un booleano.")
    else:
        print("La variable es de un tipo desconocido.")

imprimir_tipo(lista)
imprimir_tipo(cadena)
imprimir_tipo(entero)
imprimir_tipo(logico)

