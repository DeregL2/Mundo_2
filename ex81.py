# Inicializando uma lista vazia para armazenar os valores
lista = []

# Inicializando a variável de controle para o loop
x = 0

# Inicializando o contador para contar o número de valores digitados
count = 0

# Loop enquanto x for diferente de 1
while x != 1:
    # Solicitando ao usuário que digite um valor e adicionando à lista
    n = int(input('Digite Um valor: '))
    lista.append(n)

    # Perguntando ao usuário se deseja continuar
    resp = str(input('Deseja continuar? [S/N]: ')).upper()
    count += 1  # Incrementando o contador de valores digitados

    # Verificando a resposta do usuário
    if resp == 'S':
        x = 0  # Se 'S', continua no loop
    elif resp == 'N':
        x = 1  # Se 'N', sai do loop

# Ordenando a lista em ordem decrescente
lista.sort(reverse=True)

# Exibindo o número total de valores digitados e a lista ordenada
print(f'Foram digitados {count} números!')
print(lista)

# Verificando se o valor 5 está na lista e exibindo uma mensagem correspondente
if 5 in lista:
    print('O valor 5 está na lista')
