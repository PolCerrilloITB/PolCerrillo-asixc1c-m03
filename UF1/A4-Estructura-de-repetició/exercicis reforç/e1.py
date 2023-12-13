"""
Pol Cerrillo
13/12/2023
ASIXc1C M03 UF1
Descripció: Implementa un programa que demani un número i calculi el seu factorial .
El factorial d'un nombre és el producte de tots els enters entre 1 i el mateix nombre
i es representa pel nombre seguit d'un signe d'exclamació. Per exemple 5! = 1x2x3x4x5= 120)
"""
try:
    #Valor del numero que volem
    num = int(input("Numero ?"))
    #condicio de que el numero sigui positiu
    if num < 0:
        print("Un numero positiu, si us plau")
    else:
        #Variable de factor del numero escollit i repetir el valor factor multiplicant per el numero
        factor = 1
        for i in range(1, num+1):
            factor *= i
        print(num,"!", "=", factor)
except:
    print("Error")