"""
Pol Cerrillo
8/01/2024
ASIXc1C M03 UF2
Descripció: Volem fer un programa que analitzi els resultats d'un partit de bàsquet.
Hem de tenir en compte que en un partit de bàsquet es poden fer 1, 2 o 3 punts.
Donat els diferents resultats analitza que està passant.
L'usuari introduirà primer el nom dels dos equips i després el resultat actual
"""
#TODO pedirEquipos
#TODO pedirResultados
#TODO analizarResultados
#TODO mostrarGanador
#region definir funcions
equip1 = ""
equip2 = ""
def demanar_equips():
    nequip1 = input()
    nequip2 = input()
    return nequip1, nequip2
def demanar_resultat():
    resultatA =[]
    resultatB =[]
    try:
            resultat = input().split
            while resultat[0] != "-1":
                resultatA.append(int(resultat[0]))
                resultatB.append(int(resultat[1]))
                resultat = input().split
            return resultatA, resultatB
    except:
        print("Lletras en resultats")
def analitzar_resultat(resultatA, resultatB):
    for pos in range(len(resultatA)):
        puntsA = resultatA[pos]
        puntsB = resultatB[pos]
        if
def mostrar_guanyador():
    print("Guanyador",)
#endregion

nequipo1,nequipo2 = demanar_equips()
resultatA, resultatB, = demanar_resultat()
analitzar_resultat(resultatA, resultatB)
mostrar_ganador()