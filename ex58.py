#melhore o jogo do exercicio 28 onde o computador vai pensar em um numero de 0 até 10 e vai repetir até o usuario acertar e depois mostrar na tela quantas tentivas foram necessarias

from random import randint
from time import sleep

computador = randint(0, 10)
tentativas = 1

print('-=-' * 20)
print('Eu sou o computador e pensei em um número de 0 a 10.')
print('Tente adivinhar qual é!')
print('-=-' * 20)
sleep(0.5)

while True:
        # Solicita ao jogador que insira um número
        numero = int(input('Digite um número entre 0 e 10: '))
        print('PROCESSANDO...')
        sleep(0.5)

        # Verifica se o número digitado é igual ao número escolhido pelo computador
        if numero == computador:
                break  # Sai do loop se o jogador acertar

        # Se o número for diferente, o computador dá uma dica
        if numero < computador:
                print('O número que pensei é maior...')
        else:
                print('O número que pensei é menor...')

        tentativas += 1

# Quando o jogador acerta, exibe uma mensagem de parabéns
print('-=-' * 20)
print('Parabéns! Você acertou o número em {} tentativas.'.format(tentativas))
print('-=-' * 20)

