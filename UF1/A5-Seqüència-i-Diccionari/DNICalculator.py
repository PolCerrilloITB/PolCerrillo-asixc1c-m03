"""
Pol Cerrillo
16/01/2024
ASIXc1C M03 UF1
Descripció: L’objectiu d’aquest exercici és crear un programa per calcular  la lletra del DNI.
A la Web del Ministerio del Interior es pot trobar l’explicació de com fer-ho.
Els passos a seguir, bàsicament són:
Es divideix el nombre entre 23 i la resta se substitueix per una lletra que es determina per
inspecció mitjançant la següent taula:
"""
try:
    dni = int(input())
    if len(str(dni)) == 8:
        lletra = {
            0:"T",
            1:"R",
            2:"W",
            3:"A",
            4:"G",
            5:"M",
            6:"Y",
            7:"F",
            8:"P",
            9:"D",
            10:"X",
            11:"B",
            12:"N",
            13:"J",
            14:"Z",
            15:"S",
            16:"Q",
            17:"V",
            18:"H",
            19:"L",
            20:"C",
            21:"K",
            22:"E"
        }
        residu = dni % 23
        print(lletra[residu])
    else:
        print("Longitud incorrecta")
except:
    print("Numeros!!!")