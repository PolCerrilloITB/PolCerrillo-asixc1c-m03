"""
Pol Cerrillo
24/10/2023
ASIXc1C M03 UF1
Descripció: Minim nombre de monedes
"""
total = float(input())
b500 = 0
b200 = 0
b100 = 0
b50 = 0
b20 = 0
b10 = 0
b5 = 0
m2 = 0
m1 = 0
c50 = 0
c20 = 0
c10 = 0
c5 = 0
c2 = 0
c1 = 0
if total // 500 != 0:
    b500 = b500 + (500*(total // 500))
    total = (total - 500)
if total // 200 != 0:
    b200 = b200 + (200*(total // 200))
    total = (total - 200)
if total // 100 != 0:
    b100 = b100 + (100*(total // 100))
    total = (total - 100)
if total // 50 != 0:
    b50 = b50 + (50*(total // 50))
    total = (total - 50)
if total // 20 != 0:
    b20 = b20 + (20*(total // 20))
    total = (total - 20)
if total // 10 != 0:
    b10 = b10 + (10*(total // 10))
    total = (total - 10)
if total // 5 != 0:
    b5 = b5 + (0.01*(total // 0.01))
    total = (total - 5)
if total // 2 != 0:
    m2 = m2 + (0.01*(total // 0.01))
    total = (total - 2)
if total // 1 != 0:
    m1 = m1 + (0.01*(total // 0.01))
    total = (total - 1)
if total // 0.50 != 0:
    c50 = c50 + (0.01*(total // 0.01))
    total = (total - 0.50)
if total // 0.20 != 0:
    c20 = c20 + (0.01*(total // 0.01))
    total = (total - 0.20)
if total // 0.10 != 0:
    c10 = c10 + (0.01*(total // 0.01))
    total = (total - 0.10)
if total // 0.05 != 0:
    c5 = c5 + (0.01*(total // 0.01))
    total = (total - 0.05)
if total // 0.02 != 0:
    c2 = c2 + (0.01*(total // 0.01))
    total = (total - 0.02)
if total // 0.01 != 0:
    c1 = c1 + (0.01*(total // 0.01))
    total = (total - 0.01)
print("Billets de 500€: ",b500)
print("Billets de 200€: ",b200)
print("Billets de 100€: ",b100)
print("Billets de 50€: ",b50)
print("Billets de 20€: ",b20)
print("Billets de 10€: ",b10)
print("Billets de 5€: ",b5)
print("Monedes de 2€: ",m2)
print("Monedes de 1€: ",m1)
print("Centims de 50: ",c50)
print("Centims de 20: ",c20)
print("Centims de 10: ",c10)
print("Centims de 5: ",c5)
print("Centims de 2: ",c2)
print("Centims de 1: ",c1)





