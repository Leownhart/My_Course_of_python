'''
07 - Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois
números forem iguais, imprima a mensagem número iguais.
'''


n1 = int(input('Número Um: '))
n2 = int(input('Número Dois: '))

if n1 > n2:
    print(f'O número {n1} é maior que {n2}')
elif n2 > n1:
    print(f'O número {n2} é maior que {n1}')
else:
    print(f'Os números {n1} é {n2} são iguais.')