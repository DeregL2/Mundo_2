media = 0
soma = 0
maiorIdade = 0
nomeVelho = ''  # Corrigido: adicionei o sinal de atribuição
totMulher20 = 0

for p in range(1, 5):
    print('====== {} PESSOA ======'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma += idade

    # Verifica se a pessoa é o homem mais velho
    if p == 1 and sexo == 'M':
        maiorIdade = idade
        nomeVelho = nome
    if sexo == 'M' and idade > maiorIdade:
        maiorIdade = idade
        nomeVelho = nome

    # Conta o número de mulheres com menos de 20 anos
    if sexo == 'F' and idade <= 20:
        totMulher20 += 1

media = soma / 4

print('A média de idade do grupo é de {:.1f} anos'.format(media))
print('O nome do homem mais velho é {} e ele tem {} anos'.format(nomeVelho, maiorIdade))
print('Neste grupo, {} mulheres têm menos de 20 anos'.format(totMulher20))
