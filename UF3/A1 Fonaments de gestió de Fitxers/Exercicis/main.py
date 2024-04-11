'''
Pol Cerrillo
11/04/2024
ASIXc1C M03 UF3
Descripció:Llegir el fitxer Dragon.in i crear el fitxer de sortida DragonEyesClosed.out amb el mateix contingut.
Però caldrà haver canviar prèviament els ulls del drac que al fitxer d'entrada estan oberts 0    0 , i al de
sortida hauran d'estar tancats X    X  o també per uns '👁' '👁'
'''
import closeDragonEyes

def main():
    contingut = closeDragonEyes.fitxerDrac()
    closeDragonEyes.canviulls(contingut)
main()