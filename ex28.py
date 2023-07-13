from random import randint
from time import sleep

computador = randint(0,5)

print('Descubra o número que estou pensando\n')

sleep(1)
numero = int(input('Digite o número que você acha que eu pensei: '))
sleep(1)

print('Processando...')
sleep(1)

if numero == computador:
    print('Parabés você acertou o número!!!')
else:
    print('Que pena! Você errou! pensei no número {}'.format(computador))