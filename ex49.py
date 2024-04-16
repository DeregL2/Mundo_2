# refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher , só que agora utilizando um laço for!

# Solicita ao usuário para inserir um número
num = int(input('Escreva um número para ver sua tabuada: '))

# Loop for que itera de 1 a 10 para gerar a tabuada
for i in range(1, 11):
    # Multiplica o número escolhido pelo usuário pelo número do loop (de 1 a 10)
    resultado = num * i
    # Imprime o resultado da multiplicação formatado na tabuada
    print('{} X {:2} = {}'.format(num, i, resultado))

# Essa é a forma mais direta, sem criar variáveis adicionais
# para o loop
# Apenas imprime a tabuada diretamente no loop
for i in range(1, 11):
    print('{} X {} = {}'.format(num, i, num * i))
