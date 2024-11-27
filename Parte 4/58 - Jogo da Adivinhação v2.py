# Melhore o jogo do DESAFIO 28
# Onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

import time
import random

# Geração de um número aleatório entre 1 e 7
print(f"\033[1;32mINICIANDO O ADIVINHA...\033[m")
time.sleep(1)
print("Olá👋 jogador!! Bem-vindo ao programa. A regra do jogo é simples:")
print("1. Meu sistema está pensando em um número inteiro entre 1 e 7. Basta adivinhar e boom💥, você ganha!!")
print("2. Se você errar, o sistema irá te dizer que você perdeu.")
print("Fique atento!! O jogo está começando!!")
time.sleep(2.5)

contador_error = 0
numero = random.randint(1, 7)

while True: # Verifica se o loop é verdadeiro
    user_resp = int(input('Em que número estou pensando?\nR: '))
    print("Aguarde... Estou pensando em um número 🤔")
    time.sleep(1)    
    if user_resp != numero: # Verifica se a resposta do usuario é igual o numero pensado pelo programa
        print('⚠ Infelizmente você errou.')
        contador_error += 1
    else:
        print('🔥 Parabéns, você acertou.')
        break  # Sai do loop quando o jogador acerta
print(f'Parabéns! Após {contador_error} tentativa(s), você obteve seu acerto!')
