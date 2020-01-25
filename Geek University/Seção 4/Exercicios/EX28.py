'''
28 - Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.
'''

lis = []
som = 0
for c in range(0, 3):
    number = int(input('Informe o valor: '))
    number = number ** 2
    lis.append(number)

    if number in lis:
        som = som + lis[c]
print(print(f'A soma dos quadrados dos três valores é {som:.0f}'))
