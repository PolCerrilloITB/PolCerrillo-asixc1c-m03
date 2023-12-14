"""
Pol Cerrillo
14/12/2023
ASIXc1C M03 UF1
Descripció: Sustitució de lletras per caracters
"""
try:
    #Variables corresponents
    paraula = str(input("Introdueix una frase?"))
    caracter = str(input("Quin caracter vols remplaçar?"))
    caracterSubs = str(input("Quin es el caracter de substitució?"))
    #Substitució del caracter a cambiar per un altre
    resultat = paraula.replace(caracter, caracterSubs)
    print("Resultat:")
    #Resultat del canvi
    print(resultat)
except:
    print("Introdueix una frase")