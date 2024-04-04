'''
Pol Cerrillo
04/04/2023
ASIXc1C M03 UF2
Descripció: Crear una aplicació "petitesUtilitats" amb un menu que mostri per pantalla les opcions a escollir amb les funcionalitats
de cada punt
'''
import utilitats
def main():
    frase = ""
    print(1, "Signes de puntuació - Quantitat")
    print(2, "Signes de puntuació - Posició")
    print(3, "Text - Codificar")
    print(4, "Text - Descodificar")
    print(5, "Executar totes les utilitats")
    print(6, "Sortir de l'aplicació")
    eleccion = input()
    if eleccion == "1":
        frase = utilitats.utilitat1()
    elif eleccion == "2":
        frase = utilitats.utilitat2()
    elif eleccion == "3":
        frase = utilitats.utilitat3()
    elif eleccion == "4":
        frase = utilitats.utilitat4()
    elif eleccion == "5":
        frase = utilitats.utilitat5()
    elif eleccion == "6":
        print("Login Out")
    else:
        print("Escoje una de las siguientes opciones")
main()