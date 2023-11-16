"""
Pol Cerrillo
16/11/2023
ASIXc1C M03 UF1
Descripció: Mostra per pantalla tots els números fins a un enter entrat per l'usuari
"""
num = int(input("Numeró: "))
if num > 0:
    for i in range(1, num + 1):
        if i < num:
            print(str(i)+" ", end="")
        else:
            print(i, end="")
if num < 1:
    for n in range(-1, num - 1, -1):
        if n < num:
            print(str(n)+" ", end="")
        else:
            print(n, end="")