# Inicializando três listas vazias para armazenar os valores
lista1 = []
lista2 = []  # Lista para armazenar números pares
lista3 = []  # Lista para armazenar números ímpares

# Loop para solicitar ao usuário que insira valores repetidamente até que decida parar
x = 0
while x != 1:
    n = int(input('Digite um valor! '))
    lista1.append(n)  # Adicionando o valor à lista1

    # Verificando se o número é par ou ímpar e adicionando-o às listas correspondentes
    if n % 2 == 0:
        lista2.append(n)  # Se for par, adiciona à lista2
    elif n % 2 == 1:
        lista3.append(n)  # Se for ímpar, adiciona à lista3

    # Perguntando ao usuário se deseja continuar
    stri = str(input('Deseja continuar? [S/N]')).upper()
    if stri == 'N':
        x = 1  # Se 'N', sai do loop

# Exibindo as três listas
print(f'Lista 1: {lista1}')
print(f'Lista 2 (números pares): {lista2}')
print(f'Lista 3 (números ímpares): {lista3}')


# Reinicializando as três listas vazias
lista1 = []
lista2 = []  # Lista para armazenar números pares
lista3 = []  # Lista para armazenar números ímpares

# Loop para solicitar ao usuário que insira valores repetidamente até que decida parar
x = 0
while x != 1:
    n = int(input('Digite um valor! '))
    lista1.append(n)  # Adicionando o valor à lista1

    # Perguntando ao usuário se deseja continuar
    stri = str(input('Deseja continuar? [S/N]')).upper()
    if stri == 'N':
        x = 1  # Se 'N', sai do loop

# Populando lista2 com números pares e lista3 com números ímpares
for i in lista1:
    if i % 2 == 0:
        lista2.append(i)  # Adiciona à lista2 se for par
    else:
        lista3.append(i)  # Adiciona à lista3 se for ímpar

# Exibindo as três listas
print(f'Lista 1: {lista1}')
print(f'Lista 2 (números pares): {lista2}')
print(f'Lista 3 (números ímpares): {lista3}')
