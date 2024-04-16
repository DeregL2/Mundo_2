# Inicializa três listas vazias para armazenar valores digitados
lista1 = []
lista2 = []  # Lista para armazenar números pares
lista3 = []  # Lista para armazenar números ímpares

# Variável de controle para continuar ou não o loop
x = 0

# Loop para continuar solicitando valores até que o usuário decida parar
while x != 1:
    # Solicita ao usuário que digite um valor
    n = int(input('Digite um valor: '))

    # Adiciona o valor à lista1, independente se é par ou ímpar
    lista1.append(n)

    # Verifica se o valor é par ou ímpar e adiciona à lista correspondente
    if n % 2 == 0:
        lista2.append(n)
    else:
        lista3.append(n)

    # Pergunta ao usuário se deseja continuar inserindo valores
    stri = str(input('Deseja continuar? [S/N]: ')).upper()

    # Verifica se o usuário deseja continuar ou não
    if stri == 'S':
        x = 0
    elif stri == 'N':
        x = 1

# Exibe as três listas preenchidas com os valores digitados
print(f'Lista 1: {lista1}')
print(f'Lista 2 (números pares): {lista2}')
print(f'Lista 3 (números ímpares): {lista3}')

# Reinicializa as listas para que possamos preenchê-las de forma diferente
lista1 = []
lista2 = []
lista3 = []

# Reinicializa a variável de controle do loop
x = 0

# Loop para continuar solicitando valores até que o usuário decida parar
while x != 1:
    # Solicita ao usuário que digite um valor
    n = int(input('Digite um valor: '))

    # Adiciona o valor à lista1
    lista1.append(n)

    # Pergunta ao usuário se deseja continuar inserindo valores
    stri = str(input('Deseja continuar? [S/N]: ')).upper()

    # Verifica se o usuário deseja continuar ou não
    if stri == 'S':
        x = 0
    elif stri == 'N':
        x = 1

# Loop para preencher lista2 com números pares e lista3 com números ímpares
for i in range(1, len(lista1) + 1):
    if i % 2 == 0:
        lista2.append(i)
    else:
        lista3.append(i)

# Exibe as três listas preenchidas com os valores digitados
print(lista1)
print(lista2)
print(lista3)
