#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
cont = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('='*30)
    if n < 0:
        break
    for i in range(1,11):
        i *= n
        cont += 1
        print(f'{n} X {cont} = {i}')
    print('='*30)
print('Fim da execução')