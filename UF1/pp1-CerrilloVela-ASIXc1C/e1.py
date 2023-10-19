"""
Pol Cerrillo
19/10/2023
ASIXc1C M03 UF1
Descripció: S'ha creat un nou embàs, esfèric, per emmagatzemar líquids,
com ara aigua, llet, o qualsevol refresc. Ens demanen, crear un programa que mostri per pantalla,
l’àrea i el volum, d’una esfera on el radi es llegeix del teclat.
Les fórmules són V=4/3π*r3 i A=4*π*r2  on el valor de π és 3.141592.
"""

#Variables amb les seves operacions

radi = int(input("Quin es el radi: "))
PI = 3.141592
V = 4/3*PI*radi**3
A = 4*PI*radi**2
print("El àrea es", A, "i el volum es", V)