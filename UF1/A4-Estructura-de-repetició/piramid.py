"""
Pol Cerrillo
23/11/2023
ASIXc1C M03 UF1
Descripció: S'imprimeix una piràmide d'altura N de #
"""

n = int(input())
cont = 1
totxo= "\U0001F9F1"
for n in range(n):
    for j in range(cont):
        print(totxo, end=" ")
    cont = cont+1
    print()