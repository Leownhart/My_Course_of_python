'''
27 - Leia um valor de área em hectares e apresente-o convertido em metros quadrados m².
A fórmula de conversão é M = H * 1000, sendo M a área em metros quadrados e H a área em hectares.
'''

hect = int(input('Informe um  valor de área em hectares: '))
m = hect * 1000
print(f'O valor de área convertido em hectares é {m:.2f}')
