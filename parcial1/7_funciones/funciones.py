"Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa más pequeño que cumple una función específica. La función se puede reutilizar con el simple hecho de invocarla. es decir, mandarla a llamar"

"Sintaxis"

"def nombredeMifuncion (parametros):"
"   bloque o conjunto de instrucciones"

"nombredeMifuncion(parametros)"

"Las funciones pueden ser de 4 tipos"
"1.- Función que no recibe parámetros y no regresa valor"
"2.- Función que no recibe parámetros y regresa valor"
"3.- Función que recibe parámetros y no regresa valor"
"4.- Función que recibe parámetros y regresa valor"

# Ejemplo 1: Crear una función para imprimir nombre de personas
# 1.- Función que no recibe parámetros y no regresa valor
# def nombre():
#     nombre=input("Ingresa el nombre completo: ")

# nombre()

# Ejemplo 2: sumar dos números
# 2.- Función que no recibe parámetros y regresa valor
#  def suma():
#      n1=int(input("Número #1:"))
#      n2=int(input("Número #2:"))
#      suma=n1+n2
#      print(f"{n1}+{n2}={suma}")

# # suma()

# Ejemplo 3: Sumar dos números 
# 3.- Función que recibe parámetros y no regresa valor
# def suma():
#     n1=int(input("Número #1: "))
#     n2=int(input("Número #2: "))
#     suma=n1+n2
#     return suma

# resultado_suma=suma()
# print(f"La suma es: {resultado_suma}")

# Ejemplo 4: Sumar dos números 
# 4.- Función que recibe parámetros y regresa valor
# def suma(n1,n2):
#     suma=n1+n2
#     print(f"La suma es: {suma}")

# n1=int(input("Número #1: "))
# n2=int(input("Número #2: "))
# suma(n1,n2)

#Ejemplo 6: Crear un programa que solicite a través de una función la siguiente información: Nombre del Paciente, edad, estatura, tipo de sangre. Utilizar los 4 tipos de funciones

#1.- Función que no recibe parámetros y no regresa valor

def datos1():
    nombre=input("Ingresa el nombre completo del paciente: ")
    edad=int(input("Ingresa la edad: "))
    estatura=float(input("Ingresa la estatura: "))
    tipo_sangre=input("Ingresa el tipo de sangre: ")
    print(f"Nombre del paciente: {nombre} \n Edad: {edad} \n Estatura: {estatura} \n Tipo de Sangre {tipo_sangre}")
datos1()

#2.- Función que no recibe parámetros y regresa valor
def datos2():
    nombre=input("Ingresa el nombre completo del paciente: ")
    edad=int(input("Ingresa la edad: "))
    estatura=float(input("Ingresa la estatura: "))
    tipo_sangre=input("Ingresa el tipo de sangre: ")
    return f"Nombre del paciente: {nombre} \n Edad: {edad} \n Estatura: {estatura} \n Tipo de Sangre {tipo_sangre}"
print=(datos2())

#3.- Función que recibe parámetros y no regresa valor
def datos3 (nombre,edad,estatura,sangre):
    print(f"Nombre del paciente: {nombre} \n Edad: {edad} \n Estatura: {estatura} \n Tipo de Sangre {tipo_sangre}")

nombre=input("Nombre del paciente: ")
edad=int(input("Ingresa la edad: "))
estatura=float(input("Ingresa la estatura: "))
tipo_sangre=input("Ingresa el tipo de sangre: ")
datos3(nombre,edad,estatura,tipo_sangre)

#4.- Función que recibe parámetros y regresa valor


