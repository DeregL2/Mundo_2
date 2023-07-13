cont = 0
num = 0
soma = 0
totMenor = 0
totMaior = 0
while True:
    num= int(input('Digite um valor desejado: '))
    cont +=1
    soma+=num
    if cont == 1:
        totMaior = num
        totMenor = num
    else:
        if num > totMaior:
            totMaior = num
        if num < totMenor:
            totMenor = num
    s = str(input('Deseja continua? [S/N]: ')).upper()
    if s == 'S':
        print('Ok')
    elif s == 'N':
        break

media = soma /cont

print('A media entre todos os valores foi de {}, O maior número inserido foi {} e o menor número inserido foi {}'.format(media,totMaior,totMenor))