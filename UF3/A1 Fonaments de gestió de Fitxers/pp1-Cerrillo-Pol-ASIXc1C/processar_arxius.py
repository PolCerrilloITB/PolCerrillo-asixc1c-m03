'''
Pol Cerrillo
09/05/2023
ASIXc1C M03 UF3
Descripció:Crear un programa per processar el fitxer de text anomenat paraules.txt per dur
a terme les tasques que es detallen més endavant.
'''
import os
import tasca1
# DIR_ENTRADA = os.path.join(".", "entrada")
FILE = 'paraules.txt'
DIR_PARAULES = os.path.join(".", "paraules")

def llegir_fitxer():
    try:
        with open(FILE, 'r', encoding='utf-8') as f:
            linies = f.readlines()
        f.close()
        #TODO fer que hi vagi cap al fitxer tasca1 sense donar errors
#                linies_arxiu = [tasca1.llegir_paraules(linia) + '\n' for linia in linies]
#                escriptura_fixers_corresponents(linies_arxiu, arxiu)
        return linies
    except:
        print('No hi ha cap fitxer (paraules.txt)')
# TODO fer que la def escriptura_fitxers corresponents
#  s'utilitci per poder crear els fitxers de la tasca 1
'''
def escriptura_fixers_corresponents(frase, arxiu):
    os.makedirs(DIR_PARAULES, exist_ok=True)
    output_file_path = os.path.join(DIR_PARAULES, FILE + '-')
'''