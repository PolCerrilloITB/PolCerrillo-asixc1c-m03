"""
Pol Cerrillo
24/10/2023
ASIXc1C M03 UF1
Descripció: Galetes == Persones?
"""

persones, galetes = (input().split(" "))
npersona = int(persones)
ngaletes = int(galetes)
if npersona % ngaletes == 0:
    print("Let's Eat!")
else:
    print("Let's Fight")
