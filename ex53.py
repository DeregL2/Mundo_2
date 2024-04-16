#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo desconsiderando os espaços

# Solicita ao usuário que insira uma frase
frase = str(input('Digite uma frase: ')).strip().upper()  # Remove espaços extras, converte para maiúsculas

# Divide a frase em palavras
palavras = frase.split()

# Junta as palavras em uma única string, sem espaços
junto = ''.join(palavras)

# Inverte a string
inverso = ''
for letras in range(len(junto) - 1, -1, -1):
    inverso += junto[letras]

# Exibe a frase original e sua versão invertida
print('O inverso de {} é {}'.format(junto, inverso))

# Verifica se a frase original é igual à sua versão invertida
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Esta frase não é um palíndromo!')
