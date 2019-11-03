from random import shuffle
Primeiro = str(input('Primeiro Aluno: '))
Segundo = str(input('Segundo Aluno: '))
Terceiro = str(input('Terceiro Aluno: '))
Quarto = str(input('Quarto Aluno: '))
list = [Primeiro, Segundo, Terceiro, Quarto]
shuffle(list)
print('A ordem de Apresentação será\n{}'.format(list))
