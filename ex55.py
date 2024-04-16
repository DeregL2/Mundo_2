#Faça um programa que leia o peso de cinco pessoas. No final , mostre qual foi o maior e o menor peso lidos.

# Inicializa as variáveis maior e menor com o primeiro peso informado
peso = float(input('Escreva o peso da 1ª pessoa: '))
maior = peso
menor = peso

# Loop for que itera sobre as cinco pessoas
for i in range(2, 6):
    peso = float(input('Escreva o peso da {}ª pessoa: '.format(i)))

    # Verifica se o peso atual é o maior ou o menor
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

# Exibe o maior e o menor peso lidos
print('O maior peso lido foi {} kg'.format(maior))
print('O menor peso lido foi {} kg'.format(menor))
