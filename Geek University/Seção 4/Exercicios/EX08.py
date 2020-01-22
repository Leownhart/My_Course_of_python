'''
Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C = K - 273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin.
'''

# RESPOSTA

k = int(input('Informe uma temperatura em graus Kelvin: K '))
c = k - 273.15
print('A temperatura convertida em celsius e °{:.2f}'.format(c))
