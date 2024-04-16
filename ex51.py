# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.No final mostre os 10 primeiros termos dessa prograssão

# Solicita ao usuário o primeiro termo e a razão da PA
a = int(input('Primeiro termo: '))
r = int(input('Razão: '))

# Calcula o décimo termo da PA (que não é necessário para este problema)
# d = a + (10 - 1) * r

# Loop for que itera sobre os 10 primeiros termos da PA
for c in range(a, a + 10 * r, r):
    # Imprime o termo atual da PA
    print(c, end=' ')

# Imprime uma mensagem indicando o final dos termos
print('Finish')
