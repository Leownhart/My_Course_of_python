'''
99 - Faça um programa que tenha uma função chamada maior(), que receba vários parâmetos
com valores inteiros.
Seu programa tem que analisar todos os valores e dizer queal deles é o maior.
'''


def maior(valores):
    maior = 0
    print('-=' * 20)
    print('Analisando os valores passados... ')
    for n in range(0, len(valores)):
        print(f'{valores[n]} ', end='')
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
maior(valores)


