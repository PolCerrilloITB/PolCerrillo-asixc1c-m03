'''
Pol Cerrillo
18/04/2024
ASIXc1C M03 UF3
Descripció: Volem fer un petit programa per guardar la informació dels diferents llibres que té una biblioteca.
A un fitxer s'ha de dir  books.out
Per introduir els llibres, primer es llegirà els llibres per teclat (en concret: títol, autor, nombre de pàgines).
El primer nombre indica la quantitat de llibres que es vol introduir.
En versions futures la lectura dels llibres  es farà d'un fitxer.
Quan acabi volem que mostri la llista de llibres i el número total, el llibre més curt i el llibre més llarg
(en cas d'empat el primer que s'hagi llegit del fitxer).
'''
import booksApp
def main():
    llibres = booksApp.guardar_llibres()
    booksApp.mostrar_llibres(llibres)
if __name__ == "__main__":
    main()