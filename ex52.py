#faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# Solicita ao usuário que insira um número inteiro
n = int(input('Escreva um número: '))

# Variável de controle para contar o número de divisores
x = 0

# Loop for que itera de 2 até (n - 1)
for i in range(2, n):
    # Verifica se o número é divisível por i
    if n % i == 0:
        # Se for divisível, incrementa o contador
        x += 1

# Se o contador for igual a zero, significa que o número é primo
if x == 0:
    print('É primo')
else:
    print('Não é primo')

# Agora segue a implementação do "jeito do professor"


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