#Criação de antecessor e sucessor!

# Solicita ao usuário para inserir dois números inteiros
n1 = int(input('Digite um número: '))
n2 = int(input('Digite o Segundo número: '))

# Inicializa uma variável de contagem para armazenar a diferença entre os números
cont = 0

# Verifica se o primeiro número é maior que o segundo
if n1 > n2:
    # Se sim, itera sobre todos os números entre n2 e n1 (excluindo n1)
    for i in range(n2, n1):
        # Incrementa o contador para cada número no intervalo
        cont += 1
else:
    # Se o segundo número for maior ou igual ao primeiro
    # itera sobre todos os números entre n1 e n2 (excluindo n2)
    for i in range(n1, n2):
        # Incrementa o contador para cada número no intervalo
        cont += 1

# Exibe o total de números no intervalo (excluindo o próprio número de entrada)
print(cont)


