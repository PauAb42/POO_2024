#Hacer un programa que solicite numeros indefinidamente hasta que se introduzca el 111 y salir del programa

while True:
    num = int(input("Ingrese un número: "))
    if num == 111:
        print("Finalizado")
        break