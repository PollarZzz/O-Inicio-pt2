# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho 
# E quantas mulheres têm menos de 20 anos.

somar_idade = 0
media_idade = 0
maioridade_homem = 0
nome_velho = ''
total_mulher = 0

for pessoa in range(1, 4 + 1):
    print(f'----- {pessoa}º Pessoa -----')
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [F/M]: "))
    print(f'----- XXX -----')
    somar_idade += idade
    
    if pessoa == 1 and sexo in "Mm":
        maioridade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maioridade_homem:
        maioridade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher += 1
media_idade = somar_idade / 4

print(f'A media de idade do grupo é de {media_idade}.')
print(f'O nome do Homem mais velho é {nome_velho.capitalize()} e ele tem {maioridade_homem} anos.')
print(f'Ao todo temos {total_mulher} tem menos de 20 anos.')
