lista = []
for i in range(1,6):
    num=(int(input(f'Digite o {i} valor: ')))
    lista.append(num)
print(f'Você digitou os valores {lista} ')
print(f'O maior número digitado foi {max(lista)} e o menor foi {min(lista)}')
print(f'A posição do maior número é {lista.index(max(lista))} e do menor é {lista.index(min(lista))}')
