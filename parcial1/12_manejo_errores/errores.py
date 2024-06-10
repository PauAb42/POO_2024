#Los errosres de ejecución en un lenguaje de programación se presentena cuando existe una anomalía dentro de la ejecución del código, lo cual provoca que se detenga la ejecución del SW. Con el control y manejo de excepciones será posible minimizar o evitar la interrupción del programa debido a una excepción 

#Ejemplo 1 Cuando una variable no se genera

# try:
#  nombre=input("Introduce el nombre completo de una persona: ")

#  if len(nombre)>0:
#     nombre_usuario="El nombre completo del usuario es: " + nombre

#  print(nombre_usuario)
# except:
#   print("Es necesario introducir un nombre de usuario... Verifica por favor")


# x=3+4
# print("El valor de x es:" +str(x))

#Ejemplo 2 Cuando se solicita un número y se ingresa otra cosa

# try:
#  numero=int(input("Ingresa un numero entero: "))

#  if numero>0:
#     print("Soy un número entero positivo")
#  elif numero==0:
#     print("Soy un número neutro")
#  else:
#     print("Soy un número entero negativo")
# except ValueError:
#    print("Introduce un valor numérico entero")

#Ejemplo 3 Generan multiples excepciones
try:
 numero=int(input("Introduce un número: "))
 print("El cuadrado del número es: "+ str (numero*numero))
except ValueError:
 print("Introduce un valor numérico entero")
except TypeError:
 print("Se debe convertir el número a entero")
else:
 print("No se presentaron errores de ejecución")
finally:
 print("Terminé la ejecución")