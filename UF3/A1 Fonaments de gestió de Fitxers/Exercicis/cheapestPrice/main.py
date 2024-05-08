'''
Fes un programa que donada la llista de preus (sense decimals) de tot de productes, retorni el preu del
producte més baix. La ruta al fitxer serà introduïda per teclat.
IMPORTANT: no es poden fer servir les funcions de Python.
'''
import cheapestPrice
def main():
    file_path = input("Introduce el archivo: ")
    prices = cheapestPrice.read_file(file_path)
    min_price = cheapestPrice.find_min_price(prices)
    print(f"El producte més econòmic val: {min_price}€")
main()