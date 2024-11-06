# Desenvolva uma lógica que leia o peso e a altura de uma pessoa
# Calcule seu Índice de Massa Corporal (IMC) e mostre seu status
# De acordo com a tabela abaixo:

# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

import time

print('CALCULANDO ÍNDICE DE MASSA CORPORAL...')
time.sleep(0.5)
peso = float(input('Informe seu peso (KG): '))
time.sleep(0.5)
altura = float(input('Informe sua altura: '))
time.sleep(0.5)
imc = peso / (altura ** 2)

if imc <= 18.5:
    print(f'Seu IMC atualmente é de {imc:.2f}. Você está abaixo do peso! Contate um nutricionista.')
elif 18.5 <= imc <= 25:
    print(f'Seu IMC atualmente é de {imc:.2f}. Você está no peso ideial. Parabens!')
elif 25 <= imc <= 30:
    print(f'Seu IMC atualmente é de {imc:.2f}. Você está entrando no Sobrepeso. Cuide da sua saúde alimentar.')
elif 33 <= imc <= 40:
    print(f'Seu IMC atualmente é de {imc:.2f}. Você está Obeso! Contate um nutricionista e cuide da sua saúde alimenticia.')
elif imc >= 40:
    print(f'Seu IMC atualmente é de {imc:.2f}. Você está na Obesidade Mórbida cuide-se IMEDIATAMENTE!')
else:
    print('NENHUM VALOR ENCONTRADO! TENTE NOVAMENTE.')
input("\n Pressione ENTER para encerrar o programa")