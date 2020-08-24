'''
27 - Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:


Categoria - Idade

Infantil A   5 a 7
Infantil B   8 a 10
Juvenil A    11 a 13
Juvenil B    14 a 17
Sênior       Maiores de 18 anos
'''

i = int(input('Informe a idade de nadador: '))


if 5 >= i <= 7:
    if i < 5:
        print(f'((((Valor Inválido))))')
    else:
        print(f'Idade igual a {i} anos, nadador infantil A')
elif 8 >= i <= 10:
    print(f'Idade igual a {i} anos, nadador infantil B')
elif 11 >= i <= 13:
    print(f'Idade igual a {i} anos, nadador Juvenil A')
elif 14 >= i <= 17:
    print(f' Idade igual a {i} anos, nadador Juvenil B')
else:
    print(f'Idade igual a {i} anos, nadador Sênior')

