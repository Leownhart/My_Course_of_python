'''
18  - Faça um programa que mostre ao usuário um menu com 4 opções de operaçôes matemáticas
(as básicas, por exemplo). O usuário escolhe uma da opções e o seu programa
então pede dois valores numéricos e realiza a operação, mostrando o resultado e saindo.
'''

print('-='*7)
print('1 - Somar\n'
      '2 - Subtrair\n'
      '3 - Multiplicar\n'
      '4 - Dividir')
print('-='*7)

number = int(input('Informe uma Opção: '))
number2 = int(input('Número Um: '))
number3 = int(input('Número Dois: '))
if number == 1:
    print(f'A soma é {number2 + number3:.0f}')
elif number == 2:
    print(f'A Subtração é {number2 - number3:.0f}')
elif number == 3:
    print(f'A Multiplicação é {number2 * number3:.0f}')
elif number == 4:
    print(f'A Divisão é {number2 / number3:.0f}')

