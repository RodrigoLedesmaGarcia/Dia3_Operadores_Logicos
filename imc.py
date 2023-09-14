print("CALCULADORA DE INDICE DE MASA CORPORAL")
altura = float(input("¿cual es tu altura en metros? "))
peso = int(input("¿cual es tu peso en kilos "))

Imc = peso/altura**2;
intImc = int(Imc)
if intImc < 18.5:
    print(f"Tu IMC es de {intImc} estas bajo de peso")
elif intImc < 25:
    print(f"Tu IMC es de {intImc} estas en un peso saludable")
elif intImc < 30:
    print(f"Tu IMC es de {intImc} estas con algo sobre peso")
elif intImc < 35:
    print(f"Tu IMC es de {intImc} estas con obesidad grave")
else:
    print(f"Tu IMC es de {intImc} estas con obesidad morvida")

