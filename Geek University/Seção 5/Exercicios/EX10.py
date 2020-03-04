'''
10. Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes fórmulas (onde h corresponde á altura):

Homens: (72.7 * h) - 58
Mulheres: (62.1 * h) - 44,7
'''

alt = float(input('Altura: '))
sexo = str(input('Sexo [M/f]: ')).strip()[0]

if sexo in 'mM':
    homen = (72.7 * alt) - 58
    print(f'O peso ideal para os dados informados é {homen:.0f}Kg')
elif sexo in 'fF':
    mulher = (62.1 * alt) - 44.7
    print(f'O peso ideal para os dados informados é {mulher:.0f}Kg')
