# Inicializando uma lista vazia para armazenar os valores
lista = []

# Definindo uma variável para controlar o loop
x = 1

# Loop continua enquanto x for diferente de 0
while x != 0:
    # Solicitando ao usuário que digite um valor
    num = int(input('Digite um Valor: '))

    # Verificando se o número já está na lista
    if num not in lista:
        lista.append(num)  # Adicionando o número à lista se ele não estiver presente
    else:
        print('Número repetido!')  # Exibindo uma mensagem se o número já estiver na lista

    # Perguntando ao usuário se deseja continuar
    resp = str(input('Deseja continuar? [S/N] ')).upper()

    # Verificando a resposta do usuário
    if resp == 'S':
        x = 1  # Se 'S' (sim), x continua sendo 1 para continuar o loop
    elif resp == 'N':
        x = 0  # Se 'N' (não), x se torna 0 para sair do loop

# Ordenando a lista de valores únicos
lista.sort()

# Exibindo a lista ordenada
print(lista)
