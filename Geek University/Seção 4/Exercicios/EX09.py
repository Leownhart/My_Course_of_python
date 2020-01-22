'''
9 - Leia uma temperatura em graus Celsius e apresente-a comvertida em graus Kelvin.
A fórmula de conversão é K = C + 273.15, sendo C a temperatura em Celsius e K a temperatura
em Kelvin.
'''

# RESPOSTA

c = int(input('informe uma temperatura em celsius: °'))
k = c + 273.15
print('A temperatura convertida para klevin é {:.2f}K'.format(k))
