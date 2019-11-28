'''57 - Faça um programa que leia o sexo de uma pessoa
os valores 'M' ou 'F'. Caso esteja errado,
peça a digitação navamente até ter um valor correto.'''

'''n = str(input('Informe seu SEXO [M/F]: ')).strip().upper()[0]
while n != 'M' or n != 'F':
    if n == 'M' or n == 'F':
        print('Sexo \033[31m{}\033[m registrado com sucesso'.format(n))
    else:
        print('Dados inválidos. Por favor, informe seu sexo: ')
        n = str(input('Informe seu SEXO [M/F]: ')).strip().upper()[0]
print('Fim')'''

sexo = str(input('Informe seu sexo [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'. format(sexo))