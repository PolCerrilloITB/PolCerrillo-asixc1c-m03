"""
Pol Cerrillo
23/11/2023
ASIXc1C M03 UF1
Descripció: Imprimir de la A fins la Z.

A cada linia apareix un carcater i la seguent linia apareix un carcater més de forma progresiva.
Fins aconseguir tenir una linia que mostri de la A fins la Z
"""
for n in range(ord("a"), ord("z") + 1):
    for j in range(ord("a"), n+1):
        print(chr(j), end=" ")
    print()