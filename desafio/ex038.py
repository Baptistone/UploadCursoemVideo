n = int(input('Entre com primeiro valor = '))
n1 = int(input('Entre com segundo valor = '))
if n > n1:
    print('O primeiro valor é maior que o segundo {} > {}'.format(n, n1))
elif n1 > n:
    print('O segundo valor é maior que o primeiro {} > {}'.format(n1, n))
else:
    print('Os valores são iguais {} = {}'.format(n, n1))
