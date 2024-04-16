#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
# Seu código
numero = 0
contador = 0
soma = 0

# Loop infinito até que o usuário digite 999
while True:
    numero = int(input('Digite um valor desejado: '))
    contador += 1
    soma += numero
    if numero == 999:
        # Subtrai 999 da soma e 1 do contador para excluir a flag
        soma2 = soma - 999
        contador2 = contador - 1
        break

print('Você digitou {} números e a soma de todos eles foi de {}'.format(contador2, soma2))

# Jeito Guanabara
num = soma = cont = 0

# Solicita ao usuário que digite um valor
num = int(input('Digite um valor desejado: '))  # flag

# Loop continua até que o usuário digite 999
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um valor desejado: '))  # Elimina a flag como última linha

print('Você digitou {} números e a soma de todos eles foi de {}'.format(cont, soma))
