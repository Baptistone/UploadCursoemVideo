import math
cato = float(input('Entre com o valor do cateto oposto: '))
cata = float(input('Entre com o Valor do Cateto adjacente: '))
hipo = math.hypot(cato, cata)
print('A soma do cateto oposto {} com cateto adjacente {} igual a hipotenusa {} !!'.format(
    cato, cata, hipo))
