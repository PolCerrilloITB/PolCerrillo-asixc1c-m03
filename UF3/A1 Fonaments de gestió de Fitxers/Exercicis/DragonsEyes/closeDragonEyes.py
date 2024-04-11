'''
Pol Cerrillo
11/04/2024
ASIXc1C M03 UF3
Descripció:Llegir el fitxer Dragon.in i crear el fitxer de sortida DragonEyesClosed.out amb el mateix contingut.
Però caldrà haver canviar prèviament els ulls del drac que al fitxer d'entrada estan oberts 0    0 , i al de
sortida hauran d'estar tancats X    X  o també per uns '👁' '👁'
'''
def fitxerDrac():
    contingut = ''
    f = open('Dragon.in', mode='rt', encoding='utf-8')
    changelinia = f.readline()
    contingut += changelinia
    while changelinia != '':
        changelinia = f.readline()
        contingut += changelinia
    f.close()
    return contingut
def canviulls(contingut):
    x = open('DragonEyesClosed.out', mode='w', encoding='utf-8')
    for changelinia in contingut:
        if '0' in changelinia:
            x.write(changelinia.replace('0', 'X'))
        else:
            x.write(changelinia)
    x.close()
