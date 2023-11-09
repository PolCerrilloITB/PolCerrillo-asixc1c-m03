"""
Pol Cerrillo
24/10/2023
ASIXc1C M03 UF1
Descripció: Dies en un mes
"""

mes = input("Quin mes vols?")
match mes:
    case"1"|"3"|"5"|"7"|"8"|"10"|"12": print("Te 31 dias el mes", mes)
    case"2": print("Te 28 o 29 dias el mes", mes)
    case"4"|"6"|"9"|"11": print("Te 30 dias el mes", mes)
    case _: print("Error")