'''
42 - Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse
funcionario tem uma gratificação de 5% sobre o salário-base. Além disse, ele paga  7% de imposto sobre o
salário-base.
'''

# RESPOSTA

sbase = float(input('Informe o sálario base de um funcionário: '))
grati = 5 / 100 * sbase
desct = 7 / 100 * sbase
print(f'Total a receber: {sbase - desct + grati:.2f}')
