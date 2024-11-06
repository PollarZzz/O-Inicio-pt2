# A Confederação Nacional de Natação precisa de um programa que leia
# O ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

import time
import datetime

print('INCIANDO PROGRAMA DE VERIFICAÇÃO DE ATLETA...')
time.sleep(0.5)

time.sleep(0.5)
nascimento = int(input('Digite o ano de nascimento: '))
atual = datetime.date.today().year
time.sleep(0.5)
idade = atual - nascimento

if idade <= 9:
    print('Você está na categoria MIRIM!')
elif idade <= 14:
    print('Você está na categoria JOVEM!')
elif idade <= 19:
    print('Você está na categoria JÚNIOR!')
elif idade <= 24:
    print('Você está na categoria SÊNIOR!')
elif idade >= 25:
    print('Você está na categoria MASTER!')
else:
    print('ERRO! TENTE NOVAMENTE...')