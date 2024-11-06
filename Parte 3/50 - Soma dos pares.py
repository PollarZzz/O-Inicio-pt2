# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.

import time

soma = 0
contador = 0

for i in range(1, 7):
    num_int = int(input(f'Digite o {i} valor: '))
    if num_int % 2 == 0:
        soma += num_int
        contador += 1
print(f'Você informou {contador} números PARES e a soma foi de {soma}')