#  Faça um programa que leia o peso de cinco pessoas. 
#  No final, mostre qual foi o maior e o menor peso lidos.

maior_peso = 0
menor_peso = float('inf')  # Inicializando com um valor muito grande

for peso_pessoas in range(1, 5 + 1):  # Faz a contagem até a 5º Pessoa
    peso = float(input(f"Digite o peso da {peso_pessoas}º Pessoa: "))
    if peso > maior_peso: # Caso o peso digitado for maior que o peso definido (0) atualiza o valor.
        maior_peso = peso
    if peso < menor_peso: # Caso o peso digitado for maior que o peso definido (0) atualiza esse valor 
        menor_peso = peso
# Lista os candidatos e os pesos deles.
print(f'Entre os 5 candidatos o maior peso foi de {maior_peso:.2f}Kg.')
print(f'Entre os 5 candidatos o menor peso foi de {menor_peso:.2f}Kg.')