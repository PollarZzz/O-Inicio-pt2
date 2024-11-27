# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).


# Inicialização das variáveis
soma = 0
contador = 0

print("Digite números inteiros para somar. Digite 999 para encerrar.")

while True:
    numero = int(input("Digite um número: "))
    if numero == 999:  # Condição de parada
        break
    soma += numero
    contador += 1

# Exibição do resultado final
print(f"\nVocê digitou {contador} números.")
print(f"A soma dos números digitados é {soma}.")
