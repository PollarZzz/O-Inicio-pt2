# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import time
from datetime import date

data_atual = date.today().year
contador_maioridade = 0
contador_menoridade = 0

for pessoa in range(1, 7 + 1):
    nasc = int(input(f'Em que ano nasceu a {pessoa}º nasceu: '))
    idade = data_atual - nasc
    if idade >= 18:
        contador_maioridade += 1
    else:
        contador_menoridade += 1
print(f'Das 7 pessoas apenas {contador_maioridade} são maior de idade')
print(f'Os outros {contador_menoridade} são de menor.')