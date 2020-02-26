'''
97 - Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
como parâmetro e mostre uma mesagem com tamanho daptável.

Ex. escreva('Olá, Mundo!')

Saida:
------------
Olá, Mundo!
------------
'''


def escreva(frase):
    t = len(frase) + 4
    print('~' * t)
    print(f'  {frase}')
    print('~' * t)


frase = 'Francisco Leandro'
escreva(frase)

frase = 'Curso de Python no Youtube'
escreva(frase)


frase = 'CeV'
escreva(frase)

