# Faça um programa que calcule a SOMA entre todos os NÚMEROS IMPARES que são MULTIPLOS DE TRÊS  a que se encontram no intervalo de 1 até 500!

cont=0
soma = 0
for i in range(1,501, 2):
    if i % 3 ==0:
        soma = soma+i
        cont = cont +1
print('A soma é {} dos {} números'.format(soma,cont))


