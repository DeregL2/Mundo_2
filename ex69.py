#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

#A) quantas pessoas tem mais de 18 anos.

#B) quantos homens foram cadastrados.

#C) quantas mulheres tem menos de 20 anos.
contIdade = 0
contHomen = 0
contMulher = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = str(input('[M/F] ')).upper()
    if idade > 18:
        contIdade +=1
    if sexo == 'M':
        contHomen +=1
    elif sexo == 'F' and idade < 20:
        contMulher += 1
    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break

print(f'{contIdade} pessoas tem mais de 18 anos, apenas {contHomen} e homem e {contMulher} mulher(s) tem menos de 20 anos.')