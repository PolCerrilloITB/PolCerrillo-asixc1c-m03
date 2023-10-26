"""
Pol Cerrillo
24/10/2023
ASIXc1C M03 UF1
Descripció: Galetes == Persones?
"""

persones, galetes = (input().split(" "))
if persones == galetes or galetes*2 == persones:
    print("Let's Eat!")
else:
    print("Let's Fight")
