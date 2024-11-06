# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

import time

num1 = int(input('Escrava o primeiro valor inteiro: '))
time.sleep(1)
num2 = int(input('Escrava o segundo valor inteiro: '))
time.sleep(1)
print('Verificando números...')
time.sleep(1.5)
if num1 >= num2:
    print(f'O número {num1} é maior que o número {num2}.')
elif num2 >= num1:
    print(f'O número {num2} é maior que o número {num1}.')
else:
    print(f'Os valores são iguais!')
input("\n Pressione ENTER para sair")