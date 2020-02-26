'''
96 - Faça um programa que tenha uma função chamada área(),
que receba as dimisões de um terreno retengular e comprimento) e mostre a área do terreno.

F ==> 2(b + h)

'''


def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno ({larg} x {comp}) é de {a:.1f}².')


print('Controle de Terrenos')
print('-' * 20)
larg = float(input('LARGURA (M): '))
comp = float(input('COMPRIMENTO (M): '))
área(larg, comp)
