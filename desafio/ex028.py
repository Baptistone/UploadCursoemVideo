from random import randint
from time import sleep
# gera um valor random de 0 a 5
lista = randint(0, 5)
print('==#=='*28)
print('Vou pensar em um número entre 0 e 5. Em qual estou pensando??')
print('==#=='*28)
# entrada do valor do usuario
vu = int(input('Em que número estou pensando??: '))
print('processando.....')
sleep(2)
# se valor escolhido foi maior que 5 irá inciar o jogo
if vu <= 5:
    # se o valor for igual que a maquina escolheu irá soltar a mensagem abaixo
    if vu == lista:
        print('Parabéns você ganhou!!: Seu numero {}, Numero da maquina{} '.format(
            vu, lista))
    # senao o valor for diferente que a maquina escolheu irá soltar a mensagem abaixo
    else:
        print('HaHa Ganhei pensei em outro numero: Seu numero {}, Numero da maquina{}'.format(
            vu, lista))
# senao irá solta a mensagem abaixo
else:
    print('O valor escolhido foi maior que 5. Valor escolhido{}'.format(vu))
