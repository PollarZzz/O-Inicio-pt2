# Faça um programa que leia um número qualquer e mostre o seu fatorial. 
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

import math
import time

print(f"\033[1;32mCALCULANDO FATORIAL USANDO MODULO MATH...\033[m")
time.sleep(1)
user_valor = int(input('Digite o valor a ser calculado: '))
print(math.factorial(user_valor))

################################################################################
