# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.No final mostre os 10 primeiros termos dessa prograssão

a = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = a + (11-1)*r

for c in range(a,d,r):
    print(c, end=' ')
print('Finish')