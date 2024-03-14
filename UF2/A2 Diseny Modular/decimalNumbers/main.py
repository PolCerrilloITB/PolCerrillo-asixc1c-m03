'''
Pol Cerrillo
14/03/2024
ASIXc1C M03 UF2
Descripció: Volem fer un programa per mostrar en format digital, un número entrat per teclat
Números en format digital:
   #     #####   #####  #     # #######  #####  #######  #####   #####    ###
  ##    #     # #     # #     # #       #            #  #     # #     #  #   #
   #          #      ## #     # #####   #####       #    #####   ###### #     #
   #     #####        # #######      #  #     #    #    #     #       # #     #
   #    #       #     #       # #     # #     #   #     #     # #     #  #   #
 #####  #######  #####        #  #####   #####    #      #####   #####    ###
Input
207
Output
 #####    ###   #######
#     #  #   #       #
      # #     #     #
 #####  #     #    #
#        #   #    #
#######   ###     #
Input
-22
Output
       #####   #####
      #     # #     #
  ###       #       #
       #####   #####
      #       #
      ####### #######
EXTRA BONUS: Do the same, adding letters and punctuation marks. English alphabet only.
'''
import decimalNumbers
def main():
    decimalNumbers.demanar_numeros()
main()