# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
# De uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

import time

print(f"\033[1;32mSEQUENCIA DE FIBONACCI...\033[m")
time.sleep(1)
valor_user = int(input('Digite o valor que deseja visualizar a sequência: '))
if valor_user <= 0:
    print('Digite um valor inteiro diferente de 0.')
else:
    termo1, termo2 = 0, 1
    print("Sequência de Fibonacci:")
# Exibição dos termos da sequência
    for _ in range(valor_user):
        print(termo1, end=" > ")
        termo1, termo2 = termo2, termo1 + termo2
print(f'Fim do programa')