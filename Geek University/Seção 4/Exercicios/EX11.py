'''
11 -Leia uma velocidade em m/s (metros por segundo) e apresente-a em km/h
(quilômetros por hora). A fórmula de conversão é: K = M * 3.6, sendo K
a velocidade em km/h e M em m/s
'''

# RESPOSTA

m = int(input('Informe uma velocida em m/s: '))
k = m * 3.6
print('A velocidAde informada convertida em km/h é {:.0f}'.format(k))
