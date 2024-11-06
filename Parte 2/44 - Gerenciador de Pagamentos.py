# Elabore um programa que calcule o valor a ser pago por um produto
# Considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal 
# 3x ou mais no cartão: 20% de juros

import time

print('\033[1;32mINCIANDO GERENCIADOR DE PAGAMENTOS...\033[m')
time.sleep(1)
valor_produto = float(input('\033[1;33mINSIRA O VALOR DO PRODUTO: R$\033[m'))
time.sleep(1)
print('\033[1;36mINFORME COMO DESEJA FAZER O PAGAMENTO:\033[m')
time.sleep(0.5)
print('1) A vista dinheiro/cheque: 10% de desconto.')
time.sleep(0.5)
print('2) A vista no cartão: 5% de desconto.')
time.sleep(0.5)
print('3) Em até 2x no cartão: Preço formal.')
time.sleep(0.5)
print('4) Em 3x ou mais no cartão: 20% de juros.')
time.sleep(0.5)
opçao_selecionada = int(input('\033[1;31mSua opção: \033[m'))

if opçao_selecionada == 1:
    dinheiro_cheque = valor_produto - (valor_produto * 10 / 100)
    time.sleep(0.5)
    print(f'O valor a vista com dinheiro/cheque de R${valor_produto:.2f}\nPor R${dinheiro_cheque:.2f}.')
elif opçao_selecionada == 2:
    cartao_a_vista = valor_produto - (valor_produto * 5 / 100)
    time.sleep(0.5)
    print(f'O valor a vista com pagamento em cartão de R${valor_produto:.2f}\nPor R${cartao_a_vista:.2f}.')
elif opçao_selecionada == 3:
    parcelamento_2x = valor_produto / 2 
    time.sleep(0.5)
    print(f'O valor do produto: R${valor_produto:.2f}\nFoi parcelado em 2x de R${parcelamento_2x:.2f}')
elif opçao_selecionada == 4:
    parcela_meses = int(input('Em quantos meses deseja parcelar: ')) # Quantos meses o usuário vai parcelar
    time.sleep(0.5)
    print('Aplicando Juros de 20%...')
    time.sleep(1)
    # Cálculo correto dos juros e do valor total
    valor_a_pagar = valor_produto + (valor_produto * 20 / 100) # O valor total a ser pago é a soma do produto + 20%
    total = valor_a_pagar / parcela_meses # Meses com juros aplicado
    print(f'Sua compra foi parcelada em {parcela_meses} meses de R${total:.2f} com juros aplicado!')
    time.sleep(0.3)
    print(f'O valor de R${valor_produto:.2f} foi para {valor_a_pagar:.2f}')
