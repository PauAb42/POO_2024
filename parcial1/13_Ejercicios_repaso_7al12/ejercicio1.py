"""
Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

 a.- Recorrer la lista y mostrarla
 b.- hacer una funcion que recorra la lista de numeros y devuelva un string
 c.- ordenarla y mostrarla
 d.- mostrar su longitud
 e.- buscar algun elemento que el usuario pida por teclado

"""
#a
numeros=[30,24,53,45,90,66,14,23]
print(f"Lista original: {numeros}" )

#b
def recorrer_lista(lista):
    return ', '.join(str(numeros) for numeros in lista)
lista_str = recorrer_lista(numeros)
print("Lista tipo str: ")
print(lista_str)

#c
numeros.sort()
print(f"Lista ordenada: {numeros}")

#d
longitud=len(numeros)
print(f"La longitud de la lista es: {longitud}")

#e
try:
 num_buscar=int(input("Introduce un número: "))
 if num_buscar in numeros:
    print(f"El número {num_buscar} se encuentra en la lista")
 else:
    print(f"El número {num_buscar} no se encuentra en la lista")
except ValueError:
   print("Ingrese un número entero válido... Vuelva a intentarlo")