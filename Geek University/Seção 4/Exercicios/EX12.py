'''
12 - Leia uma distância em milhas e apresente-a convertida em quilômetros.
A fórmula de conversão é: K = 1.61 * M, sendo K a distância em quilômetors e M
em milhas.
'''

# RESPOSTA

milhas = int(input('Informe um valor em quilômetros: milhas '))
km = 1.61 * milhas
print('A distância em milhas convertida para km é {:.0f}km '.format(km))
