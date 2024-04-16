#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato.

# Inicialização das variáveis para as estatísticas
barato = ''  # Nome do produto mais barato
tot = cont = menor = 0  # Inicialização do total gasto, quantidade de produtos e menor preço

# Loop infinito para permitir a entrada de múltiplos produtos
while True:
    nome = str(input('Qual o nome do produto?: '))  # Solicitação do nome do produto
    preco = float(input('Qual o preço do produto?: '))  # Solicitação do preço do produto
    cont += 1  # Atualização do contador de produtos
    tot += preco  # Atualização do total gasto

    # Verificando se o preço do produto é maior ou igual a R$ 1000
    if preco >= 1000:
        cont += 1  # Se sim, incrementa o contador de produtos com preço maior ou igual a R$ 1000

    # Verificando se é o primeiro produto ou se o preço atual é menor que o menor preço anteriormente registrado
    if cont == 1 or preco < menor:
        menor = preco  # Atualiza o menor preço com o preço atual
        barato = nome  # Atualiza o nome do produto mais barato com o nome atual

    # Perguntando ao usuário se deseja continuar adicionando produtos
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]  # Obtém a resposta e a converte para maiúsculas
        print('-'*30)
    if resp == 'N':
        break  # Se a resposta for 'N', sai do loop

# Exibição das estatísticas finais
print(f'Total gasto: {tot}')
print(f'O produto mais barato é {barato} e custou: {menor}')
print(f'{cont} custam mais de R$ 1000,00')
