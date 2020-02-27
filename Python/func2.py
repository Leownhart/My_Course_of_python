'''
- Interactive Help
- Docstrings
- Argumentos Opcionais
- Escopo de variáveis
- Retorno de Resultados

========================================================================
- Interactive Help

help () - Função interna do python, método aplicável.

Ex:
print(input.__doc__)
print(input)
========================================================================
- Docstrings

String de documentação - manual com funcionalidades internas.

def contador(i, f, p) <= Parâmetros formais
"""
-> Fazer contagem e mostrar na tela.
:param i: inicio da contagem
:param f: fim da contagem
:param p: passo da contagem
:return: sem retorno
"""
c = 1
while c <= f:
    print(f'(c)', end='..')
    c += p
print('FIM!')

contador(2, 10, 2) <= Parâmetros Reais
========================================================================
- Argumentos Opcionais

def somar(a=0, b=0, c=0): <= Zero como Argumemto opcional.
    """
    -> Faz a soma de três valores e mostrar o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Gustavo Guanabara do canal curso em Video.
    """
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
========================================================================
- Escopo de variáveis

def teste():
    global a <= transforma uma váriavel local em uma global.
    x = 8 == Local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa principal
n = 2 == Global
print(f'No programa principal, n vale {n}')
========================================================================
- Retorno de Resultados

    def somar(a=0, b=, c=0)
        s = a + b + c
        return s   <= Atribuindo Retorno de Resultado na Minha Função

    # Programa princinpal
    resp = somar(3, 2, 5) or print(somar(3, 2, 5))

    r1 = somar(3, 2, 5)

    r2 = somar(1, 7)

    r3 = somar(4)

    print(f'Meus cálculos deram (r1), (r2) e (r3).')
'''


