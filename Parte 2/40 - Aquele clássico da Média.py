# Crie um programa que leia duas notas de um aluno e calcule sua média
# mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

import time

primeiro_semestre = float(input('Qual a nota do aluno no primeiro semetre: '))
time.sleep(0.5)
segundo_semestre = float(input('Qual a nota do aluno no segundo semetre: '))
time.sleep(0.5)

nota_final = (primeiro_semestre + segundo_semestre) / 2

print('CALCULANDO NOTA FINAL...')
time.sleep(0.5)

if nota_final < 5:
    print('VOCÊ FOI REPROVADO!')
elif nota_final <= 5 or nota_final <=6.9:
    print('VOCÊ FOI PARA A RECUPERAÇÃO!')
elif nota_final >= 7:
    print('PARABENS VOCÊ FOI APROVADO!')
else:
    print('NENHUM PARÂMETRO ENCONTRADO. TENTE NOVAMENTE!')