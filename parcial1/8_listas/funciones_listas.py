paises=["Mexico","USA", "Brasil","Japon"]
numeros=[23,100,3.1416,0.100]
varios=["Hola",True,100,10.22]

#Ordenar la lista
# print(paises)
# paises.sort()
# print(paises)

# print(numeros)
# numeros.sort()
# print(numeros)
#Solo se puede ordenar una lsita que contenga los mismos tipos de datos

#Agregar elementos a la lista
# print(numeros)
# numeros.insert(len(numeros),100)
# print(numeros)
# numeros.append(100)

#Eliminar elementos a la lista
print(numeros)
numeros.pop(2)
print(numeros)
numeros.remove(100)

#Buscar en una lista dentro de una lista un dato o un valor 

encontrar="Brasil" in paises
print(encontrar)

#Dar la vuelta 
print(varios)
varios.reverse()
print(varios)

#Unir listas
print(paises)
paises.extend(numeros)
print(paises)

#Vaciar una lista
print(varios)
varios.clear()
print(varios)
