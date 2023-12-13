"""
Pol Cerrillo
13/12/2023
ASIXc1C M03 UF1
Descripció: Implementa un programa que demani un número i calculi el seu factorial .
El factorial d'un nombre és el producte de tots els enters entre 1 i el mateix nombre
i es representa pel nombre seguit d'un signe d'exclamació. Per exemple 5! = 1x2x3x4x5= 120)
"""
try:
    num = int(input("Numero ?"))
    if num < 0:
        print("Un numero positiu, si us plau")
    else:
        factorial = 1
        for i in range(1, num+1):
            factorial *= i
        print(num,"!", "=", factorial)
except:
    print("Error")