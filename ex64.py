numero = 0
contador = 0
soma = 0
while True:
    numero = int(input('Digite um valor desejado: '))
    contador +=1
    soma +=numero
    if numero == 999:
        break
print('Você digitou {} números e a soma de todos eles foi de {}'.format(contador,soma))