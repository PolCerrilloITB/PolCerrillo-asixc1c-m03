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
    if caracter in paraula:
        #TODO fer que canvi el caracter seleccionat per el que volem substituir.
        # AMb el paraula.replace(caracter, caracterSubs) no es pot fer
        caracterSubs = paraula
    resultat = caracterSubs
    print("Resultat:")
    #Resultat del canvi
    print(resultat)
except:
    print("Introdueix una frase")