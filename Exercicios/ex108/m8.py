def aumentar(preco=0, taxa=0):
    res = preco + (preco * taxa / 100)
    return res


def diminuir(preco=0, taxa=0):
    res = preco - (preco * taxa / 100)
    return res


def dobro(preco=0):
    res = preco * 2
    return res


def metade(preco=0):
    res = preco / 2
    return res


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')  # Substituição de ponto por virgula


'''def aumentar(preco, taxa):
    res = preco + (preco * taxa / 100)
    return f'R${res:.0f}'


def diminuir(preco, taxa):
    res = preco - (preco * taxa / 100)
    return f'R${res:.0f}'


def dobro(preco):
    res = preco * 2
    return f'R${res:.0f}'


def metade(preco):
    res = preco / 2
    return f'R${res:.0f}'''
