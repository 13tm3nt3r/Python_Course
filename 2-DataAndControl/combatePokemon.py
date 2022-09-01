# In this file, we will create a pokemon combat

import random
import os

# Vidas iniciales
VIDA_PIKACHU_I = 80
VIDA_SQUIRTLE_I = 90

TAMAÑO_VIDA = 20

def combate():
    inicio = "BIENVENIDO AL COMBATE POKEMON!!"
    subrayado_inicio = "-" * len(inicio)

    # Dialogo inicial
    print("\n{}\n{}\n".format(inicio, subrayado_inicio))
    print("En este combate, los pokemon PIKACHU y SQUIRTLE se enfrentarán. \n¿¿Quién ganará??")

    vida_pikachu = VIDA_PIKACHU_I
    vida_squirtle = VIDA_SQUIRTLE_I

    print("COMIENZA EL COMBATE CON ESTAS VIDAS INICIALES")
    vidas(vida_pikachu, vida_squirtle)

    while vida_pikachu > 0 and vida_squirtle > 0:
        # Pikachu ataca
        ataque_n = random.randint(1, 2)
        if ataque_n == 1:
            ataque_pikachu = "Bola Voltio"
            vida_squirtle -= 10
        else:
            ataque_pikachu = "Onda Trueno"
            vida_squirtle -= 11

        print("\nPikachu elige el ataque {}".format(ataque_pikachu))

        vidas(vida_pikachu, vida_squirtle)

        input("ENTER PARA CONTINUAR EL COMBATE\n")
        os.system("cls")

        # Squirtle ataca
        ataque_n = 0
        lista = [1, 2, 3, 4]
        while ataque_n not in lista:
            ataque_n = input("""\nElige el número del ataque de Squirtle:
    1 - Placaje
    2 - Pistola Agua
    3 - Burbuja
    4 - No atacar en este turno
    >>>>> """)

        if ataque_n == "1":
            ataque_squirtle = "Placaje"
            vida_pikachu -= 10
        elif ataque_n == "2":
            ataque_squirtle = "Pistola Agua"
            vida_pikachu -= 12
        elif ataque_n == "3":
            ataque_squirtle = "Burbuja"
            vida_pikachu -= 9
        elif ataque_n == "4":
            ataque_squirtle = "4. Por lo que decide no atacar en este turno"

        print("\nSquirtle elige el ataque {}".format(ataque_squirtle))

        vidas(vida_pikachu, vida_squirtle)

        input("ENTER PARA CONTINUAR EL COMBATE\n")
        os.system("cls")


def vidas(vida_pikachu, vida_squirtle):
    fin = False

    if vida_pikachu < 0:
        vida_pikachu = 0
        fin = True
    elif vida_squirtle < 0:
        vida_squirtle = 0
        fin = True

    barra_pikachu = int((vida_pikachu * TAMAÑO_VIDA) / VIDA_PIKACHU_I)
    barra_squirtle = int((vida_squirtle * TAMAÑO_VIDA) / VIDA_SQUIRTLE_I)

    print("Pikachu  [{}{}] {}".format(("*" * barra_pikachu), " " * (TAMAÑO_VIDA - barra_pikachu), vida_pikachu))
    print("Squirtle [{}{}] {}".format(("*" * barra_squirtle), " " * (TAMAÑO_VIDA - barra_squirtle), vida_squirtle))

    if fin:
        ganador(vida_pikachu, vida_squirtle)


def ganador(vida_pikachu, vida_squirtle):
    if vida_pikachu < vida_squirtle:
        print("\nEl ganador es SQUIRTEL con {} puntos de vida!!!".format(vida_squirtle))
        exit(0)
    else:
        print("\nEl ganador es PIKACHU con {} puntos de vida!!!".format(vida_pikachu))
        exit(0)


combate()
