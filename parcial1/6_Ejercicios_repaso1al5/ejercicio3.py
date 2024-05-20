# Escribir un programa que muestre los cuadrados (un numero multiplicado por si mismo) de los 60 primeros numeros naturales. Resolverlo con while y for

#WHILE

contador=1
while contador<=60:
    cuadrado = contador**2
    print(f"El cuadrado de {contador} es: {cuadrado} ")
    contador+=1

#for

num=0
for num in range(1,61):
    cuadrado = num**2
    print(f"El cuadrado de {num} es: {cuadrado} ")