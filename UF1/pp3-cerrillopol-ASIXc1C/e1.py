"""
Pol Cerrillo
01/02/2023
ASIXc1C M03 UF1
Descripció: Implementar un programa que faci les següents operacions:
Demanar, a l'usuari, la quantitat de files i columnes d'una matriu 2D.
Comprovar que la matriu sigui quadrada, es a dir que tingui les mateixes fileres que columnes
Guarda la matriu en una variable anomenada "matriu"
Omplir la matriu amb 1's a les vores i la resta amb 0's.
La mida de la matriu ha de ser senar
"""
#Constants declarades
FILAS = []
COLUMNES = []
MATRIU = []
try:
    #Pregunta de las fileras i columnes
    files = int(input("Quantitat files: "))
    columnes = int(input("Qunatitat de columnes: "))
    #TODO revisar aquesta condicio perque funcioni adecuadament
    if files == columnes and files // columnes != 0:
        #Aqui printa el quadre que li demanem perque sigui quadrat, sino no hi printa
        #TODO fer que la quadricula que volem sigui senar i no parella
        for x in range(files):
            for y in range(columnes):
                #TODO fer que aquesta linea es converteixi en una linea per la MATRIU i ficar-la dins.
                if x in FILAS and y in COLUMNES:
                    print("1", end="")
                    #TODO Aquesta linea esta be, pero li falta la ajuda de la matriu per poder funcionar correctament
                else:
                    print("0", end="")
            print()
            #Mostrar l'error de que no te forma quadrada
    else:
        print("Mateix nombre de files i columnes, si us plau.")
        #Mostra per pantalla quan es un caracter i no un numero
except:
    print("Un numero de filas i de columnes si us plau.")