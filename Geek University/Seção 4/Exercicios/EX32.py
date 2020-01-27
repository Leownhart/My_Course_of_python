'''
32 - Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.
'''

s = 0
n = int(input('Informe um valor: '))
ant = (n-1) * 3
suc = (n+1) * 2
print(f'soma do sucessor de seu triplo com o antecessor de seu dobro é {ant + suc}')


