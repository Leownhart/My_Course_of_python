'''
51 - Escreva um programa que leia as coordenadas x e y pontos R² e calcule sua distância
da origem (0,0)
'''

# RESPOSTA

from math import sqrt, pow

x = float(input('X: '))
y = float(input('Y: '))

res = sqrt(pow(x,2) + pow(y,2))

print(f'{res:.2f}')