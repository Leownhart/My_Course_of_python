'''
30 - Leia um valor em real e a cotação do dólar. Em seguida, Imprima o valor correspondente em dólares.
'''

print('-='*9)
print('CONVERSOR DE MOEDA')
print('-='*9)

cot = float(input('Informe a cotação do dolar atual: $ '))
real = float(input('Informe um valor em (Real): R$ '))
dol = real / cot
print(f'A valor informado convertido em dolar é {dol:.2f}$ ')
