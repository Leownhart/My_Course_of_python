'''
02 - Leia um número fornecido pelo usuário . Se esse número for positivo, calcule a raiz quadrada desse número,
Se o número for negativo mostre uma mesagem dizendo que o número é invalido.
'''

from math import sqrt
number = int(input('Informe um número: '))
if number > 0:
    raiz = sqrt(number)
    print(f'A raiz quadrada de {number} é {raiz}')
else:
    print('\033[0:31mNúmero inválido\033[m')