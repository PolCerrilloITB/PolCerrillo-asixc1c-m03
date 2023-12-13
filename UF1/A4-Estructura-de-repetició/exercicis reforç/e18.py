"""
Pol Cerrillo
5/12/2023
ASIXc1C M03 UF1
Descripció: Fer un programa que mostri per pantalla un cronòmetre, indicant les hores, minuts i segons.
"""
#Variables i la configuració de time
import time
nhora = 00
nmin = 00
nseg = 00
#definir el limit de cada variable
while nseg <= 59 and nmin <= 59 and nhora <= 23:
    #repetir fins que arribi a un valor definit
    if nseg == 59:
        nseg = 0
        if nmin == 59:
            nmin = 0
        else:
            nmin = nmin + 1
    else:
        nseg = nseg + 1
        #time.sleep velocitat del cronometre
    time.sleep(0.25)
    #str().zfill(valor dels valors que vols)
    print(str(nhora).zfill(2), ":", str(nmin).zfill(2), ":", str(nseg).zfill(2))