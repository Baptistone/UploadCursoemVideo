n1 = float(input('Entre Com sua primeira nota: '))
n2 = float(input('Entra Com sua Segunda nota:  '))
media = (n1 + n2) / 2
print('tirando a {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(
    n1, n2, media))
if media > 7:
    print('ALUNO ESTA APROVADO'.format(media))
elif media >= 5 and media < 7:
    print('ALUNO ESTA EM RECUPERACAO'.format(media))
elif media < 5:
    print('ALUNO ESTA REPROVADO'.format(media))
