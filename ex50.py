#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daquela que forem pares. Se o valor digitado for ímpar . Desconsidere-o.

# Inicializa as variáveis de soma e contagem
soma = 0
cont = 0

# Loop for que itera seis vezes para ler os seis números
for i in range(1, 7):
    # Solicita ao usuário que insira um número
    num = int(input('Escreva o {} valor: '.format(i)))
    # Verifica se o número é par
    if num % 2 == 0:
        # Se for par, adiciona-o à soma
        soma += num
        # Incrementa o contador de números pares
        cont += 1

# Exibe a quantidade de números pares informados e a soma deles
print('Você informou {} números PARES e o resultado foi {}'.format(cont, soma))
