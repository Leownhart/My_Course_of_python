'''63 - Escreva  um programa que leia um número n inteiro
qualquer e mostre na tela os n primeiros elementos de uma sequência
de fibonacci.

Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8.'''

n = int(input('Quantos termos você que mostrar? ')) # quantidade de termos
t1 = 0 # termo um
t2 = 1 # termo dois
print('{} -> {}'.format(t1, t2), end='')  # exibindo os termos
cont = 3 # contador comçando com três
while cont <= n:
    t3 = t1 + t2 # termo três e a soma dos dois primeiros termos /
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print(' Fim')


