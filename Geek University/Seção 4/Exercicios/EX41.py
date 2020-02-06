'''
41 - Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas
trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.
'''

# RESPOSTA

ht = float(input('Informe o valor da hora trabalhada em reais : '))
hm = int(input('Informe o número de horas trabalhados no mês: '))
total = hm * ht
desc = (10 / 100) * total
print(f'O valor a ser pago acrescimo é {total - desc:.2f}')
