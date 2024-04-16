'''
Pol Cerrillo
16/04/2024
ASIXc1C M03 UF3
Descripció:Després de fer un examen un professor vol veure l'estat general de la classe.
Vol conèixer la nota mínima, la màxima i la mitjana dels seus alumnes.
Les notes provenen d'un fitxer la ruta del qual serà introduïda per teclat.
Per tant, la quantitat de notes és indeterminada, i dependrà del contingut de cada fitxer que es faci servir.
Fes un petit programa que li solucioni la tasca (les notes de l'examen no tenen decimals).
'''
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def llegirFitxer():
    try:
        fitxer = open(input("Ruta del fitxer:"))
        linia = fitxer.readline()
        fitxer.close()
        return linia
    except:
        print("Ruta incorrecta o no trobada")
def lletras():
    if nums in linia:
        fitxer
def calculdenotes(notes):
    notes = notes.split()
    notes = [int(nota) for nota in notes]
    minima = min(notes)
    maxima = max(notes)
    mitjana = sum(notes)/len(notes)
    return minima, maxima, mitjana
def main():
    notes = llegirFitxer()
    minima, maxima, mitjana = calculdenotes(notes)
    print(f"Minima: {round(minima)}")
    print(f"Maxima: {round(maxima)}")
    print(f"Mitjana: {round(mitjana, 2)}")
