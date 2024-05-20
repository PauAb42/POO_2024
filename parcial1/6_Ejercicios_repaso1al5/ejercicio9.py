#Hacer un programa que solicite numeros indefinidamente hasta que se introduzca el 111 y salir del programa

while True:
    num = int(input("Ingrese un número (o 111 para salir): "))
    if num == 111:
        print("Finalizando...")
        break