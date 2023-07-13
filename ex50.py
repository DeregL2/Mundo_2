#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daquela que forem pares. Se o valor digitado for ímpar . Desconsidere-o.

soma = 0
cont = 0
for i in range (1,7):
    num = int(input('Escreva o {} valor '.format(i)))
    if num % 2 ==0:
        soma+= num
        cont+= 1
print('Você informou {} números PARES e o resultado foi {}'.format(cont,soma))

