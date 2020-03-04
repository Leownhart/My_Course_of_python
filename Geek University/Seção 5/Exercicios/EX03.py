'''
03 - Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrario,
imprima o número quandrado.
'''

from math import sqrt, pow

number = float(input('Informe um número real: '))
if number > 0:
    raiz = sqrt(number)
    print(f'A raiz quadrada de {number} é {raiz}')
else:
    print(f'{pow(number, 2)}')
