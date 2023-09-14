print("Bienvenido a la montaña rusa")
altura = int(input("Cual es tu altura en cm? "))

if altura >= 120:
     print("Te puedes subir a la montaña rusa!")
     edad = int(input("¿Cual es tu edad? "))
     if edad < 12:
         cuenta = 5
         print("Pagas $5")
     elif edad <= 18:
         cuenta = 10
         print("Pagas $10")
     else:
         cuenta = 20
         print("Paga $20")

     foto = input("¿quieres la foto del paseo, SI o No ?")
     if foto =="SI":
      cuenta +=3
      print(f"¿Total a pagar ${cuenta}, por favor?")
     else:
         cuenta
         print(f"¿Total a pagar ${cuenta}, por favor?")

else:
    print("No te puedes subir a la montaña rusa")