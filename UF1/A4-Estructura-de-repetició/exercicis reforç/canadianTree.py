"""
Pol Cerrillo
19/12/2023
ASIXc1C M03 UF1
Descripció:Fer un programa que dibuixa un avet del Canadà. Cal demanar la mida de l'arbre.
La mida inclou el tronc i les branques
"""
import random
from time import sleep
n = int(input())
TRONC = "🪵"
FULLA = "🌿"
ESTEL = "🔸"
BOLA="🔴"
MINIM_ALT = 4

altura = 0
while altura < MINIM_ALT:
    altura = int(input("Altura del arbol?\n"))

alturaHojas = int(altura * 0.7)
alturaTroncos = int(altura * 0.3)

print(" " * (alturaHojas - 2) + ESTEL)
for i in range(2, alturaHojas + 1):
    print(" " * (alturaHojas -i -1), end="")
    sleep(0.25)
    for j in range(0, i):
        decoracion = random.randint(1, 5)
        if decoracion == 1:
            print(BOLA, end="")
        else:
            print(FULLA, end="")
    print("")
anchoTronco = int(alturaHojas * 0.33)
for k in range(0, alturaTroncos):
    print(" " * (alturaHojas-anchoTronco -1) + TRONC * anchoTronco)
    sleep(0.5)
