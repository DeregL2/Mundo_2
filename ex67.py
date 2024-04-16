#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
# Inicializa o loop infinito
while True:
    # Solicita ao usuário que digite um número
    n = int(input('Quer ver a tabuada de qual valor? '))

    # Verifica se o número digitado é negativo para interromper o loop
    if n < 0:
        break

    # Exibe uma linha separadora
    print('=' * 30)

    # Loop para calcular e exibir a tabuada do número digitado
    for i in range(1, 11):
        # Calcula o resultado da multiplicação
        resultado = n * i
        # Exibe a linha da tabuada
        print(f'{n} X {i} = {resultado}')

    # Exibe uma linha separadora
    print('=' * 30)

# Exibe uma mensagem de fim de execução quando o loop é interrompido
print('Fim da execução')
