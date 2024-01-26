"""
Bernat Carol Costajussà - Roma
26/01/2024
ASIXc1C M03 UF1 A5 pushButtonPadlockSimulator
Descripció: Volem fer un simulador d'un "candau" (cadenat) com el de la foto:
La nostra versió, també tindrà 8 botons, però el primer serà el 0. A l'inici tots els botons
estaran sense apretar.
L'usuari introduirà enters indicant quin botó ha "clicat" premut (o desclicat)
Quan introdueixi el -1, és que ja ha acabat i hem d'imprimir l'estat del "candau"
"""
CONTRASSENYA = [0, 1, 2, 3, 4, 5, 6, 7]
candau = []
numeros = input().split(" ")
sortir = False
for x in CONTRASSENYA:
    numStr = numeros[x]
    numInt = int(numStr)
    if numInt == -1:
        sortir = True
    else:
        if sortir is False:
            if CONTRASSENYA[x] == numInt:
                candau.append("True")
            else:
                candau.append("False")
print(candau)