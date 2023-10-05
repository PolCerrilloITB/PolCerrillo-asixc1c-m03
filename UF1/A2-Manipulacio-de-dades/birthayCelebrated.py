"""
Pol Cerrillo
03/10/2023
ASIXc1C M03 UF1
Descripció: Birthay Celebrated
"""
# Programa demana data de naixament i data actual

diaAniversari = int(input("Quin dia vas neixer?"))
mesAniversari = int(input("Quin mes vas neixer?"))
diaActual = int(input("Quin dia es avui?"))
mesActual = int(input("Quin mes es avui?"))

if ((mesAniversari < mesActual) or
        (mesActual == mesAniversari) and diaActual >= diaAniversari):
    print("Has celebrat el teu aniversari")
else:
    print("No has celebrat encara el teu aniversari")
