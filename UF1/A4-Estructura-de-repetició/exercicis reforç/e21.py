"""
Pol Cerrillo
12/12/2023
ASIXc1C M03 UF1
Descripció:Crea una aplicació que permet endevinar un nombre aleatori pensat per un usuari.
L'usuari introdueix un número “aleatori” de l'1 al 100.
A continuació, l’ordinador “Computer” va intentant “endevinar” el número que l’usuari ha introduït.
A cada intent que fa el “computer”,  haurà de comprovar si ha encertat o no.
En cas que no encerti, preguntarà a l’usuari si és més gran o més petit, el nombre que està buscant.
El programa acaba quan encerta el número o si s'arriba al límit d'intents (10 intents màxims per encertar-lo)
En acabar cal mostrar si ha encertat o no, i la quantitat d’intents que s’han fet servir.
"""
try:
    cont = 1
    sortir = "false"
    import random
    num_escollit = int(input())
    minNum = 0
    maxNum = 100
    n = random.randint(1, 100)
    while num_escollit <= 0 or num_escollit > 100:
        num_escollit = int(input())
    while cont <= 10 and sortir == "false":
        if num_escollit != n:
            print("El teu numero es aquest?", n)
            pista = input("Gran o petit?")
            if pista == "-":
                cont = cont + 1
                maxNum = n
                n = random.randint(minNum, n)
            elif pista == "+":
                cont = cont + 1
                minNum = n
                n = random.randint(n, maxNum)
            else:
                print("Error")
        else:
            sortir = "true"
    if sortir == "true" and cont <= 10:
        num_escollit = n
        print("Encertat en", cont, "intents i el numero es", num_escollit)
    else:
        print("Has arribat al numero maxim d'intetns. El numero es aquest", num_escollit )
except:
    print("Error")

