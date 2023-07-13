#faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Escreva um número: '))
x=0

for i in range(2,n):
   if n % i ==0:
        x += 1

if x == 0:
    print('É primo')
else:
    print('Não é primo')
print('\n Jeito do Professor!')

'''Jeito do professor!'''

num = int(input('Escreva um número: '))
contador = 0

#Range de 1 até o número inserido
for c in range(1,num+1):
    if num % c ==0:                    # Se número foi dividido (mod) pelo C e o resultado for zero, Faça:
        print('\033[33m', end=' ')     #Verificação dos números e mudando suas cores
        contador +=1                   #Contando quantas vezes o número foi dividido
    else:
        print('\033[31m',end=' ')
    print('{} '.format(c),end=' ')

# se o contador for IGUAL a 2 entao faça:
if contador == 2:
    print('\n\033[mO número {} foi dividido {} vezes, por isso ele é PRIMO '.format(num,contador))
else:
    print('\n\033[mO número {} foi divido {} vezes, por isso ele NÃO É PRIMO'.format(num,contador))