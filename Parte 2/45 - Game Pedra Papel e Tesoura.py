# Crie um programa que faça o computador jogar Jokenpô com você.

import time
import random

escolhas = ['Pedra', 'Papel', 'Tesoura']
jogador_escolha = str(input('Faça sua jogada [Pedra, Papel ou Tesoura]: ').capitalize())
time.sleep(0.5)
print('Computador fazendo jogada...')
time.sleep(1)
computador_escolha = random.choice(escolhas)

print(f"Você escolheu: {jogador_escolha}")
time.sleep(0.5)
print(f"O computador escolheu: {computador_escolha}")
time.sleep(0.5)

if jogador_escolha == computador_escolha:
    print("Empate!")
    # Verifica se as escolhas do jogador e da maquina
elif (jogador_escolha == 'Pedra' and computador_escolha == 'Tesoura') or \
     (jogador_escolha == 'Papel' and computador_escolha == 'Pedra') or \
     (jogador_escolha == 'Tesoura' and computador_escolha == 'Papel'):
    # Caso a escolha do jogador for vitoriosa, retorna o win dele.
    print("Você venceu!") 
else:
    time.sleep(0.5)
    print("O computador venceu!") # Se não a máquina ganha.
