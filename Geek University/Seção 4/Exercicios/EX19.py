"""
19 - Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m³.
A fórmula de conversão é: M = L / 1000, sendo L o volume em litros e M o volume em metros
cúbicos.
"""

l = int(input('Informe um valor em litros: '))
m = l / 1000
print('O volume informado convetido em metros cúbicos é {:.5f}'.format(m))
