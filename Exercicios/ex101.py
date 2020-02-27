'''
101 - Crie um programa que tenha uma função chamada voto() que vai receber como
parâmetro o ano de nascimento de uma pessoa, retornan um valor literal indicando
se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleiçôes.

'''


def voto(nasc):
    from datetime import datetime
    anoatual = datetime.today().year
    idade = anoatual - nasc
    print('-'*30)
    if idade <= 15:
        return f'Com {idade} anos: VOTO NEGADO.'
    elif 17 <= idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


'''Programa Principal'''
nas = int(input('EM que ano você nasceu? '))
print(voto(nas))
