# Faça um programa que leia o ano de nascimento de um jovem e informe
# De acordo com a sua idade, se ele ainda vai se alistar ao serviço militar
# Se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import time
import datetime

nome = str(input('Informe seu nome: '))
time.sleep(0.5)
nascimento = int(input('Digite o ano de nascimento: '))
atual = datetime.date.today().year
time.sleep(0.5)
idade = atual - nascimento

# Iniciando verificação se deve ou não se alistar!

if idade == 18:
    print(f'{nome} Você chegou na idade de se alistar ao serviços militar.')
elif idade >= 18:
    anos_pendente = idade - 18
    ano = atual - anos_pendente
    print(f'{nome} Você está atrasado! Você passou {anos_pendente} anos deve se apresentar no alistamento militar!')
    print(f'Seu alistamento foi em {ano}.')
elif idade <= 18:
    anos_pendente = 18 - idade
    ano = atual + anos_pendente
    print(f'{nome} Você ainda é muito novo, faltam {anos_pendente} para que chegue a idade pedida para o alistamento!')
    print(f'Seu alistamento será em {ano}.')
input("\n Pressione ENTER para sair")