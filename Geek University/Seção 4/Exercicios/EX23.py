'''
23 - Leia um valor de comprimento em metros e apresente-o convertido em jardas. A fórmula
de conversão é: J = M / 0.91, sendo J o comprimento em jardas e M o comprimento em metros.
'''

met = int(input('Informe um valor de comprimento em metros: '))
jard = met / 0.91
print('O valor do comprimento em metros convertido em jards é {:.2f}'.format(jard))
