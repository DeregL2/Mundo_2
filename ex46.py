# Importa a função sleep do módulo time
from time import sleep

# Loop for que conta de 10 até 0 em ordem decrescente
for i in range(10, -1, -1):
    # Pausa a execução do programa por 1 segundo
    sleep(1)
    # Imprime o número atual
    print(i)

# Imprime uma mensagem ao final do loop
print('BUUM! BUUM! POOW!')
