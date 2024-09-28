v = float(input('Em qual velocidade estava andando? '))
multa = (v-80) * 7
if v > 80:
    print('Você ultrapassou o limite permitido de 80 km')
    print('Você irá receber uma multa no valor de R${:.2f}'.format(multa))
else:
    print('Você está dirigindo no limite permitido, tenha um otimo dia!!')
