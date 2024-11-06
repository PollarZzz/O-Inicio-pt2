# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo
# Desconsiderando os espaços. Exemplos de palíndromos:
# APÓS A SOPA 
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA


import time

print("Iniciando Programa de Verificação de Palídromos!")
time.sleep(1)
print("\033[31mLembre-se Palídromos são palavras que podem ser lidas de frente para tras.\033[0m")
time.sleep(1)

palavra = str(input("Digite a Palavra a Verificar: "))
palavra_sem_espacos = palavra.replace(" ", "").lower() # Faz a leitura da palavra e converte em letras minusculas
palavra_invertida = ''.join(reversed(palavra_sem_espacos)) # Faz a leitura da palavra e inverte ela
# Verificar se é um palíndromo e imprimir o resultado
if palavra_sem_espacos == palavra_invertida: # Checa se a palavras são iguais
  print("A frase é um palíndromo!")
else:
  print("A frase não é um palíndromo.")