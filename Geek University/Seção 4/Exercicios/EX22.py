'''
22 - Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula
de conversão é: M = 0.91 * J, sendo J o comprimento em jardas e M o Comprimento em metros.
'''

jard = int(input('Informe um valor de comprimento em jardas: '))
metros = 0.91 * jard
print('O valor do comprimento em jar convertido metros é {:.2f}'.format(metros))
