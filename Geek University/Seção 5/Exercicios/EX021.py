'''
21 - Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida.
Escreva uma mesagem de erro se a opção for inválida.

Escolha a opção:

1 - Soma de 2 números.
2 - Diferença entre 2 números (maior pelo menor)
3 - Produto entre 2 números.
4 - Divisão ente 2 números (o denominador não pode ser zero).
'''

print('[1] Soma de 2 números. \n'
      '[2] Diferença entre 2 números (maior pelo menor) \n'
      '[3] Produto entre 2 números. \n'
      '[4] Divisão ente 2 números (o denominador não pode ser zero).')
op = int(input('Opção: '))
number1 = int(input('Número 1: '))
number2 = int(input('Número 2: '))
if op == 1:
    print(f'Soma = {number1 + number2}')
elif op == 2:
    if number1 > number2:
        print(f'Diferença entre {number1} é {number2} = {number1 - number2}')
    else:
        print(f'Diferença entre {number2} é {number1} = {number2 - number1}')
elif op == 3:
    print(f'O produto é {number1 * number2}')
elif op == 4:
    if number1 > 0:
        print(f'{number1 / number2}')
    else:
        print('O denominador e inválido')


