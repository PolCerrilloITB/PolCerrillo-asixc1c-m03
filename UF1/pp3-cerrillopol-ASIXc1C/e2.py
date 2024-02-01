"""
Pol Cerrillo
01/02/2023
ASIXc1C M03 UF1
Descripció:Encriptar frases:
"""
paraula = input("Donem una frase: ")
if len(paraula) > 3:
    for i in paraula:
        if i != paraula[-1]:
            print(ord(i), end=".")
        else:
            print(ord(i))
else:
        print("Una frase no un/a lletra/numero/caracter")
