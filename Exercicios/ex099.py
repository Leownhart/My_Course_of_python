'''
99 - Faça um programa que tenha uma função chamada maior(), que receba vários parâmetos
com valores inteiros.
Seu programa tem que analisar todos os valores e dizer queal deles é o maior.
'''
from time import sleep


def maior(* núm):
    cont = maior = 0
    print('-=' * 30)
    print('\nAnalisando os valores passados...')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


#Programa Principal
maior(2, 9, 5, 6, 7, 1)
maior(4, 7, 8)
maior(1, 2)
maior(6)
maior()

'''from time import sleep


def maior(valores):
    maior = 0
    print('-=' * 20)
    print('Analisando os valores passados... ')
    for n in range(0, len(valores)):
        sleep(0.5)
        print(f'{valores[n]} ', end='', flush=True)
        if maior < valores[n]:
            maior = valores[n]
    print(f'Foram informados {len(valores)} valores ao todo')
    print(f'O maior valor informado foi {maior}')


valores = [2, 9, 4, 5, 7, 1]
maior(valores)

valores = [4, 7, 0]
maior(valores)

valores = [1, 2]
maior(valores)

valores = [6]
maior(valores)

valores = [0]
maior(valores)'''


