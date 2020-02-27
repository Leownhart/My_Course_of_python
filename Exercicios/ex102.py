'''
102 - Crie um programa que tenha uma função fatorial() que receba
dois parâmetros: o primeiro que indique o númeroa calcular e o outro
chamaddo show, que será um valor lógico (opcional) indicando se será mostrado ou não
na tela o processo de cáculo do fatorial.
'''


def fatorial(fat, show=False):
    f = 1
    for n in range(0, fat, -1):
        print(f'')


'''Programa Principal'''
fatorial(5, show=True)
