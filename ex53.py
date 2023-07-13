#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo desconsiderando os espaços

frase = str(input('Digite uma frase: ')).strip().upper() #Escrevi ela, eliminei os espaços antes e depois e joguei tudo para maiuscula
palavras = frase.split()  #Split = transforma a frase em lista
junto = ''.join(palavras)  #Juntei tudo numa string só

'''inverso = junto[::-1] Esse jeito porem sem o FOR'''


inverso = ''
for letras in range(len(junto)-1,-1,-1):  #Inverti as letras, fui da ultima para a primeira, voltando uma letra
    inverso += junto[letras]
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto: # Se o 'Inverso' for IGUAL 'junto' Faça:
    print('Temos um palindromo!')
else:
    print('Essa palavra não é um palindromo!')