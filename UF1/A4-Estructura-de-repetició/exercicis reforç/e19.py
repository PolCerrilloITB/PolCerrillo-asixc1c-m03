"""
Pol Cerrillo
5/12/2023
ASIXc1C M03 UF1
Descripció: Escriu un programa que mostri el següent menú d’opcions:
Literatura
Cinema
Música
Videojocs
Sortir
Si l’usuari tria una opció de l’1 al 4, el programa ha de mostrar uns quants suggeriments de títols relacionats
amb el tema escollit. Si l’usuari tria una opció no contemplada, el programa ha de mostrar un missatge d’error.
En tot cas, el programa tornarà a mostrar el menú d’opcions, tret que l’usuari triï l’opció 5:
en aquest cas, el programa mostrarà un missatge de comiat i acabarà.
"""
sortir = "false"
print("Tria una d'aquestes opcions: ")
print("1. Literatura")
print("2. Cinema")
print("3. Música")
print("4. Videojocs")
print("5. Sortir")
while sortir == "false":
    opcio = int(input())
    if opcio == 1:
        print("Tituls de literatura: etc")
    elif opcio == 2:
        print("Tituls de cinema: etc")
    elif opcio == 3:
        print("Tituls de música: etc")
    elif opcio == 4:
        print("Tituls de videojocs: etc")
    elif opcio == 5:
        print("Adeu")
        sortir = "true"
    else:
        print("Error")