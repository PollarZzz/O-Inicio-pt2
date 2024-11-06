# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

import time

print(f'\033[1;32mINICIANDO CONTADOR DE NÚMEROS PARES...\033[m')
time.sleep(1)
print('-=' * 10)

valor1 = int(input('\033[1;33mDeseja começar em que número: \033[m'))
valor2 = int(input('\033[1;33mDeseja finalizar em que número: \033[m'))

for contagem in range(valor1, valor2 + 1, 2):
    time.sleep(0.3)
    print(contagem)
print('-=' * 10)
input("\n Pressione ENTER para encerrar o programa")