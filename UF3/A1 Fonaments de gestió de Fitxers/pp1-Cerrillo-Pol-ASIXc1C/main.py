'''
Pol Cerrillo
09/05/2023
ASIXc1C M03 UF3
Descripció:Crear un programa per processar el fitxer de text anomenat paraules.txt per dur
a terme les tasques que es detallen més endavant.
'''
import time
import log
import processar_arxius
def main():
    cont_s = time.time()
    log.info_log()
    processar_arxius.llegir_fitxer()
    print('El archivo se ha procesado')
    cont_f = time.time()
    duracion = cont_f - cont_s
    log.final_log(duracion)
main()