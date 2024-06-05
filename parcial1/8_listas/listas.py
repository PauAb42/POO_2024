"""

List (Array)
Son colecciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un índice numérico

NOTA: Sus valores si son modificables

La lista es una colección ordenada y modificable. 
Permite miembros duplicados

"""

#Ejemplo 1: Crear un lista de números e imprimir el contenido

# numeros=[23,34]
# print(numeros)

#Recorrer la lista con ciclo for
# for i in numeros:
#     print(i)

#Recorrer la lista con ciclo while
# i=0
# while i<=len(numeros)-1:
#     print(numeros[i])
#     i+=1

#Ejemplo 2: Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra

palabras=["naranja","utd","amreica ","azul"]
palabra_buscar=input("Ingresa la palabra a buscar: ")


for i in palabras:
    if i==palabra_buscar:
        print(f"Se encontró la palabra a buscar en la posición {palabras.index}")
    else:
        print()