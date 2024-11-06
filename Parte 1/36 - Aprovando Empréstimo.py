# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

import time

valor_casa = float(input("Digite o valor da casa: R$ "))
time.sleep(1)
salario = float(input("Digite o seu salário: R$ "))
time.sleep(1)
anos = int(input("Em quantos anos você deseja pagar? "))
time.sleep(1)

# Calculando o valor da prestação mensal
prestacao = valor_casa / (anos * 12)

# Calculando 30% do salário
limite_prestacao = salario * 0.3

# Verificando se a prestação está dentro do limite
if prestacao <= limite_prestacao:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado. A prestação excede 30% do seu salário.")
input("\n Pressione ENTER para sair")