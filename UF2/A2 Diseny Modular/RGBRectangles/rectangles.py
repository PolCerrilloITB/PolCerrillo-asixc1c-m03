import systemColors
vermell = systemColors.CRED
verd = systemColors.CGREEN
blue = systemColors.CBLUE
def dades():
    matriu = []
    colors = input()
    while matriu != ';Q':
        matriu.append(int(colors))
        colors = input()
    rectangles(matriu)

def rectangles(matriu):
    for colors in matriu:
        colors = colors.lower().split()
        llargada = colors[1]
        amplada = colors[2]
        colors = colors[0]
        if colors == 'Red':
            colors = vermell
        elif colors == 'Verd':
            colors = verd
        elif colors == 'Blue':
            colors = blue
        for i in range(llargada):
            for x in range(amplada):
                print(colors + 'x', end="")
            print()
        print()