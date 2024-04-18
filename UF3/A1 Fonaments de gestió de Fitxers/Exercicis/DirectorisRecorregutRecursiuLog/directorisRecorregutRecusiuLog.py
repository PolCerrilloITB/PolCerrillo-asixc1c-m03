'''
Pol Cerrillo
18/04/2024
ASIXc1C M03 UF3
Descripció: Modificar l'exemple Recorregut de directoris recursiu, per a controlat els possibles errors.
Anotar en un fitxer error.log, els errors trobats (només)
'''
import os
def recorrer_arbol_directorios(directorio, archivo_log):
    try:
       # Obtener la lista de archivos y directorios en el directorio actual
       contenido = os.listdir(directorio)
       # Recorrer cada elemento del directorio actual
       for elemento in contenido:
           # Crear la ruta completa del elemento
           ruta_elemento = os.path.join(directorio, elemento)
           # Si el elemento es un directorio, recorrer recursivamente
           if os.path.isdir(ruta_elemento):
               print("Directorio:", ruta_elemento)
               recorrer_arbol_directorios(ruta_elemento)
           else:
               print("Archivo:", ruta_elemento)
    except Exception as e:
        with open(archivo_log, 'a') as log:
            log.write(f"Error: {str(e)} en el directorio {directorio}\n")
# Función principal
def main():
   # Solicitar al usuario el directorio inicial
   directorio_inicial = input("Introduce la ruta del directorio inicial: ")
   # Verificar si el directorio ingresado existe
   if not os.path.isdir(directorio_inicial):
       print("El directorio especificado no existe.")
   else:
       # Llamar a la función recursiva para recorrer el árbol de directorios
       print("\nRecorrido del árbol de directorios:")
       archivo_log = "error.log"
       recorrer_arbol_directorios(directorio_inicial, archivo_log)