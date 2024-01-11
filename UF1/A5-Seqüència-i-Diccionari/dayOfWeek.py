"""
Pol Cerrillo
11/01/2024
ASIXc1C M03 UF1
Descripció: Donat un enter, mostrar el dia de la setmana amb text (dilluns, dimarts, dimecres…),
tenint en compte que dilluns és el 1. Els dies de la setmana es guarden en una llista.
"""
try:
    setmana = ["Dilluns", "Dimarts", "Dimecres", "Dijous", "Divendres", "Dissabte", "Diumenge"]
    diaSetmna = int(input())
    if diaSetmna > 0 and diaSetmna < 8:
        print(setmana[diaSetmna-1])
    else:
        print("la setmana te 7 dias")
except:
    print("Un numero")
