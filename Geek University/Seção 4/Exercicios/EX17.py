'''
17 - Leia um valor de comprimento em centimetros e apresente-o convertisdo em  polegadas.
A fórmula de conversão é P = C / 2.54, sendo C o comprimento em centimetros e P o comprimento em
polegadas.
'''

c = int(input('Informe um valor em centimetros: '))
p = (c / 2.54)
print('O valor informado convertido em polegadas é {:.2f}'.format(p))
