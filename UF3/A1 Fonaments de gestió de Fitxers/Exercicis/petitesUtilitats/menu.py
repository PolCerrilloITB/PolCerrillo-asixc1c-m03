import utilitat1
import utilitat2
import utilitat3
import utilitat4
import mixUtilitats
def escoger_opcion():
    print("1 - Signes puntuació - Quantitat")
    print("2 - Signes puntuació - Posició")
    print("3 - Text - Codificar")
    print("4 - Text - Descodificar")
    print("5 - Executar totes les utilitats")
    print("6 - Sortir de l'aplicacio")

    opcion = int(input("Selecciona una opción: "))
    return opcion
def ejecutar_opcion(opcion):
    comprobar = True
    while comprobar:
        if opcion == 1:
            utilitat1.calcular_letras()
        elif opcion == 2:
            utilitat2.calcular_consvoc()
        elif opcion == 3:
           utilitat3.codificar_frase()
        elif opcion == 4:
            utilitat4.cambiar_color()
        elif opcion == 5:
            mixUtilitats.ejectutar_utilidades()
        elif opcion == 6:
            print("Saliendo de la aplicación...")
            comprobar = False
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")