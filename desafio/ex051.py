print('=' * 100)
print('                 10 TERMOS DE UMA PA')
print('=' * 100)
termo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
dec = termo + (10-1) * razao
for c in range(termo,dec,razao):
    print('{} '.format(c), end=' -> ')
print('fim')
