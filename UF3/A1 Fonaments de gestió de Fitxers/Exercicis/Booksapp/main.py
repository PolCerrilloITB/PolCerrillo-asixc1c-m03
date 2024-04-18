import booksApp
def main():
    llibres = booksApp.guardar_llibres()
    booksApp.mostrar_llibres(llibres)
if __name__ == "__main__":
    main()