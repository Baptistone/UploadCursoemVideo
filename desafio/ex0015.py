d = int(input('Quantos dias alugados? '))
k = float(input('Quantos Km rodados?'))
vs = (d*60)+(k*0.15)
print('Valor a pagar do aluguel é de R${:.2f}'.format(vs))
