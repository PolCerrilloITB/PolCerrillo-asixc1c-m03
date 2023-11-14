"""
Pol Cerrillo
14/11/2023
ASIXc1C M03 UF1
Descripció: MODIFICACIÓ: IsPasswordOK --> IsPinOK
Programa que demana a l'usuari un PIN, de manera repetitiva mentre que no introdueixi 1234.
L'usuari té només 3 intents.
Quan finalment escrigui el PIN correcte, li dirà "Benvingut" i acabarà el programa.
O quan s'esgoti el nombre d'intents, també haurà d'acabar, tot dient "LAS CAGAO BACALAO"
Tenim, un Easter Egg , que és 0007, que també permet que acabi correctament.
"""
PWD = "asdasd"
clave = input("Dime la clave:")
EasterEgg = "0007"
intentos = 0
while clave != PWD and intentos > 2 and clave != EasterEgg:
   print("Clave incorrecta!!!")
   clave = input("Dime la clave:")
   intentos = intentos+1
if intentos < 2:
    print("Bienvenido!!!")
    print("Programa terminado")
else:
    print("LAS CAGAO BACALAO")

