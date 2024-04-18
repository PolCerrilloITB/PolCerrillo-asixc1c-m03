'''
Pol Cerrillo
18/04/2024
ASIXc1C M03 UF3
Descripció: Modificar l'exemple Recorregut de directoris recursiu, per a controlat els possibles errors.
Anotar en un fitxer error.log, els errors trobats (només)
'''
import os
def recorrer_arbol_directorios(directorio):
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
       recorrer_arbol_directorios(directorio_inicial)
if __name__ == "__main__":

   main()