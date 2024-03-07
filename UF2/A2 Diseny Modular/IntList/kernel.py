'''
Crear el mòdul kernel.py
Defineix, a dins del mòdul,  la funció readIntList que llegeixi per teclat i retorna una llista amb aquests enters.
Els enters són introduïts amb un espai de separació. El valor -1 indica que ja no hi ha més enters a llegir.
def readIntListFromKeyboard():
   numbers=[]
   #TODO: ...
   return numbers
Per provar la funció, fes un programa, al mòdul main.py, que llegeixi una llista d'enters i la imprimeixi per pantalla.
'''
def readIntListFromKeyboard():
   numbers=[]
   num = input().split()
   numbers = list((int, num.split()))
   if -1 in numbers:
       numbers = numbers[:numbers.index(-1)]
   return numbers
