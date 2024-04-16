# Criando uma lista vazia para armazenar os valores digitados
lista = []

# Iterando sobre os números de 1 a 5
for i in range(1, 6):
    # Solicitando ao usuário que insira um valor e armazenando na variável 'num'
    num = int(input(f'Digite o {i} valor: '))
    # Adicionando o valor à lista
    lista.append(num)

# Exibindo os valores digitados pelo usuário
print(f'Você digitou os valores {lista} ')

# Exibindo o maior e o menor valor da lista usando as funções max() e min()
print(f'O maior número digitado foi {max(lista)} e o menor foi {min(lista)}')

# Exibindo as posições do maior e do menor valor na lista usando o método index()
print(f'A posição do maior número é {lista.index(max(lista))} e do menor é {lista.index(min(lista))}')

