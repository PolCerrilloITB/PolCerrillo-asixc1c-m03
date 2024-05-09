'''
Pol Cerrillo
09/05/2023
ASIXc1C M03 UF3
Descripció:Crear 5 fitxers per guardar les paraules que acaben en: ing, itb, tic, tica i ció
(amb accent). Es a dir, s'ha de crear els fitxers: paraules-ing.txt, paraules -itb.txt,
paraules-tic.txt, paraules-tica.txt, paraules-cio.txt
'''
import os

ING = ['g']
ITB = ['b']
TIC = ['c']
TICA = ['a']
CIO = ['ó']
DIR_PARAULES = os.path.join(".", "paraules")
#Lectura de les linieas
def llegir_paraules(frase):
    fraseSplit = frase.split()
    frase_final = ""
    for palabra in fraseSplit:
        if palabra[-1] in ING:
            frase_final = palabra
            os.makedirs(DIR_PARAULES, exist_ok=True)
            output_file_path = os.path.join(DIR_PARAULES, "paraules-ing.txt")
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.writelines(frase_final)
            f.close()
        elif palabra[-1] in ITB:
            frase_final = palabra
            os.makedirs(DIR_PARAULES, exist_ok=True)
            output_file_path = os.path.join(DIR_PARAULES, "paraules-itb.txt")
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.writelines(frase_final)
            f.close()
        elif palabra[-1] in TIC:
            frase_final = palabra
            os.makedirs(DIR_PARAULES, exist_ok=True)
            output_file_path = os.path.join(DIR_PARAULES, "paraules-tic.txt")
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.writelines(frase_final)
            f.close()
        elif palabra[-1] in TICA:
            frase_final = palabra
            os.makedirs(DIR_PARAULES, exist_ok=True)
            output_file_path = os.path.join(DIR_PARAULES, "paraules-tica.txt")
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.writelines(frase_final)
            f.close()
        elif palabra[-1] in CIO:
            frase_final = palabra
            os.makedirs(DIR_PARAULES, exist_ok=True)
            output_file_path = os.path.join(DIR_PARAULES, "paraules-cio.txt")
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.writelines(frase_final)
            f.close()
        else:
            frase_final = " "
    return frase_final, frase
# Funció per procesar apóstros i guions a les paraules.
def apostrofe_guion(palabra):
    if "'" in palabra or "-" in palabra:
        if "'" in palabra:
            palabra = palabra.replace("'", "").replace("'", "")
        elif "-" in palabra:
            palabra = palabra.replace("-", "").replace("-", "")
    if len(palabra) > 1 and palabra[-1] in ["'", "-"]:
        palabra = palabra[:-1] + palabra[-1] + palabra[-1]
    return palabra