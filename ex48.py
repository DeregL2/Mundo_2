# Faça um programa que calcule a SOMA entre todos os NÚMEROS IMPARES que são MULTIPLOS DE TRÊS  a que se encontram no intervalo de 1 até 500!

# Inicializa as variáveis de soma e contagem
cont = 0
soma = 0

# Loop for que itera sobre todos os números ímpares no intervalo de 1 a 500
for i in range(1, 501, 2):
    # Verifica se o número atual é um múltiplo de três
    if i % 3 == 0:
        # Se for, adiciona o número à soma
        soma = soma + i
        # Incrementa o contador de números ímpares múltiplos de três
        cont = cont + 1

# Exibe a soma total e a contagem de números
print('A soma é {} dos {} números'.format(soma, cont))
