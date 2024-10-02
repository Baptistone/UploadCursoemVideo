n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão')
print('[ 1 ] Converter para Binário')
print('[ 2 ] Converter para Octal')
print('[ 3 ] Converter para Hexadecimal')
base = int(input('Sua opção: '))
if base == 1:
    print('{} Convertido para Binário é igual a {}'.format(n, bin(n)[2:]))
elif base == 2:
    print('{} Convertido para Octal é igual a {}'.format(n, oct(n)[2:]))
elif base == 3:
    print('{} Convertido para Hexadecimal é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção invalidá')
