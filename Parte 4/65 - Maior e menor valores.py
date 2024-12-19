# Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

respst = 'S'
soma = quant = média = maior = menor = 0
while respst in 'Ss':
    number = int(input('Digite um número: '))
    soma += number
    quant += 1
    if quant == 1:
        maior = menor = number
    else:
        if number > maior:
            maior = number
        if number < maior:
            menor = number
    respst = str(input('Deseja Continuar [S/N]: ')).upper().strip()[0]
média = soma / quant
print(f'Você digitou {quant} valores e a média entre ele foi de {média}')
print(f'O maior valor foi de {maior} e o menor valor foi de {menor}')