"""
Pol Cerrillo
24/10/2023
ASIXc1C M03 UF1
Descripció: Dies en un mes
"""

mes = input("Quin mes vols?")
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes 12:
    print("Aquest mes te 31 dias")
elif mes == 2:
    print("Aquest mes te 28 o 29 dias")
elif mes == 4 or mes == 6 or mes == 11:
    print("Aquest mes te 30 dias")
else:
    print("Error")