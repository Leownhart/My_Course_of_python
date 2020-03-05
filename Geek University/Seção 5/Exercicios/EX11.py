'''
11 - Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela
, a soma de todos os seus algarismo. Por exemplo, ao número 251 correspoderá o valor
8 (2 + 5 + 1). Se o número lido não for maior do que zero, o programa terminrá com a mesagem "Número Invalido".
'''

from time import sleep

intnumber = somar = 0
strnumber = str(input('Número: '))
for n in range(0, len(strnumber)):
    if strnumber[n].isnumeric():
        intnumber = int(strnumber[n])
        somar = somar + intnumber
if intnumber <= 0:
    print(' \033[0:31mNúmero invalido\033[m')
else:
    sleep(1.0)
    print(f'A soma dos algorismos é  {somar})')
    print('FIM....')