'''
37 - Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo
em vista que o desconto foi de 12%.
'''

# RESPOSTA

val = float(input('Informe um valor: R$ '))
desc = 12 / 100 * val
print(f'O desconto de 12% em cima do valor informado é: {desc:.2f}')


