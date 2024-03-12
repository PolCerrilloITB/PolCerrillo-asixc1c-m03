import re
def demanar_dades():
    dades = input()
    word_count(dades)
def word_count(dades):
    dades = dades.lower()
    dades = re.sub(r'[^\w\s]', '', dades)
    dades = dades.split()
    dades = sorted(dades)
    paraules = {}
    for paraula in dades:
        if paraula in paraules:
            paraules[paraula] += 1
        else:
            paraules[paraula] = 1
    for paraula in paraules:
        print(paraula + ": " + str(paraules[paraula]))