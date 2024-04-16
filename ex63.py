# Solicita ao usuário que insira um número
numero = int(input('Digite um número: '))

# Inicializa as variáveis
anterior = numero
soma = anterior + numero
resultado = anterior + soma
contador = 0

# Loop para imprimir os números enquanto resultado for menor ou igual a numero
# No entanto, parece que resultado nunca será menor ou igual a numero, então o loop nunca será executado
while resultado <= numero:
    print(resultado)
    resultado += 1
