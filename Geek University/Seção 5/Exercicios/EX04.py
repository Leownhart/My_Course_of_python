'''
04 - Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:

* O número digitado ao quadrado
* A raiz quadrada do número digitado
'''

from  math import sqrt, pow

number = int(input('Número: '))
if number > 0:
    quad = pow(number, 2)
    raiz = sqrt(number)
    print(f'O quadrado do número {number} é {quad}')
    print(f'A raiz quadrada do número {number} é {raiz:.2f}')
else:
    print('\033[0:31mNúmero Invalido!\033[m')
