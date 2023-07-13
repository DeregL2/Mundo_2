#faça um programa que leia um número qualquer e mostre seu fatorial EX: 5 = 5X4X3X2X1 = 120

numero = int(input('Digite um número para ver seu fatorial: '))

resultado = 1
count = 1
while count <= numero:
    resultado *= count
    count += 1
print('Seu fatorial é {}'.format(resultado))

# Jeito do Professor!
n = int(input('Digite um valor: '))
c = n
f = 1
print('calculando {}! = '.format(n),end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' X 'if c >1 else ' = ',end='')
    f *=c
    c-=1
print(f)