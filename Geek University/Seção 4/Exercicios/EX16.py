'''
16 -Leia um valor de comprimento em polegadas e apresente-o convertido em centimetros.
A fórmula de conversão é C = P * 2,54, sendo C o comprimento em centimetros e P o comprimento
em polegdas.
'''

p = int(input('Informe um valor de comprimento em polegadas: '))
c = (p * 2.54)
print('o valor informado em centimetros é {:.2f}'.format(c))
