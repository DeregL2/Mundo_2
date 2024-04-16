from random import randint  # Importa a função randint do módulo random
from time import sleep  # Importa a função sleep do módulo time

# Gera um número aleatório entre 0 e 5
computador = randint(0, 5)

# Imprime uma mensagem para o jogador
print('Descubra o número que estou pensando\n')

# Aguarda 1 segundo antes de continuar
sleep(1)

# Solicita ao jogador que digite um número
numero = int(input('Digite o número que você acha que eu pensei: '))

# Aguarda 1 segundo antes de continuar
sleep(1)

# Imprime uma mensagem de "Processando..." para criar suspense
print('Processando...')
sleep(1)

# Verifica se o número digitado pelo jogador é igual ao número escolhido pelo computador
if numero == computador:
    # Se forem iguais, o jogador acertou
    print('Parabéns! Você acertou o número!!!')
else:
    # Caso contrário, o jogador errou e o número escolhido pelo computador é revelado
    print('Que pena! Você errou! Eu pensei no número {}'.format(computador))
