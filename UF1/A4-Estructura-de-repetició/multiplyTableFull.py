"""
Pol Cerrillo
21/11/2023
ASIXc1C M03 UF1
Descripció: Volem mostrar per pantalla les taules de multiplicar.
"""
for i in range(1, 10):
    for n in range(1, 10):
        if i*n <= 9:
            print("", i*n, end=" ")
        else:
            print(i*n, end=" ")
    print(" ")
