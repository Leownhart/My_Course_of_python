'''
36 - Leia a altura e o raio de cilindro circular e imprima o valume do cilindro. O volume
de cilindro circular é calculado por meio da seguinte fórmula: V = pi * raio² * altura, onde
pi = 3.14159.
'''

# RESPOSTA

from math import pi
alt = float(input('Informe uma altura em metros: '))
rai = float(input('Informe o raio do cilindro: '))
v = pi * pow(rai, 2) * alt
print(f'O volume so cilindro sugerido é: {v:.3f} Litros')

