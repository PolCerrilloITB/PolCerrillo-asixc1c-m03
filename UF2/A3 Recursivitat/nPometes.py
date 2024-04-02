'''
Pol Cerrillo
02/04/2023
ASIXc1C M03 UF1
Descripció:Volem fer un programa que escrigui la cançó de
N pometes té el pomer (és repeteix fins a que ja no queden pomes)
'''
def getAppleSongStanza(applesCount):
    stanza = f"{applesCount} pometes té el pomer,\n" \
             f"de {applesCount} una, de {applesCount} una,\n" \
             f"{applesCount} pometes té el pomer,\n" \
             f"de {applesCount} una en caigué.\n" \
             f"Si mireu el vent d'on vé\n" \
             f"veureu el pomer com dansa,\n" \
             f"si mireu el vent d'on vé\n" \
             f"veureu com dansa el pomer."
    return stanza
def getAppleSongStanzaIndividual(applesCount):
    stanza = f"{applesCount} poma té el pomer,\n" \
             f"de {applesCount} una, de {applesCount} una,\n" \
             f"{applesCount} poma té el pomer,\n" \
             f"de {applesCount} una en caigué.\n" \
             f"Si mireu el vent d'on vé\n" \
             f"veureu el pomer com dansa,\n" \
             f"si mireu el vent d'on vé\n" \
             f"veureu com dansa el pomer."
    return stanza
def getAppleSong(applesCount):
    if applesCount == 0:
        return ""
    elif applesCount == 1:
        return getAppleSongStanzaIndividual(applesCount) + "\n" +getAppleSong(applesCount-1)
    else:
        return getAppleSongStanza(applesCount) + "\n" +getAppleSong(applesCount -1)
def main():
    print(getAppleSong(int(input())))
main()

