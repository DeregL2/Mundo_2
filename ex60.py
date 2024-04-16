#faça um programa que leia um número qualquer e mostre seu fatorial EX: 5 = 5X4X3X2X1 = 120

# Solicita ao usuário que insira um número para calcular seu fatorial
numero = int(input('Digite um número para ver seu fatorial: '))

# Inicializa o resultado como 1, pois 1 é o elemento neutro da multiplicação
resultado = 1

# Inicializa o contador como 1, para iterar de 1 até o número inserido pelo usuário
count = 1

# Loop while que calcula o fatorial do número inserido
while count <= numero:
    # Multiplica o resultado pelo valor atual do contador
    resultado *= count
    # Incrementa o contador
    count += 1

# Exibe o resultado, que é o fatorial do número inserido
print('Seu fatorial é {}'.format(resultado))

# Este é o código do "Jeito do Professor", que faz a mesma coisa, mas de forma ligeiramente diferente
# Solicita ao usuário que insira um valor
n = int(input('Digite um valor: '))

# Inicializa uma variável f como 1, pois 1 é o elemento neutro da multiplicação
f = 1

# Inicializa uma variável c como o valor inserido pelo usuário
c = n

# Exibe uma mensagem indicando que o cálculo do fatorial está sendo feito
print('Calculando {}! = '.format(n), end='')

# Loop while que calcula o fatorial
while c > 0:
    # Exibe o valor atual de c
    print('{}'.format(c), end='')
    # Exibe ' X ' se c for maior que 1, caso contrário, exibe ' = '
    print(' X ' if c > 1 else ' = ', end='')
    # Multiplica f pelo valor atual de c
    f *= c
    # Decrementa c
    c -= 1

# Exibe o resultado, que é o fatorial do número inserido
print(f)
