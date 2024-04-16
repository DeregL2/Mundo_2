#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
# Inicializa as variáveis
cont = 0  # Contador para contar quantos números foram inseridos
soma = 0  # Variável para armazenar a soma de todos os valores
maior = menor = 0  # Variáveis para armazenar o maior e o menor valor inserido

# Loop para continuar solicitando valores até que o usuário decida parar
while True:
    num = int(input('Digite um valor desejado: '))
    cont += 1  # Incrementa o contador

    # Soma o valor inserido ao total
    soma += num

    # Verifica se é o primeiro valor inserido para inicializar maior e menor
    if cont == 1:
        maior = menor = num
    else:
        # Compara o valor inserido com o maior e o menor atual
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    # Pergunta ao usuário se deseja continuar inserindo valores
    s = str(input('Deseja continuar? [S/N]: ')).upper()

    # Verifica a resposta do usuário e decide se continua o loop ou não
    if s == 'N':
        break

# Calcula a média dos valores inseridos
media = soma / cont

# Exibe o resultado final
print(
    'A média entre todos os valores foi de {}, o maior número inserido foi {} e o menor número inserido foi {}'.format(
        media, maior, menor))
