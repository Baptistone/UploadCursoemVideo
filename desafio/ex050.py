soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o valor {}: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Voce informou {} numeros e a soma deles foi {}'.format(cont,soma))
