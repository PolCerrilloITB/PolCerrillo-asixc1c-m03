import systemColors
vermell = systemColors.CRED
verd = systemColors.CGREEN
blau = systemColors.CBLUE
def dades():
    matriu = []
    colors = input()
    while colors != ';Q':
        matriu.append(colors)
        colors = input()
    rectangles(matriu)

def rectangles(matriu):
    for colors in matriu:
        colors = colors.lower().split()
        llargada = int(colors[1])
        amplada = int(colors[2])
        color = colors[0]
        if color == 'Red':
            color = vermell
        elif color == 'Green':
            color = verd
        elif color == 'Blue':
            color = blau
        for i in range(llargada):
            for x in range(amplada):
                print(color + "X", end="")
            print()
        print()