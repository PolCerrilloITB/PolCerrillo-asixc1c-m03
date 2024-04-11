'''
Pol Cerrillo
11/04/2024
ASIXc1C M03 UF3
Descripció:Llegir el fitxer Knights.in i crear el fitxer de sortida KnightEyesClosed.out amb el mateix contingut.
Però caldrà, haver canviat prèviament, els ulls del cavaller que al fitxer d'entrada estan oberts 0   0 , i
al de sortida hauran d'estar tancats -    - o també per uns '👁' '👁'
'''
def fitxerKnight():
    contingut = ''
    f = open('Knights.in', mode='rt', encoding='utf-8')
    changelinia = f.readline()
    contingut += changelinia
    while changelinia != '':
        changelinia = f.readline()
        contingut += changelinia
    f.close()
    return contingut
def canviulls(contingut):
    x = open('KnightsEyesClosed.out', mode='w', encoding='utf-8')
    for changelinia in contingut:
        if '0' in changelinia:
            x.write(changelinia.replace('0', '-'))
        else:
            x.write(changelinia)
    x.close()