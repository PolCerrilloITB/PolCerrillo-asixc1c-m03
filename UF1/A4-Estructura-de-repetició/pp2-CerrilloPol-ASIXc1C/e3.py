"""
Pol Cerrillo
14/12/2023
ASIXc1C M03 UF1
Descripció: Taulell que canvia la columna sencera i la fila sencera per un asterisc
"""
try:
    #Variables definides per la fila, columna i asterisc
    fil = int(input("Fila?"))
    col = int(input("Columna?"))
    ast = "*"
    #Que printi les files corresponents
    for x in range(8):
        print(end="")
    # Posar que es repetixi y vegades, i printi les vegades adequades
        for y in range(8):
            if fil == x and col == y:
                print(ast, end=" ")
            elif (x + y) % 2 == 0:
                print("B", end=" ")
            else:
                print("N", end=" ")
        print()
except:
    print("Un numero si us plau")