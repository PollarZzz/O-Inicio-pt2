# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário 
# 2 para octal
# 3 para hexadecimal.

import time

num = int(input('Escreva um número inteiro: '))
print('Como deseja converter?\n 1 > BINÁRIO\n 2 > OCTAL\n 3 > HEXADECIMAL')
opção = int(input('Escolha uma opção: '))

if opção == 1:
    print(f'{num} convertido em BINÁRIO é {bin(num)}')
elif opção == 2:
    print(f'{num} convertido em OCTAL é {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} convertido em HEXADECIMA é {hex(num)[2:]}')
else:
    print(f'Opção Invalida ou Inexistente!')
input("\n Pressione ENTER para sair")