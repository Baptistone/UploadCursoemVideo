import random
a1 = str(input('Informe o Nome do 1: '))
a2 = str(input('Informe o Nome do 2: '))
a3 = str(input('Informe o Nome do 3: '))
a4 = str(input('Informe o Nome do 4: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem da apresentação será {}'.format(lista))
