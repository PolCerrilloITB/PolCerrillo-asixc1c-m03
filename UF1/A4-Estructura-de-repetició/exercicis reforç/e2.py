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
import random
nrandom = "false"
f = random.randint(1, 100)
for i in range(1, 11):
    if nrandom == "false":
        print("Digues un numero:")
        n = int(input())
        if f < n:
            print("És més petit")
        elif f > n:
            print("És més Gran")
        elif f == n:
            print("Adivinat")
            nrandom = "true"
if nrandom == "true":
    print("Acabat en ", cont, "intents")
else:
    print("Sense intents")
print("Programa finalitzat")
