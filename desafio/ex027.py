nome = str(input('Qual é seu nome completo? ')).strip().split()
print('Analisando seu nome {}......'.format(nome))
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {} '.format(nome[len(nome)-1]))
