'''67 - Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for
negativo.'''

cont = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('='*35)
    while cont < 10:
        cont += 1
        print(f'{n:.0f} x {cont:.0f} = {n*cont:.0f}')
    cont = 0
    print('='*35)
    if n <= 0:
        break
print('Acabou')
