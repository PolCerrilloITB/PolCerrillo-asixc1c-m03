"""
Pol Cerrillo
23/11/2023
ASIXc1C M03 UF1
Descripció: Programa per crear una serp Python a mida.

Cal demanar quina mida (quantitat de COS) ha de tenir la serp. Tot seguit mostrar-la per pantalla.

Es valorarà el fet de que el cos faci siga sagues. Potser, la mida del cos ha de ser mínim 5
"""
import random

CAP= "....\...../ ...."
ULLS= "...╚⊙ ⊙╝..."
COS = "═(███)═"
COS2 = ".╚═(███)═╝"
COS3 = "..╚═(███)═╝"
COS4 = "...╚═(███)═╝"
CUA =  " ═V═ "
c = int(input())
print(CAP)
print(ULLS)
if c < 5:
    print("Minim 5")
else:
    for i in range(c):
        print(random.choice([(COS), (COS2), (COS3), (COS4)]))
    print(CUA)