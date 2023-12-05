"""
Pol Cerrillo
5/12/2023
ASIXc1C M03 UF1
Descripció: Fer un programa que mostri per pantalla un cronòmetre, indicant les hores, minuts i segons.
"""
import time
nhora = 00
nmin = 00
nseg = 00
while nseg <= 59 and nmin <= 59 and nhora <= 23:
    if nseg == 59:
        nseg = 0
        if nmin == 59:
            nmin = 0
        else:
            nmin = nmin + 1
    else:
        nseg = nseg + 1
    time.sleep(0.25)
    print(str(nhora).zfill(2), ":", str(nmin).zfill(2), ":", str(nseg).zfill(2))