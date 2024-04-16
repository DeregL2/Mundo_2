# Solicita ao usuário que insira dois valores
numero = int(input('Digite o Primeiro Valor: '))
numero1 = int(input('Digite o Segundo Valor: '))
seletor = 0

# Loop principal do programa, continua até que o usuário selecione a opção 5 para sair
while seletor != 5:
    print('\n')
    print('Digite 1 para somar os Dois Valores!')
    print('Digite 2 para Multiplicar os Dois Valores!')
    print('Digite 3 para Solicitar o Maior número inserido!')
    print('Digite 4 para colocar novos números!')
    print('Digite 5 Para SAIR do programa!')
    print('\n')

    # Solicita ao usuário que insira a opção desejada
    seletor = int(input('Digite o valor Desejado:'))

    # Verifica se a opção selecionada está dentro do intervalo de 1 a 5
    if seletor >= 1 and seletor <= 5:
        if seletor == 1:
            # Soma os dois valores e exibe o resultado
            soma = numero + numero1
            print('O resultado da soma dos Dois valores é {}'.format(soma))
        elif seletor == 2:
            # Multiplica os dois valores e exibe o resultado
            soma = numero * numero1
            print('O resultado da Multiplicação dos DOis valores é de {}'.format(soma))
        elif seletor == 3:
            # Verifica qual dos valores é o maior e exibe-o
            if numero > numero1:
                print('O maior valor inserido é {}'.format(numero))
            else:
                print('O maior valor inserido é {}'.format(numero1))
        elif seletor == 4:
            # Solicita ao usuário que insira novos valores
            numero = int(input('Digite o Primeiro Valor: '))
            numero1 = int(input('Digite o Segundo Valor: '))
