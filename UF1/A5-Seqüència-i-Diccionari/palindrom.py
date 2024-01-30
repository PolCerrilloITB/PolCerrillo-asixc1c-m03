"""
Pol Cerrillo
30/01/2024
ASIXc1C M03 UF1
Descripció: Indica si una paraula o frase és palíndrom.
"""
try:
    frase = input().lower()
    fraseNormal = []
    fraseReves = []
    for x in frase:
        if x != " " and x != "." and x != "," and x != "’":
            if x == "à" or x == "á":
                x = "a"
            elif x == "è" or x == "é":
                x = "e"
            elif x == "í":
                x = "i"
            elif x == "ò" or x == "ó":
                x = "o"
            elif x == "ú":
                x = "u"
            fraseNormal.append(x)
    fraseReves.append(fraseNormal[-1::-1])
    print(fraseReves)
    print(fraseNormal)
    if fraseReves[0] == fraseNormal:
        print("Es palindrom.")
    else:
        print("No es palindrom.")
except:
    print("Error")