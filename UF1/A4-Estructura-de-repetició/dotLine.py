"""
Pol Cerrillo
16/11/2023
ASIXc1C M03 UF1
Descripció: Demana un enter a l'usuari, per saber quantes línies
Demana un enter a l'usuari, per saber quants punts
Imprimeix per pantalla tantes línies amb tants punts com l'usuari hagi indicat
"""
linies = int(input("Linies: "))
punts = int(input("Punts: "))
for i in range(linies):
    for n in range(punts):
        print(".", end="")
    print("")