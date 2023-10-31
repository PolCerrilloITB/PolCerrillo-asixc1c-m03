"""
Pol Cerrillo
31/10/2023
ASIXc1C M03 UF1
Descripció: Seguent segon
"""

hora, minuts, segons = (input().split(" "))

nhora = int(hora)
nmin = int(minuts)
nseg = int(segons)

if nseg == 59 or nseg == 60:
    nseg = 0
    if nmin == 59 or nmin == 60:
        nmin = 0
        if nhora == 24 or nhora == 00:
            nhora = 1
        else:
            nhora = nhora + 1
    else:
        nmin = nmin + 1
else:
    nseg = nseg+ 1

nhora_str = str(nhora).zfill(2)
nmin_str = str(nmin).zfill(2)
nseg_str = str(nseg).zfill(2)

print(nhora_str,":",nmin_str,":",nseg_str)