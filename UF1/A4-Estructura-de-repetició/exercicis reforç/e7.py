"""
Pol Cerrillo
13/12/2023
ASIXc1C M03 UF1
Descripció: Realitza un programa que mostri la taula de multiplicar d'un número introduït per teclat.
"""
try:
    #Variable del numero que volem multiplicar
    numero = int(input("Numero per la taula de multiplicar? "))
    print("Taula de multiplicar del", numero, ":")
    # Repetició de 10 cops de la taula de multipliar del numero que volem
    for i in range(1, 11):
        resultat = numero * i
        print(numero, "x", i, "=", resultat)
except:
    print("Error, introduieix un numero")