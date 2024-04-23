'''
Pol Cerrillo
23/04/2023
ASIXc1C M03 UF3
Descripció: Fer un programa en Python que llegint el fitxer JSON de les platges
de Barcelona ens doni la següent informació:
Obtenir els noms de tots els districtes de Barcelona que tenen platges CV? i SM?
Obtenir la quantitat de platges que hi ha al districte de "Ciutat Vella"  4?
Font:  Open Data BCN  Inici >  Territori >  Urbanisme i infraestructures >  Platges a la ciutat de ...
Arxiu a processar: opendatabcn_NP-NASIA_Platges-js.json
quantitat de línies:  ???
'''
import json
def get_beaches_data():
    with open("opendatabcn_NP-NASIA_Platges-js.json", "r") as f:
        data = json.load(f)
    beachAndDistrict = {beach["name"]: beach["addresses"][0]["district_name"] for beach in data}
    return beachAndDistrict
def quantityDistrict(beachAndDistrict):
    district_to_quantity = {}
    for district in beachAndDistrict.values():
        if district not in district_to_quantity:
            district_to_quantity[district] = 1
        else:
            district_to_quantity[district] += 1
    return district_to_quantity
def main():
    beachAndDistrict = get_beaches_data()
    district_to_quantity = quantityDistrict(beachAndDistrict)
    print(district_to_quantity)
    for district, quantity in district_to_quantity.items():
        print(f"El distrito {district} tiene {quantity} playas.")
main()
