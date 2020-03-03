print('\033[4;30;45mOlá, Mundo!\033[m')
print('\033[7;33;44mOlá, Mundo!\033[m')
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m !!!'.format(a, b))
cores = {'limpa':'\033[m',
         'Azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretobranco':'\033[7;30m'}
nome = 'Francisco'
print('Olá! Muito prazer em te conhecer, {}{}{} !!!'.format(cores['pretobranco'], nome, cores['limpa']))



