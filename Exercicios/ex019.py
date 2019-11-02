from random import choice
Primeiro = str(input('Primeiro Aluno: '))
Segundo = str(input('Segundo Aluno: '))
Terceiro = str(input('Terceiro Aluno: '))
Quarto = str(input('Quarto Aluno: '))
list = [Primeiro, Segundo, Terceiro, Quarto]
escolhido = choice(list)
print('O aluno escolhido foi : {}'.format(escolhido))


