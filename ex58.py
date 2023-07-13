#melhore o jogo do exercicio 28 onde o computador vai pensar em um numero de 0 até 10 e vai repetir até o usuario acertar e depois mostrar na tela quantas tentivas foram necessarias

from random import randint
from time import sleep
computador = randint (0,10)
tentativas = 1

print('-=-'*20)
print('Eu sou o cumputador e pensei em um número, será que voce consegue adivinhar? ')
print('-=-'*20)
sleep(0.5)
numero = int(input('Digite um número para adivinhar: '))
print('-=-'*20)
print('PROCESSANDO')
sleep(0.5)

while computador != numero:
        print('GANHEI!Você não acertou HAHA!')
        numero = int(input('Tente novamente adivinha o número: '))
        tentativas += 1

print('Parabéns você acertou o número, você é incrível! e só precidou de {} tentativas '.format(tentativas))
