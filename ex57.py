#Faça um programa que leia o SEXO de uma pessoa, mas só aceite 'm' ou 'f' caso esteja errado peça para digitar novamente!

sexo =str(input('Digite seu sexo [M/F]: ')).upper()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite novamente seu sexo [M/F]: ')).upper()
print('Fim')