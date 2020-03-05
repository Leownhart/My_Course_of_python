'''
15 - Usando um switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia
da semana correspondente a este numero. Isto é, domingo se 1, segunda-feira se 2, e assim
por diante.

Obs: if, elif, else no caso do Python.
'''


opção = int(input('Informe um número [1 a 7]: '))

if opção == 1:
    print('Dómingo')
elif opção == 2:
    print('Segunda-Feira')
elif opção == 3:
    print('Terça-Feira')
elif opção == 4:
    print('Quarta-Feira')
elif opção == 5:
    print('Quinta-Feira')
elif opção == 6:
    print('Sexta-Feira')
elif opção == 7:
    print('Sábado')