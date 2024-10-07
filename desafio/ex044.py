compra = float(input('Qual o valor da sua compra? '))
print('''FORMAS DE PAGAMENTO
      [1] à Vista dinheiro / cheque
      [2] à vista no cartao
      [3] 2 x no cartao
      [4] 3 x ou mais no cartão''')
pagamento = int(input('Qual é a opcao?'))
if pagamento == 1:
    total = compra - (compra*10/100)
    print('Sua compra de R${:.2f} vai custar R${:.2f}.'.format(compra, total))
elif pagamento == 2:
    total = compra - (compra*5/100)
    print('Sua compra de R${:.2f} vai custar R${:.2f}.'.format(compra, total))
elif pagamento == 3:
    total = compra
    print('Sua compra de R${:.2f} vai custar R${:.2f}.'.format(compra, total))
elif pagamento == 4:
    total = compra + (compra*20/100)
    print('Sua compra de R${:.2f} vai custar R${:.2f}.'.format(compra, total))
else:
    print('Opcao invalida')
