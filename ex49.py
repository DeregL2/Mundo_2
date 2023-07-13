# refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher , só que agora utilizando um laço for!

num = int(input('Escreva um número para ver sua tabuada: '))
s = 0
for i in range(1,11):
    i = num*i
    s= s +1
    print('{} X {:2} = {}'.format(num,s,i))

#Forma do professor
for i in range(1,11):
    print('{} X {} = {}'.format(num,i,num*i))