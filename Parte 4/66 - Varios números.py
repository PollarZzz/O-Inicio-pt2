# Crie um programa que leia números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre elas.

import time

contador = soma = 0

while True:
    number_user = int(input("Digite um valor: "))
    time.sleep(0.7)
    contador += 1
    if number_user == 999:
        break
    soma += number_user
print(f'Programa finalizado.\nFoi mostrado {contador} número e a soma deles é de: {soma}')