lista = []
x = 1
while x != 0:
    num = int(input('Digite um Valor: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Número repetido!')
    resp = str(input('Deseja continuar? [S/N] ')).upper()
    if resp == 'S':
        x=1
    if resp == 'N':
        x=0
lista.sort()
print(lista)