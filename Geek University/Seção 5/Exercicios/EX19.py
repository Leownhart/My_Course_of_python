'''
 19 - Faça um programa para vericar se um determinado número inteiro e divisivel por 3 ou 5, mas não
simultaneamente pelos dois.
'''

number = int(input('Número: '))
if number % 3 == 0:
    print('É divisivel por 3')
elif number % 5 == 0:
    print('É divisivel por 5')
else:
    print('Não e divisilvel por 3 e nem por 5')
