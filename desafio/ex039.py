from datetime import date
ano = int(input('Em que ano voce nasceu? '))
atual = date.today().year
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print('Voce ainda não tem 18 anos. ainda faltam {} anos para o alistamento'.format(saldo))
    ano2 = atual + saldo
    print('Seu alistamento será em {} ano'.format(ano2))
elif idade > 18:
    saldo = idade - 18
    ano2 = atual - 18
    print('Voce ja deveria ter se alistado há {} anos'.format(saldo))
    print('Seu alistamento foi em {} ano'.format(ano2))
