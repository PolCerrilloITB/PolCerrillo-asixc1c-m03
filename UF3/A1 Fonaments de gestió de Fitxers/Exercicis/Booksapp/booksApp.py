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
def guardar_llibres():
    cllibres = int(input("Quantitat llibres: "))
    llibres = []
    for _ in range(cllibres):
        titol = input("Títol del llibre: ")
        autor = input("Autor del llibre: ")
        npagines = int(input("Nombre de pàgines: "))
        llibres.append((titol, autor, npagines))
    with open("books.out", "w") as file:
        for llibre in llibres:
            file.write(f"Llibres\n")
            file.write(f"-----------\n")
            file.write(f"{llibre[0]},{llibre[1]},{llibre[2]}\n")
    return llibres, cllibres
def mostrar_llibres(llibres):
    print("\nLlista de llibres:")
    for i, llibre in enumerate(llibres, 1):
        print(f"{i}. Títol: {llibre[0]}, Autor: {llibre[1]}, Pàgines: {llibre[2]}")

    print(f"\nTotal llibres: {len(llibres)}")

    llibreC = min(llibres, key=lambda x: x[2])
    llibreL = max(llibres, key=lambda x: x[2])

    print(f"Llibre més curt: {llibreC[0]} ({llibreC[2]} pàgines)")
    print(f"Llibre més llarg: {llibreL[0]} ({llibreL[2]} pàgines)")



