"""
Pol Cerrillo
05/10/2023
ASIXc1C M03 UF1
Descripció:Contardor monedes
"""
# Contar las monedas i digues el seu import

moneda1 = int(input("Monedes de 2€?"))
moneda2 = int(input("Monedes de 1€?"))
moneda3 = int(input("Monedes de 20 cèntims?"))
moneda4 = int(input("Monedes de 10 cèntims?"))
moneda5 = int(input("Monedes de 5 cèntims?"))

euros = (moneda1+2 + moneda2)
centims = (moneda3+20 + moneda4+10 +moneda5+5)
print("Tens", euros, "€ i", centims, "centims")