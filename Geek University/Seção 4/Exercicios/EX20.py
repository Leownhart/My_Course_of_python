'''
20 - Leia um valor de massa em quilometros e apresente-o convertido em libras.
A fómula de conversão é: L = K / 0.45, Sendo K a massa em quilogramas e L a massa
em libras.
'''

k = int(input('Informe um valor em quilogramas: '))
l = k / 0.45
print('O valor informado convertido em libras é {:.2f}'.format(l))