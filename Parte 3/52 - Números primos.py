# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

import time

print("Iniciando Programa de Verificação de Números Primos!")
time.sleep(1)
print("\033[31mLembre-se número primo só é dividido apenas por 1 e por ele mesmo\033[0m")
time.sleep(1)
numero = int(input("Digite o número para verificação: "))
numeros_contados = 0
for contador in range(1, numero + 1): # Inicia o contador do programar
    if numero % contador == 0: # Caso o contador seja divisivel pelo contador até o número ele
        print(f'\033[33m', end='') # Colocar uma cor indicando que é divisivel.
        numeros_contados += 1
    else:
        print(f'\033[31m', end='') # Aqui Caso não seja divisivel ele mostra em vermelho
print(f"\033[0mO número \033[33m{numero} \033[0mfoi divisivel \033[33m{numeros_contados} \033[0mvezes")
if numeros_contados == 2:
    print(f"E por isso ele \033[33mÉ PRIMO!")
else:
    print(f"\033[0mE por isso ele \033[31mNÃO É PRIMO!")