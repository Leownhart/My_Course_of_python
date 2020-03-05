'''
20 - Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo
e, se forem, se é um triângulo escaleno, equilátero, ou isóscele, considerando os seguintes conceitos:

* O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
* Chama-se equilátero o triângulo que tem três lafos iguais.
* Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
* Recebe o nome de escaleno o triângulo que tem is três ldos diferentes.

'''

A = float(input('Lado A: '))
B = float(input('Lado B: '))
C = float(input('Lado C: '))

if A == B == C:
    print('Triângulo Equilátero')
elif A == B or B == C or C == A:
    print('Triângulo Isósceles')
elif A != B != C:
    print('Triângulo Escaleno')