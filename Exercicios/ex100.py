'''
100 - Faça um programa que tenha uma lista chamada números e duas funções
chamadas sorteia() e somapar(). A primeira função vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função vai mostrar a soma entre todos
os valores pares sorteados pela função anterior.
'''

from random import randint
from time import sleep

sor = []


def sorteia(sor):# Função para sortear os números.
    for n in range(0, 5):
        sor.append(randint(0, 9))
    print(f'Sorteando {len(sor)} valores da lista: ', end='', flush=True)
    for n in range(0, len(sor)):
        print(f'{sor[n]} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!', end='')


def somapar(sor):# Função para somar os valores pares dentro da lista.
    somar = 0
    for n in range(0, len(sor)):
        if sor[n] % 2 == 0:
            somar += sor[n]
    print(f'\nSomando os valores pares de {sor}, temos {somar}')


sorteia(sor)
somapar(sor)

