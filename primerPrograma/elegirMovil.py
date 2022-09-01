# En este programa, ayudaremos al usuario a elegir su nuevo movil

movil = ""
error = "Lo siento, la opción debe ser una de las anteriores, vuelve a intentarlo la próxima vez."

print("Hola!! Gracias por acudir a nosotros para guiarte en esta decisión tan difícil! \n"
      "Vamos allá!!\n")

so = input("Prefieres iOS o Android? ")
if so == "Android":
    dinero = input("Tienes dinero? S/N: ")
    if dinero == "N":
        movil = "Android Chino de 100€"
    elif dinero == "S":
        camara = input("Te importa la camara del móvil? S/N: ")
        if camara == "S":
            movil = "Google Pixel Supercamara"
        elif camara == "N":
            movil = "Android Calidad-Precio"
        else:
            print(error)
    else:
        print(error)
elif so == "iOS":
    dinero = input("Tienes dinero? S/N: ")
    if dinero == "S":
        movil = "iPhone Ultra Pro Max"
    elif dinero == "N":
        movil = "iPhone de segunda mano"
    else:
        print(error)
else:
    print(error)

print("RESULTADO: Tu movil ideal es el {}.".format(movil))