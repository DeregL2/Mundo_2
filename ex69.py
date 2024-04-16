#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

#A) quantas pessoas tem mais de 18 anos.

#B) quantos homens foram cadastrados.

#C) quantas mulheres tem menos de 20 anos.\

# Inicializando contadores para as estatísticas
contIdade = 0  # Contador para pessoas com mais de 18 anos
contHomen = 0  # Contador para homens cadastrados
contMulher = 0  # Contador para mulheres com menos de 20 anos

# Loop infinito para permitir o cadastro de várias pessoas
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)

    # Solicitação da idade e sexo da pessoa
    idade = int(input('Idade: '))
    sexo = str(input('[M/F] ')).upper()

    # Verificando as condições para atualizar os contadores
    if idade > 18:
        contIdade += 1
    if sexo == 'M':
        contHomen += 1
    elif sexo == 'F' and idade < 20:
        contMulher += 1

    # Perguntando ao usuário se deseja continuar o cadastro
    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break

# Exibindo as estatísticas finais
print(
    f'{contIdade} pessoas têm mais de 18 anos, {contHomen} homens foram cadastrados e {contMulher} mulher(es) tem menos de 20 anos.')
