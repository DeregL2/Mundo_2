#crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas sao de maior
from datetime import date
atual = date.today().year
totMaior = 0
totMenor = 0
for i in range(1,8):
    ano = int(input('Em que ano a {} pessoa nasceu? '.format(i)))
    idade = atual - ano
    if idade >= 21:
        totMaior += 1
    else:
        totMenor += 1
print('Os {} são de maior! '.format(totMaior))
print('E todos os {} ainda sao de menor! '.format(totMenor))