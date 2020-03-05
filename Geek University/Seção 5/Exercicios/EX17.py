'''
17 - Faça um programa que calcule e mostre a área de trapézio. Sabe-se que:
        A = (BASEMAIOR + BASEMENOR) * ALTURA / 2
Lembre-se a base maior e a base menor devem ser números maiores que zero.
'''

altura = float(input('Altura: '))
basemaior = float(input('Base Maior: '))
basemenor = float(input('Base Menor: '))

Area = ((basemaior + basemenor) * altura) / 2

print(f'A área do  trapézio informado é {Area:.2f}m² ')
