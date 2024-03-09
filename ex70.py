#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato.
barato = ''
tot = cont = menor = 0
while True:
    nome = str(input('Qual o nome do produto?: '))
    preco = float(input('Qual o preço do produto?: '))
    cont += 1
    tot += preco 
    if preco >= 1000:
        cont += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]  
        print('-'*30)
    if resp == 'N':
        break   
print(f'Total gasto: {tot}')
print(f'o produto mais barato e {barato} e custou : {menor}')
print(f'{cont} Custam mais de R$ 1000,00')