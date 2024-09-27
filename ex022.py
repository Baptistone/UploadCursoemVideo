nome = str(input('Entre com seu nome completo: ')).strip()
print('Seu nome em Letra Maiuscula é {}'.format(nome.upper()))
print('Seu nome em Letra Minuscula é {}'.format(nome.lower()))
print('Seu nome tem {} caracteres'.format(len(nome)-nome.count(' ')))
nome2 = nome.find(' ')
print('Seu Primeiro nome é {}'.format(nome2))
separa = nome.split()
print('Seu Primeiro nome é {} e tem {} careteres'.format(
    separa[0], len(separa[0])))
