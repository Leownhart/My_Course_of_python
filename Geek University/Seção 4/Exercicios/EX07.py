'''
Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus celsius.
A fórmula de conversão é C = 5.0 * (F -32.0) / 9.0, sendo C em Celsius e F
a temperatura em Fahrenheit.
'''

# RESPOSTA

f = int(input('Informe a temperatura em Fahrenheit: °'))
c = 5.0 * (f - 32.0) / 9.0
print('A temperatura informada em Celsius é °{:.1f}'.format(c))