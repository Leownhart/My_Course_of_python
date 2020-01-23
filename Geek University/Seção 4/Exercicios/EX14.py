'''
14 - Leia um ângulo em graus e apresente-o convertido em radianos. A fómula
de conversão é R = G * PI / 180, sendo G o ângulo em graus e R em radianos
e PI = 3.14.
'''

# RESPOSTA

ang = int(input('Informe um ângulo em graus: '))
radi = ang * 3.14 / 180
print('O valor em graus convertido para radianos é {:.6f}: '.format(radi))
