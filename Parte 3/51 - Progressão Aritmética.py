# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

import time

primeiro_termo = int(input("Primeiro Termo: "))
time.sleep(0.7)
razão = int(input("Razão: "))
time.sleep(0.7)
qnt_termos = int(input("Até quantos termos deseja mostrar: "))
time.sleep(0.7)
print('Calculando PA')

# Inicia o calculo da PA
result_termos = primeiro_termo + (qnt_termos - 1) * razão 
for contador in range(primeiro_termo, result_termos + razão, razão):
    print(f'{contador}', end=' » ') # Mostra o resultado da PA
print("Programa Encerrado!")