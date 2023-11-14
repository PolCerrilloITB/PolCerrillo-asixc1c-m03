"""
Pol Cerrillo
14/11/2023
ASIXc1C M03 UF1
Descripció: Dona un numero fins que sigui 5
"""

number=0
PWD=1234
while number!=5:
    number = int(input("Give me five:"))
    if number == PWD and number!=5:
        number=5
print("Great thank you")