lista= []
x = 0
count = 0
while x != 1:
    n = int(input('Digite Um valor: '))
    lista.append(n)
    resp = str(input('Deseja continuar? [S/N]: ')).upper()
    count += 1
    if resp == 'S':
        x = 0
    elif resp == 'N':
        x = 1
lista.sort(reverse=True)
print(f'Foram digitados {count} números!')
print(f'{lista}')
if 5 in lista:
    print('o Valor 5 está na lista')
