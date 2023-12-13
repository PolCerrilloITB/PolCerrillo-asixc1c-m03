"""
Pol Cerrillo
5/12/2023
ASIXc1C M03 UF1
Descripció: Crea una aplicació que permet endevinar un número.
L'aplicació genera un nombre “aleatori” de l'1 al 100.
A continuació, l’aplicació va demanant números i va responent si el nombre a endevinar és més gran o més petit
que el que ha introduït, a més dels intents que et queden (tens 10 intents per encertar-lo).
El programa acaba quan s'encerta el número (a més et diu quants intents has necessitat per encertar-lo),
si s'arriba al límit d'intents, l’aplicació et mostra el número que havia generat.
"""
#Variables i la config del random (l'arxiu no es pot dir random)
import random
nrandom = "false"
f = random.randint(1, 100)
cont = 1
#Condicio per fer us del contador i si adivino el numero que hem digui els intents
while cont <= 10 and nrandom == "false":
    print("Digues un numero:")
    n = int(input())
    if f < n:
        cont = cont + 1
        print("És més petit")
    elif f > n:
        cont = cont + 1
        print("És més Gran")
    elif f == n:
        print("Adivinat")
        nrandom = "true"
if nrandom == "true" and cont <= 10:
    print("Acabat en ", cont, "intents")
#Sino que hem digui que no tinc mes intents
else:
    print("Sense intents")
print("Programa finalitzat")
