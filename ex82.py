lista1 = []
lista2 = []
lista3 = []

x = 0
while x != 1:
    n = int(input('Digite um valor! '))
    lista1.append(n)
    if n % 2 == 0:
        lista2.append(n)
    elif n % 2 == 1:
        lista3.append(n)
    stri = str(input('Deseja continuar? [S/N]')).upper()
    if stri == 'S':
        x=0
    elif stri =='N':
        x = 1
print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')
print(f'Lista 3: {lista3}')

lista1 = []
lista2 = []
lista3 = []
x = 0
while x != 1:
    n = int(input('Digite um valor! '))
    lista1.append(n)
    stri = str(input('Deseja continuar? [S/N]')).upper()
    if stri == 'S':
        x = 0
    elif stri == 'N':
        x = 1

for i in range(1,len(lista1)+1):
    if i % 2 == 0:
        lista2.append(i)
for k in range(1,len(lista1)+1):
    if k % 2 == 1:
        lista3.append(k)


print(lista1)
print(lista2)
print(lista3)