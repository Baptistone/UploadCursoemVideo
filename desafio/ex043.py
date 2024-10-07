peso = float(input('Qual seu peso? (KG)'))
altura = float(input('Qual sua altura? (M)'))
imc = peso / (altura**2)
print('O seu IMC é de {}'.format(imc))
if imc <= 18.5:
    print('Voce esta abaixo do peso')
elif 18.5 <= imc < 25:
    print('Voce esta no peso ideal')
elif 25 <= imc < 30:
    print('Voce esta com sobrepeso')
elif 30 <= imc < 40:
    print('Voce está com obesidade')
else:
    print('Voce está com obesidade Mórbida procure ajuda com urgencia!!!')
