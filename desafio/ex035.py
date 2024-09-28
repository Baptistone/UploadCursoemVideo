from time import sleep
print('-='*20)
print('\033[7;31;46mAnalisandor de triângulos\033[m')
print('-='*20)
r1 = float(input('Primeira segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))
print('processando.....')
sleep(2)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1+r2:
    print('Os segmento acima pode forma um triangulo')
else:
    print('Os segmento acima não podem gerar um triangulo')
