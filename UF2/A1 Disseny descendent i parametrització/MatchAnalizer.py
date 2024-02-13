"""
Pol Cerrillo
8/01/2024
ASIXc1C M03 UF1
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
def demanar_equips():
    equip1 = input()
    equip2 = input()
    return equip1, equip2
def demanar_resultat():

def mostrar_guanyador():
    print("Guanyar", equipo)
#endregion
resultat = 0
while resultat != -1:
    resultat = input().split()
    if resultat[0] != "-1":
        demanarresultat(int(resultat[0][1]))
    else:
        print("final del partido")

equipo1,equipo2 = demanar_equips()
mostrar_ganador()