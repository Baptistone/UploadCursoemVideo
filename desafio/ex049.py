n = int(input('Entre com valor para fazer a sua tabuada: '))
for c in range(0, 11):
    print('{:2} X {:2} = {:2}'.format(n, c, (c*n)))
