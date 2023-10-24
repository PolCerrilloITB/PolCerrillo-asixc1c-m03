"""
Pol Cerrillo
24/10/2023
ASIXc1C M03 UF1
Descripció: Dies en un mes
"""

mes = input("Quin mes vols?")
match mes:
    case"1": print("Te 31 dias el mes", mes)
    case"2": print("Te 28 dias el mes", mes)
    case"3": print("Te 31 dias el mes", mes)
    case"4": print("Te 30 dias el mes", mes)
    case"5": print("Te 31 dias el mes", mes)
    case"6": print("Te 30 dias el mes", mes)
    case"7": print("Te 31 dias el mes", mes)
    case"8": print("Te 31 dias el mes", mes)
    case"9": print("Te 30 dias el mes", mes)
    case"10": print("Te 31 dias el mes", mes)
    case"11": print("Te 30 dias el mes", mes)
    case"12": print("Te 31 dias el mes", mes)
    case _: print("Error")
