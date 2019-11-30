'''67 - Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for
negativo.'''

cont = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('\033[34m=\033[m'*35)
    if n <= 0:
        break
    while cont < 10:
        cont += 1
        print(f'\033[33m{n:.0f}\033[m x \033[32m{cont:.0f}\033[m= '
              f'\033[31m{n*cont:.0f}\033[m')
    cont = 0
    print('\033[34m=\033[m'*35)
print('Acabou')
