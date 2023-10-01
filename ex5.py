#Criação de antecessor e sucessor!

n1 = int(input('Digite um número: '))
n2 = int(input('Digite o Segundo número: '))

cont = 0
if n1 > n2:
    for i in range(n2,n1):
        cont+=1
else:
    for i in range(n1,n2):
        cont+=1
print(cont)


