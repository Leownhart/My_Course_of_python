'''
38 - Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sbendo que
ele recebeu um aumento de 25%.
'''

# RESPOSTA

base = float(input('Informe o valor de um  salário em reais: R$ '))
acres = 25 / 100 * base
print(f'O valor do salário com aumento é {base + acres:.2f}')
