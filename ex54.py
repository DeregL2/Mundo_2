#crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas sao de maior
# Importa a função date do módulo datetime
from datetime import date

# Obtém o ano atual
atual = date.today().year

# Inicializa as variáveis de contagem
totMaior = 0
totMenor = 0

# Loop for que itera sobre as sete pessoas
for i in range(1, 8):
    # Solicita ao usuário que insira o ano de nascimento da pessoa
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(i)))

    # Calcula a idade da pessoa
    idade = atual - ano

    # Verifica se a pessoa é maior de idade (21 anos ou mais)
    if idade >= 21:
        totMaior += 1
    else:
        totMenor += 1

# Exibe o total de pessoas maiores e menores de idade
print('Das sete pessoas, {} são maiores de idade.'.format(totMaior))
print('E {} ainda são menores de idade.'.format(totMenor))
