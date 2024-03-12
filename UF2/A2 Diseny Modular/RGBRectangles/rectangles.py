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
    comprobar_rectangle(matriu)

def comprobar_rectangle(matriu):
    for colors in matriu:
        colors = colors.lower().split()
        if colors[0] != "vermell" and colors[0] != "verd" and colors[0] != "blau":
            print("color desconegut")
            return False
        if not colors[1].isdigit() or not colors[2].isdigit():
            print("No son numeros enters")
            return False
        rectangles(matriu)

def rectangles(matriu):
    for rectangle in matriu:
        rectangle = rectangle.lower().split()
        color = rectangle[0]
        llargada = int(rectangle[1])
        amplada = int(rectangle[2])
        if color == 'vermell':
            color = vermell
        elif color == 'verd':
            color = verd
        elif color == 'blau':
            color = blau
        for i in range(llargada):
            for x in range(amplada):
                print(color + "X", end="")
            print()
        print()