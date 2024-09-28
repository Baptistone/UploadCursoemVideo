from datetime import date
ano = int(input('Que ano quer analisar, Caso queira o ano atual coloque 0? '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('O ano atual é BISSEXTO'.format(ano))
else:
    print('O ano atual não é BISSEXTO'.format(ano))
