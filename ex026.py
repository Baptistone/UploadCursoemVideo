nome = str(input('Digite um frase: ')).strip().lower()
print('A letra A apareceu {} vezes na frase.'.format(nome.count('a')))
print('A primeira letra A apareceu na posição {}'.format(nome.find('a')))
print('O ultima letra A apareceu na posição {}'.format(nome.rfind('a')))
