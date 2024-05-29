
calculos=0

SiNo=str(input("Desea hacer un cálculo (SI/NO)"))

while True:
    if SiNo == "SI":
        calculos += 1
        altura=float(input("Altura en metros: "))
        peso=float(input("Peso en Kg: "))

        imc=peso/(altura*altura)
        
        if imc < 18.5:
            print(imc)
            print("Peso inferior al normal")
        elif imc == 18.5 and imc > 24.9:
            print(imc)
            print("Normal")
        elif imc == 25.0 and imc > 29.9:
            print(imc)
            print("Sobre Peso")
        elif imc > 30.0:
            print(imc)
            print("Obesidad")

            SiNo=str(input("Desea hacer otro cálculo (SI/NO)"))

    elif SiNo == "NO":
        print (f"El número de cálculos fueron de:  {calculos}")
        break
