a = int(input('Entre com primeiro valor: '))
b = int(input('Entre com segundo valor: '))
c = int(input('Entre com terceiro valor: '))
menor = a
# Verificar o menor valor
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificar o maior valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
# Print o resultado localizado
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))
