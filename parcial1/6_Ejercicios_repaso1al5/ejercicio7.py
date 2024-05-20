#Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

num1 = int(input("Ingrese el primer número: "))
num2= int(input("Ingrese el segundo número: "))

print(f"Los números impares entre {num1} y {num2} son: ")
for numero in range (num1, num2, + 1):
    if numero % 2!= 0:
        print(numero)