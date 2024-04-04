'''
Pol Cerrillo
04/04/2023
ASIXc1C M03 UF2
Descripció: Utilitat 1: Calcular quantes lletres tenen les frases que s'entrin per teclat. les frases han de tenir mes
de dues paraules. No s'han de comptar els signes de puntuació, ni els numeros nu els caracters especials.
El \q es que la frase ha acabat
Fer que las utilitats facin el que pertocan:
Utilitat 2: contar vocals i consonants
Utilitat 3 : Canviar les lletres per numeros
Utilitat 4: Canviar els colors de vocals i consonants
Utilitat 5 : Executar totes les utilitats
Utilitat 6: Finalitzar la aplicacio
'''
import re
import systemColors
def utilitat1():
    frase = ""
    try:
        while frase[:] != "\q" and frase != 3:
            frase = input()
            frase = frase.lower()
            frase = re.sub(r'[^\w\s]', '', frase)
            frase = frase.split()
            print(frase)
            paraules = {}
            especial = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "/", "#", ".", ",", "-", "_", ";", ":", "@", "$", "(", ")", "=", "?", "¿", "?"}
            for paraula in frase:
                #TODO fer que conti les paraules
                if paraula in especial:
                    paraula = 0
                else:
                    paraula += 1
                return paraula
            for caracter in frase:
                if caracter in paraules:
                    caracter +=1
                else:
                    caracter =1
                return caracter
            try:
                if caracter <= 0 and paraula <= 0:
                    print("De" + caracter + "caràcters" + paraula + "són lletres.")
            except:
                print("Revisió")
    except:
        print("Introdueix una frase")

def utilitat2():
    dades = ""
    while dades[:] != "\q" and dades != 3:
        dades = dades.lower()
        dades = re.sub(r'[^\w\s]', '', dades)
        dades = dades.split()
        paraules = {}
        #TODO fer que conti lletres no paraules
        for paraula in dades:
            if paraula in paraules:
                paraules[paraula] += 1
            else:
                paraules[paraula] = 1
        for paraula in paraules:
            print(paraula + ": " + str(paraules[paraula]))
def utilitat3():
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    paraula = ""
    while paraula != "\q":
        paraula = input("")
        if len(paraula) > 2:
            if paraula in numeros:
                #TODO Fer que no tracti el numero en la taula ASCII
                return paraula
            else:
                for i in paraula:
                    if i != paraula[-1]:
                        # Separacio entra paraules encriptades
                        print(ord(i), end=".")
                    else:
                        print(ord(i))
        else:
            print("Una frase no un/a lletra/numero/caracter")
    else:
        print("Login Out")
def utilitat4():
    VOCAL = ["a", "e", "i", "o", "u"]
    CONSONANT = ["b", "c", "d", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "z", "x"]
    CONSONANT = systemColors.CBLACK
    VOCAL = systemColors.CBLUE
    dades = ""
    while dades[:] != "\q" and dades != 3:
        dades = dades.lower()
        dades = re.sub(r'[^\w\s]', '', dades)
        dades = dades.split()
        paraules = {}
        #TODO canviar las lletres a colors
        for paraula in dades:
            #TODO acabar de fer el canvi i canviar el codi de sota
            if paraula in VOCAL:
                VOCAL[paraula] += 1
            else:
                CONSONANT[paraula] = 1
        for paraula in paraules:
            print(paraula)

def utilitat5():
    utilitat1()
    utilitat2()
    utilitat3()
    utilitat4()