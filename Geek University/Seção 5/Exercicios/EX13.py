'''
13 - Faça um algoritmo que calcule a média ponderada das notas de três provas. A primeira e
a segunda prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e
indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 6.0.
'''

soma = med = 0
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))

mp = ((1 * n1) + (1 * n2) + (3 * n3)) / 5
if mp <= 5:
    print('Aluno Reprovado')
else:
    print('Aluno Aprovado')

print(f'A média poderada das notas é {mp:.2f}')
