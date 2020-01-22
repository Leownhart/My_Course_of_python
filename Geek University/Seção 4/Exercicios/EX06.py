'''
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A fórmula de conversão é: F = C * (9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius.
'''

# RESPOSTA

c = int(input('Informe a temperatura em graus celcius: °'))
f = c * (9.0/5.0) + 32.0 # Fómula da conversão
print('A temperatura informada em graus fahrenheit é °{:.0f}'.format(f))
