"""
Pol Cerrillo
12/12/2023
ASIXc1C M03 UF1
Descripció: Escriu un programa que mostri la taula de multiplicar dels números 1,2,3,4 i 5.
"""
for i in range(1, 6):
    print("Taula de multiplicar del", i, ":")
    for n in range(1, 11):
        resultat = i * n
        print(i, "x", n, "=", resultat)