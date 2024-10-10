somaidade = 0
mediaidade = 0
maioridadehomen = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print('------{}º PESSOA------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str (input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p ==1 and sexo in 'Mm':
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A media de idade do grupo é de {} anos'.format(mediaidade))
print('O homen mais velho tem {} anos e se chama {}'.format(maioridadehomen,nomevelho))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(totmulher20))
