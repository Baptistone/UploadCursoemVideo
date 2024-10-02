casa = float(input('Qual o  valor da casa?? R$'))
salario = float(input('Qual salario do comprador?? R$'))
tempo = int(input('Quanto tempo de financiamento??'))
prestacao = casa / (tempo * 12)
minimo = salario * 30 / 100
print('Analisando')
print('O valor da sua casa é de {} e você deseja pagar a casa em {} anos'.format(
    casa, tempo), end='')
print('O valor da mensalidade será de {:.2f}.'.format(prestacao))
if prestacao <= minimo:
    print('\033[7;32;46mEmpréstimo Concedido\033[m')
else:
    print('\033[7;31;46mEmprestimo negado\033[m')
