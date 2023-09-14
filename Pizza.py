print("¿Bienvenido a la pizzeria")
tamano = input("¿De que tamaño quiere la pizza?, CHICA, MEDIANA, GRANDE ")
if tamano == "CHICA":
    costo = 120
    peperoni = input("Añadir pepeeroni? SI o NO " )
    if peperoni == "SI":
        costo += 15
    else:
        costo
    extra_queso = input("¿Quiere añadir mas queso a la pizza? SI o NO ")
    if extra_queso == "SI":
        costo += 10
        print(f"El costo de tu pizza es de ${costo}.MXN")
    else:
        print(f"El costo de tu pizza es de ${costo}.MXN")


elif tamano == "MEDIANA":
    costo = 250
    peperoni = input("Añadir pepeeroni? SI o NO ")
    if peperoni == "SI":
        costo += 15
    else:
        costo
    extra_queso = input("¿Quiere añadir mas queso a la pizza? SI o NO ")
    if extra_queso == "SI":
        costo += 10
        print(f"El costo de tu pizza es de ${costo}.MXN")
    else:
        print(f"El costo de tu pizza es de ${costo}.MXN")

elif tamano == "GRANDE":
    costo = 320
    peperoni = input("Añadir pepeeroni? SI o NO " )
    if peperoni == "SI":
        costo += 15
    else:
        costo
    extra_queso = input("¿Quiere añadir mas queso a la pizza? SI o NO ")
    if extra_queso == "SI":
        costo += 10
        print(f"El costo de tu pizza es de ${costo}.MXN")
    else:
        print(f"El costo de tu pizza es de ${costo}.MXN")
else:
    print("Esa opcion no existe")

