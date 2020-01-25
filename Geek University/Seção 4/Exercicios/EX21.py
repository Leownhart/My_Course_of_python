'''
21 - Leia um valor de massa em  libras e apresente-o convertido em quilogramas. A fórmula
de conversão é: K= L * 0.45, sendo K a masssa em quilogramas e L a massa em libras.
'''

libras = int(input('Informe um valor de massa em libras: '))
k = libras * 0.45
print('O valor da massa em libras convertido para quilogramas é {:.0f}'.format(k))


