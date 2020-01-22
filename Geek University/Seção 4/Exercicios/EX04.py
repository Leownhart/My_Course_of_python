'''
4 - Leia um número real e imprima o resultado do quadrado desse número.
'''

# RESPOSTA

from math import pow
number = float(input('Informe um valor: '))
quad = pow(number, 2)
print('O quadrado do valor informado é {:.0f}'.format(quad))
