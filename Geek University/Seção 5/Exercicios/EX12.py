'''
12 - Ler um número inteiro. Se o número lido for negqativo, escreva a mesagem "Número inválido".
Se o número for positivo, calcular o logaritimo deste numero.
'''

import math

number = int(input('Número: '))
if number <= 0:
    print('Número Invalido')
else:
    print(f'{math.log(number):.11f}')  # Função do Logaritmo
