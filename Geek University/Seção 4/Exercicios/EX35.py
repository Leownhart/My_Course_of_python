'''
35 - Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = raiz = a² + b² faça um programa que receba os valores de a e b e calcule
o valor da hipotenusa através da equação. Imprima o resultado dessa operação.
'''

from math import sqrt
a = float(input('Informe o cateto A: '))
b = float(input('Informe o cateto B: '))
hip = sqrt(pow(a, 2) + pow(b, 2))
print(f'O Cálculo da hipotenusa é {hip:.2f}')
