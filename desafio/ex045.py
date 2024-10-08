from time import sleep
from random import randint
itens = ('pedra', 'papel', 'tesoura')
lista = randint(0, 2)
print('-=-'*20)
print('JOKENPO!!!')
print('-=-'*20)
print('''Escolha uma opção
      [0] Pedra
      [1] Papel
      [2] Tesoura''')
opcao = int(input('Qual é sua jogada? '))
print('JO!')
sleep(1)
print('KEN!!')
sleep(1)
print('PO!!!')
sleep(1)
if opcao == 0 or opcao == 1 or opcao == 2:
    print('A maquina jogou {}'.format(itens[lista]))
    print('Jogador jogou {}'.format(itens[opcao]))
else:
    print('Opcao escolhida invalida')
if lista == 0:
    if opcao == 0:
        print('Empatou!!')
    elif opcao == 1:
        print('O JOGADOR GANHOU!!')
    elif opcao == 2:
        print('O JOGADOR PERDEU!!')
    else:
        print('Opcao escolhida invalida')
elif lista == 1:
    if opcao == 0:
        print('O JOGADOR PERDEU!!')
    elif opcao == 1:
        print('EMPATE')
    elif opcao == 2:
        print('O JOGADOR GANHOU!!')
    else:
        print('Opcao escolhida invalida')
elif lista == 2:
    if opcao == 0:
        print('O JOGADOR GANHOU!!')
    elif opcao == 1:
        print('O JOGADOR PERDEU!!')
    elif opcao == 2:
        print('EMPATE')
    else:
        print('Opcao escolhida invalida')
