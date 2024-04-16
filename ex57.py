#Faça um programa que leia o SEXO de uma pessoa, mas só aceite 'm' ou 'f' caso esteja errado peça para digitar novamente!

# Solicita ao usuário que digite o sexo e converte para maiúsculas
sexo = str(input('Digite seu sexo [M/F]: ')).upper()

# Loop while que continua pedindo o sexo até que seja 'M' ou 'F'
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite novamente seu sexo [M/F]: ')).upper()

# Exibe "Fim" quando o sexo digitado for válido
print('Fim')
