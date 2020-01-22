'''
10 - Leia uma velocidade em km/h (quilômetros por hora) e apresente-a covertida em m/s
(metros por segundo). A fórmula de conversão é: M= K/3.6, sendo K a velocidade em km/he M
em m/s.
'''

# RESPOSTA

km = int(input('Iforme a velocidade em [KM/H]: '))
metros = km / 3.6
print('A velocidade convertida em [M/S] é {:.2f}'.format(metros))
