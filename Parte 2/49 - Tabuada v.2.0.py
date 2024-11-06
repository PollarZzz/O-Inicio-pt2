# Refaça o DESAFIO 9
# Mostrando a tabuada de um número que o usuário escolher
# Só que agora utilizando um laço for.

tabuada = int(input('Qual tabuada deseja visualizar: '))
limite = int(input('Até que valor deseja ver a tabuada: '))

for i in range(1, limite + 1):
    resultado = tabuada * i
    print(f"{tabuada} x {i} = {resultado}")
input("\n Pressione ENTER para encerrar o programa")