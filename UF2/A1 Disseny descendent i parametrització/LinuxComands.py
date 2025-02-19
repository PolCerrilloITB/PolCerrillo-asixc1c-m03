"""
Pol Cerrillo
20/02/2024
ASIXc1C M03 UF2
Descripció: Al ITB s'està creant un nou sistema operatiu, basat el Linux. De moment,
només té unes poques comandes, donat que és una versió alfa.
Les comandes que es poden executar són:
touch
grep
cat
fdisk
cmp
dmesg
man
top
htop
halt   "Cas especial" Aquesta comanda aturarà el sistema, tot i que no l'apagarà
Les opcions que han de tenir implementades per aquesta versió són:
-h, --help
           Mostra un text d'ajuda i surt
 -v, --version
          Mostra la versió i surt
En cas de triar una opció no valida ha de mostrar el missatge: Value xx is not valid option BACALAO"
A on les xx ha de ser l'opció triada que no ha estat valida
"""
comandas = ['touch', 'grep', 'cat', 'fdisk', 'cmp', 'dmesg', 'man', 'top', 'htop', 'halt']
opcions = ['-h', '--help', '-v', '--version']
def columnes():
    while True:
        com = input().split()
        if len(com) == 2 and com[0] in comandas:
            if com[0] == 'halt':
                print("El programa s'aturara")
                exit(0)
            return com[0], com[1]
        else:
            print("Comanda", com, "no valida")
def mostrar_ayuda(comanda):
    print("Ayuda de ", comanda)
def mostrar_versio(comanda):
    print("Versió de ", comanda)
def main():
    while True:
        comanda, opcio = columnes()
        if comanda == "halt":
            break
        if opcions in ['-h', '--help']:
            mostrar_ayuda(comanda)
        else:
            mostrar_versio(comanda)
main()