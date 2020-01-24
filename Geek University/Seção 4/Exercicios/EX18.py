'''
18 - Leia um valor de volume  em metro m³ e apresente-o convertido em litros.  A
fómula de conversão é: L = 1000 * M, sendo L o volume em litros e M o volume em metros
cúbicos.
'''

mil = 1000
m = int(input('Informe um valor de volume em metros cúbicos: '))
lit = mil * m
print('O valor informado em litros é {:.0f}'.format(lit))
