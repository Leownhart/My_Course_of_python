'''
15 - Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula
de conversão é: G = R * 180 / PI, sendo G o ângulo em graus e R em radianos e
PI = 3.14.
'''

# RESPOSTA

radi = int(input('Informe um ângulo em radianos: '))
grau = radi * 180 / 3.14
print('O valor do ângulo em radianos convertido em graus é {:.2f}'.format(grau))

