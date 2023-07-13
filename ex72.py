tupla = ('Zero','um','Dois','Três','Quatro',
         'Cinco','Seis','Sete','Oito','Nove',
         'Dez','Onze','Doze','Treze','Quatorze'
         ,'Quinze','Dezesseis','Dezessete','Dezoito',
         'Dezenove','Vinte')

numero = int(input('Digite um valor de 0 até 20: '))

while numero < 0 or numero > 20:
    numero = int(input('Digite novamente um valor : '))

print(f'Você digitou o número {tupla[numero]}')