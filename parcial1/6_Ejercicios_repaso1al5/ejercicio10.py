#Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron

aprobados=0
reprobados=0
contador=0

for contador in range(1,16):
    calificacion=(float(input(f"Ingrese la calificación del alumno {contador}: ")))
    if calificacion >=60:
        aprobados += 1
    else:
        reprobados +=1

print(f"Total de alumnos aprobados {aprobados}")
print(f"Total de alumnos reprobados {reprobados}")