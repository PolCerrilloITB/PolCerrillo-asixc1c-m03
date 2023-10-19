"""
Pol Cerrillo
19/10/2023
ASIXc1C M03 UF1
Descripció: Crear un programa que sigui capaç de calcular la nota final de la UF3 del mòdul 03 del
Cicle de Grau Superior d'Administració de Sistemes Informàtics en Xarxa (CFGS ASIX).
El programa només haurà de fer el càlcul per a 1 estudiant, i mostra'ls per pantalla.
Les notes de cadascun dels estudiants s'haurà de demanar per pantalla.
La fórmula de la UF3 és: QUF3 =1*RA1 a on  RA1= 0,30*Pt1.3 + 0,70*Pp1.
El pes de cada IA està fitxat a l'inici de curs per a no ser modificat.
La nota final de les UF's es calcula amb 2 decimals.
"""
#Variables amb les seves funcions:

alumne = input("Alumne a avaluar: ")
Pt1 = float(input("Nota de la Pt1.3: "))
Pp1 = float(input("Nota de la Pp1: "))

#Calcul de la nota QUF3

RA1 = 0.30*Pt1 + 0.70*Pp1
QUF3 = 1*RA1
print("La nota final de", alumne, "en la UF3 es ", round(QUF3,2))
