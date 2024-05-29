
contador=0

nombre=str(input("Ingrese el nombre del trabajador: "))
horasTrabajadas=int(input("Ingrese las horas trabajadas por día: "))
diasTrabajados=int(input("Ingrese los días trabajados: "))
sueldoHora=int(input("Ingrese el sueldo por hora: "))

sueldoSemana=sueldoHora*diasTrabajados*horasTrabajadas
print(f"El sueldo semanal es: {sueldoSemana}")

sueldoMes=sueldoSemana*4
print(f"El sueldo mensual es: {sueldoMes}")

if sueldoMes <= 10000:
    print("Obrero tipo A") 
if sueldoMes > 10000 and sueldoMes >= 15000:
    print("Obrero tipo B") 
else:
    print("Sin categoría") 

while True:
    pregunta = str(input("¿Desea otra captura? (NO/SI) "))
    contador +=1
    if pregunta == "NO":
        print("Finalizado")
        break
print(f"Cantidad de trabajadores capturados {contador}")