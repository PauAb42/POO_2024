"""
Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
el contenido de la lista en mayúsculas

"""

palabras = []

if not palabras:
    print("Añada palabras o frases a la lista: ")

    while True:
        entrada = input("Introduce una palabra o frase (o escribe 'salir' para terminar): ")
        if entrada.lower() == 'salir':
            break
        palabras.append(entrada)

print("\nContenido de la lista en mayúsculas:")
for palabra in palabras:
    print(palabra.upper())