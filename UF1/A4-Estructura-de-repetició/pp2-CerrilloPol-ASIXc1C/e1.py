"""
Pol Cerrillo
14/12/2023
ASIXc1C M03 UF1
Descripció: L'usuari introduira una llista d'enters separada per espais.
Previament dira quants enters introduira
Un cop llegits tots, mostrar per pantalla la suma de tots els valors positius.
Cal fer control de errors.
"""
#Control errors
try:
    #Variable de numeros que volem
    maxNum = int(input("Quants numeros: "))
    #Condició de que sigui positiu
    if maxNum > 0:
        #Ficar els numeros amb espais
        num = int(input().split(" "))
        #TODO fer que no salti de la linea 17 a la 21  ique faci la operacio amb els positius
        # print(num)
except:
    print("No has ficat un numero positiu")