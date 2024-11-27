# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.

import time

# Entrada do primeiro termo e da razão
primeiro_termo = int(input("Primeiro Termo: "))
time.sleep(0.7)
razão = int(input("Razão: "))
time.sleep(0.7)

# Inicializando variáveis
termo = primeiro_termo
cont = 1
total_termos = 10
mais_termos = 10  # Começa com os primeiros 10 termos

print("Calculando PA...")
time.sleep(0.7)

# Loop para mostrar os termos da PA
while mais_termos != 0:
    while cont <= total_termos:
        print(f'{termo} > ', end='')
        termo += razão
        cont += 1
    print("Pausa")
    
    # Perguntar ao usuário se deseja mostrar mais termos
    mais_termos = int(input("Quantos termos a mais você quer mostrar? [0 para encerrar]: "))
    total_termos += mais_termos  # Adiciona os novos termos ao total

print(f"Progressão Aritmética encerrada.\n Termos visualializados: {total_termos}")
