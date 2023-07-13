media = 0
soma = 0
maiorIdade = 0
nomeVelho: ''
totMulher20 = 0
for p in range(1,5):
    print('====== {} PESSOA ======'.format(p))
    nome = str(input('Nome: '))
    idade= int(input('Idade: '))
    sexo = str(input('sexo [M/F]: ')).strip().upper()
    soma += idade
    if p == 1 and sexo == 'M':
        maiorIdade = idade
        nomeVelho = nome
    if sexo in 'M' and idade > maiorIdade:
        maiorIdade = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade <= 20:
        totMulher20+=1
media = soma / 4
print('A média de idade do grupo é de {} '.format(media))
print('O nome do homem mais velho é {} e ele tem {} anos!'.format(nomeVelho,maiorIdade))
print('Neste grupo {} mulheres tem menos de 20 anos!'.format(totMulher20))