'''
Fes un programa que donada la llista de preus (sense decimals) de tot de productes, retorni el preu del
producte més baix. La ruta al fitxer serà introduïda per teclat.
IMPORTANT: no es poden fer servir les funcions de Python.
'''
file_path = 'precios.txt'
def read_file(file_path):
    with open(file_path, 'r') as f:
        prices = [int(price) for price in f.read().split()]
    return prices


def find_min_price(prices):
    min_price = prices[0]
    for price in prices:
        if price < min_price:
            min_price = price
    return min_price