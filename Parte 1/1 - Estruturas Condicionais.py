import time

print(f'\033[1;32mINICIANDO ESTRUTURA CONDICIONAL SIMPLES...\033[m')
time.sleep(1)

nome = str(input("Digite seu nome: "))
if nome == "Gabriel":
    print(f'Que belo nome {nome}, prazer em conhecê-lo!')
else:
    print(f'Que nome interessante {nome}, prazer em conhecê-lo!')
input("\n Pressione ENTER para sair")

print(f'\033[1;35mINICIANDO ESTRUTURA CONDICIONAL COMPOSTA...\033[m')
time.sleep(1)

nome = str(input("Digite seu nome: "))
if nome == "Gabriel" or nome == "Matheus" or nome == "Kaua" or nome ==  "Henrique":
    print(f'Que nome mais comum {nome} 😂')
else:
    print(f'Que nome interessante {nome}')

print(f'\033[1;33mINICIANDO ESTRUTURA CONDICIONAL ANINHADA...\033[m')
time.sleep(1)

nome = str(input("Digite seu nome: "))
if nome in "Gabriel Matheus Kaua Henrique":
    print(f'Que belo nome masculino {nome}')
else:
    print(f'Que nome interessante {nome}')
input("\n Pressione ENTER para sair")

