# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
# Script Aprimorado by PollarZzz

# Programa para ler o sexo da pessoa, aceitando apenas 'M' ou 'F'
while True:
    sexo = input("Digite o sexo da pessoa ('M' para masculino ou 'F' para feminino): ").upper()
    
    # Verifica se o valor inserido é 'M' ou 'F'
    if sexo == 'M' or sexo == 'F':
        print(f"Sexo registrado com sucesso: {sexo}")
        break  # Interrompe o loop se o valor estiver correto
    else:
        print("Valor inválido! Digite novamente.")
