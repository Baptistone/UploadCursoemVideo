km = float(input('Qual a distancia que irá viajar?: '))
print('Você irá realizar uma viagem de {}'.format(km))
print('para viagem de até 200 km o custo por km é igual a 0,50 acima fica por 0,45 por km')
if km <= 200:
    custokm1 = km*0.50
    print('O custo da sua viagem será R${:.2f}'.format(custokm1))
else:
    custokm2 = km*0.45
    print('O custo da sua viagem será R${:.2f}'.format(custokm2))
