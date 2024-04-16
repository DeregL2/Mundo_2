# Solicita ao usuário a largura e a altura da parede
largura = float(input('Escreva a Largura de uma parede: '))
altura = float(input('Escreva a altura de uma parede: '))

# Calcula a área da parede multiplicando largura pela altura
area = altura * largura

# Calcula a quantidade de tinta necessária para pintar a parede (assumindo 2 metros quadrados de parede por litro de tinta)
tinta = area / 2

# Exibe a quantidade de tinta necessária
print(tinta)

# Solicita ao usuário um valor e calcula um desconto de 10%
valor = int(input('Escreva a Largura de uma parede: '))
r = valor * (10 / 100)
s = valor - r

# Exibe o valor com o desconto aplicado
print(s)
