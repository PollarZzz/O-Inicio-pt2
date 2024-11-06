# Faça um programa que calcule a soma entre todos os números
# Que são múltiplos de três e que se encontram no intervalo de 1 até 500.

import time
print(f'\033[1;32mINICIANDO CALCULO E SOMA ENTRE NÚMEROS MÚTIPLOS DE 3...\033[m')
time.sleep(1)
print('-=' * 10)

soma = 0 # Inicia a soma com valores zerado
contador = 0 # Inicia o programa com o contador zerado

for soma_total in range(1, 501, 2): # Inicia a contagem no "1" e finaliza no "501" pulando de 2 em 2.
    if soma_total % 3 == 0: # Pega os valores da contagem e verifica quais são mútiplos de 3 que finalizam a conta.
        soma = soma + soma_total # Cada vez que ele ver um mútiplo de 3 ele soma + o próximo mútiplo de 3
        contador = contador + 1 # Cada vez que ele achar um mútiplo de 3 ele adiciona 1 na contagem.
print(f'A soma de todos os {contador} valores solicitados é igual a: {soma}.')
input("\n Pressione ENTER para encerrar o programa")