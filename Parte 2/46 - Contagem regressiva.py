# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício
# Indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time
print(f'\033[1;32mINICIANDO CONTAGEM REGRESSIVA...\033[m')
time.sleep(1)
print('-=' * 10)

for contagem in range(10, -1, -1):
    time.sleep(0.5)
    print(contagem)
print('-=' * 10)
print('BOOOM 💥💥💥')
input("\n Pressione ENTER para encerrar o programa")