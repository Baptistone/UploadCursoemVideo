import random
a1 = str(input('Informe o Nome do 1 aluno: '))
a2 = str(input('Informe o Nome do 2 aluno: '))
a3 = str(input('Informe o Nome do 3 aluno: '))
a4 = str(input('Informe o Nome do 4 aluno: '))
lista = [a1, a2, a3, a4]
sorteio = random.choice(lista)
print('O aluno sorteado para Limpar a sala é: {}'.format(sorteio))
