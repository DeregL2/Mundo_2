#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
numero = 0
contador = 0
soma = 0
while True:
    numero = int(input('Digite um valor desejado: '))
    contador +=1
    soma += numero
    if numero == 999:
        soma2= soma - 999
        contador2 = contador - 1
        break
print('Você digitou {} números e a soma de todos eles foi de {}'.format(contador2,soma2))

# jeito guanabara
num = soma = cont = 0
num = int(input('Digite um valor desejado: ')) #flag
while num != 999: # verifica se o numero inserido e diferente de 999
    soma += num
    cont += 1
    num = int(input('Digite um valor desejado: ')) #elimina a flag como ultima linha
print('Você digitou {} números e a soma de todos eles foi de {}'.format(cont,soma))