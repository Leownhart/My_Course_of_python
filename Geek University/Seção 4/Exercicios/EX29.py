'''
29 - Leia quatro notas, calcule a média aritmética e imprima o resultado.
'''

med = som = 0
for n in range(1, 5):
    np = float(input(f'Informe a nota Nª{n}: '))
    som = som + np
med = som / 4
print(f'A média aritmética é {med:.1f}')

