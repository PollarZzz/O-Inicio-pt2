# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

import time

print(f"\033[1;32mBRINCANDO COM NÚMEROS...\033[m")
time.sleep(0.7)
number1 = int(input(f'Digite o primeiro valor: '))
number2 = int(input(f'Digite o segundo valor: '))
time.sleep(0.7)
user_option = 0

while user_option != 5: # Se a opção for diferente de 5, mantem o loop das opções.
    print(f'INFORME A OPÇÃO DESEJADA')
    time.sleep(0.7)
    print(f'''   ---- MENU ----
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR QUE
    [4] NOVOS NÚMEROS
    [5] ENCERRAR PROGRAMA''')
    time.sleep(0.7)
    print(f'   ---- XXXX ----')
    user_option = int(input('Informe a opção desejada: '))
    time.sleep(0.7)
    if user_option == 1:
        result_soma = number1 + number2
        print('Calculando...')
        time.sleep(0.7)
        print(f'A soma do primeiro valor {number1} e o segundo valor {number2} é de: {result_soma}.')
        time.sleep(0.7)
    elif user_option == 2:
        print('Calculando...')
        time.sleep(0.7)
        result_multiplicacao = number1 * number2
        print(f'A multiplicação do primeiro valor {number1} e o segundo valor {number2} é de: {result_multiplicacao}.')
        time.sleep(0.7)
    elif user_option == 3:
        print('Verificando...')
        time.sleep(0.7)
        maior = max(number1, number2)
        print(f'O maior valor entre {number1} e {number2} é: {maior}.')
        time.sleep(0.7)
    elif user_option == 4:
        print(f'Descartando números antigos...')
        time.sleep(0.5)
        print(f'Pronto!')
        time.sleep(0.5)
        number1 = int(input(f'Digite o novo primeiro valor: '))
        time.sleep(0.3)
        number2 = int(input(f'Digite o novo segundo valor: '))
        time.sleep(0.7)
    elif user_option == 5:
        print("Encerrando o programa.")
        time.sleep(0.7)
    else:
        print("Opção inválida. Tente novamente.")