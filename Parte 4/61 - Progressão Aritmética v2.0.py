# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA 
# Mostrando os 10 primeiros termos da progressão usando a estrutura while.

import time

primeiro_termo = int(input("Primeiro Termo: "))
time.sleep(0.7)
razão = int(input("Razão: "))
time.sleep(0.7)
print('Calculando PA')
print('Visualizando os 10 primeiros resultados...')
termo = primeiro_termo
cont = 1
while cont <= 10:
    print(f'{termo} > ', end='')
    termo += razão
    cont += 1
print(f'Encerrado.')