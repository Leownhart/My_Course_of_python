'''
102 - Crie um programa que tenha uma função fatorial() que receba
dois parâmetros: o primeiro que indique o númeroa calcular e o outro
chamaddo show, que será um valor lógico (opcional) indicando se será mostrado ou não
na tela o processo de cáculo do fatorial.
'''


def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número escolhido;
    :param n: parãmetro que recebe um número escolhido;
    :param show: parãmetro de escolha de exibição;
    :return: retorna o resultado da função.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
        f = f * c
    return f


'''Programa Principal'''
vasp = int(input('Informe um número para fatorial: '))
print(fatorial(vasp, show=True))
