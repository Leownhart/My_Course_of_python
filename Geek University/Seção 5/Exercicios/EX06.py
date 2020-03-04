'''
06- Escreva um programa que, dados dois números inteiros, Mostre na tela o maior deles,
assim como a diferença existente entre ambos.
'''

n1 = int(input('Número Um: '))
n2 = int(input('Número Dois: '))

if n1 > n2:
    print(f'O número {n1} é maior que {n2}')
    print(f'A diferença entre eles é {n1 - n2}')
else:
    print(f'O número {n2} é maior que {n1}')
    print(f'A diferença entre eles é {n2 - n1}')