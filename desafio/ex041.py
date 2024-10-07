from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('O Nadador tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade >= 10 and idade <= 14:
    print('Classificação: INFANTIL')
elif idade >= 15 and idade <= 19:
    print('Classificação: JUNIOR')
elif idade >= 20 and idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')
