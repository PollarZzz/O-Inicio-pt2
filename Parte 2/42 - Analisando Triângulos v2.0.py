# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

import time

print('Desenvolvendo um analisador de triângulos...')
time.sleep(1.5)
r1 = float(input('Digite aqui o primeiro segmento: '))
r2 = float(input('Digite aqui o segundo segmento: '))
r3 = float(input('Digite aqui o terceiro segmento: '))
time.sleep(1.5)
if  r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3: # Se a soma dos segmentos forem iguais retorna um triangulo equilatero
        print(f'A soma dos segmentos forma um triângulo EQUILÁTERO!')
    elif r1 != r2 != r3 != r1: # Se a soma dos segmentos forem todas diferentes retorna um triangulo escaleno
        print(f'A soma dos segmentos forma um triângulo ESCALENO!')
    else: # Se a soma dos segmentos tiver 2 numeros iguais e 1 diferente formam um triangulos isosceles
        print(f'A soma dos segmentos forma um triângulo ISÓSCELES!')
else:
    print('Os segmentos NÃO PODEM formar um triângulo.')
input("\n Pressione ENTER para encerrar o programa")