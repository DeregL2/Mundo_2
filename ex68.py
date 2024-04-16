#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint  # Importa apenas a função randint da biblioteca random

print('-=-'*10)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=-'*10)

cont = 0  # Inicializa um contador para contar quantas vezes o jogador ganha

while True:  # Loop infinito para continuar o jogo até que o jogador decida parar
    n = int(input('Diga um valor: '))  # O jogador insere um valor
    pc = randint(1, 101)  # O computador "pensa" em um número de 1 a 100 (inclusive)
    soma = n + pc  # Soma os valores escolhidos pelo jogador e pelo computador
    escolha = str(input('PAR ou IMPAR? [P/I] ')).upper()  # O jogador escolhe PAR ou IMPAR

    if escolha == 'P':  # Se o jogador escolheu PAR
        if soma % 2 == 0:  # Se a soma dos valores é par
            print(f'Voce jogou {n} e o computador {pc}. Total deu {soma} DEU PAR')
            cont += 1  # Incrementa o contador de vitórias do jogador
        else:
            print(f'Voce jogou {n} e o computador {pc}. Total deu {soma} DEU IMPAR')
            print('VOCE PERDEU')  # Indica que o jogador perdeu
            break  # Sai do loop
    elif escolha == 'I':  # Se o jogador escolheu IMPAR
        if soma % 2 == 1:  # Se a soma dos valores é ímpar
            print(f'Voce jogou {n} e o computador {pc}. Total deu {soma} DEU IMPAR')
            cont += 1  # Incrementa o contador de vitórias do jogador
        else:
            print(f'Voce jogou {n} e o computador {pc}. Total deu {soma} DEU PAR')
            print('VOCE PERDEU')  # Indica que o jogador perdeu
            break  # Sai do loop

print(f'VOCE GANHOU UM TOTAL DE {cont}x')  # Exibe o total de vitórias do jogador

