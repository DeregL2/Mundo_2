# Inicializando uma lista vazia para armazenar os valores
lista = []

# Loop for para solicitar ao usuário que insira cinco valores
for i in range(1, 6):
    # Solicitando ao usuário que digite um valor
    num = int(input(f'Digite o {i} Valor: '))

    # Verificando se é o primeiro valor inserido ou se o valor é maior do que o último valor na lista
    if i == 1 or num > lista[-1]:
        lista.append(num)  # Adicionando o valor ao final da lista se for o primeiro ou maior que o último
    else:
        pos = 0
        # Loop while para encontrar a posição correta do novo valor na lista
        while pos < len(lista):
            # Verificando se o valor é menor ou igual ao valor atual na posição pos
            if num <= lista[pos]:
                lista.insert(pos, num)  # Inserindo o valor na posição pos
                break  # Saindo do loop while após a inserção do valor
            pos += 1  # Incrementando a posição se o valor não for menor ou igual ao valor atual

# Exibindo a lista ordenada
print(lista)
