"""
Pol Cerrillo
01/02/2023
ASIXc1C M03 UF1
Descripció:Encriptar frases:
Fer un programa per llegir una frase pel teclat i, en acabar, mostri la frase encriptada.
Per encriptar la frase, ha de fer servir el valor numeric de cada lletra. Caldrà escriure un punt "." per
poder indentificar a on comença i acaba cada lletra.
"""
paraula = input("Donem una frase: ")
#Posem una regla per la longitud maxima que ahuria de tenir una frase normal
if len(paraula) > 3:
    for i in paraula:
        if i != paraula[-1]:
            #Separacio entra paraules encriptades
            print(ord(i), end=".")
        else:
            print(ord(i))
else:
    print("Una frase no un/a lletra/numero/caracter")
