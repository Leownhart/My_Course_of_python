'''
13 - Leia uma distância em quilômetros e apresente-a convertida em  milhas.
A fómula de conversão é M - k / 1,61, sendo K a distância em quilõmetros e M
em milhas.
'''

# RESPOSTA

km = int(input('Informe uma distância em quilômetros: '))
m = km / 1.61
print('A distância convertida em milhas é {:.0f} milhas'.format(m))
