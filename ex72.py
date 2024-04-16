# Definindo uma tupla com os números de 0 a 20 por extenso
tupla = ('Zero','Um','Dois','Três','Quatro',
         'Cinco','Seis','Sete','Oito','Nove',
         'Dez','Onze','Doze','Treze','Quatorze',
         'Quinze','Dezesseis','Dezessete','Dezoito',
         'Dezenove','Vinte')

# Solicitando ao usuário que insira um número de 0 a 20
numero = int(input('Digite um valor de 0 até 20: '))

# Enquanto o número estiver fora do intervalo de 0 a 20, solicita que o usuário insira novamente
while numero < 0 or numero > 20:
    numero = int(input('Digite novamente um valor : '))

# Exibindo por extenso o número digitado pelo usuário usando a tupla
print(f'Você digitou o número {tupla[numero]}')
