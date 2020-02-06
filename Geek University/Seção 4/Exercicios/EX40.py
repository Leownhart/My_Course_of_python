'''
40 - Uma empresa contrata um encanador a R$ 30,00, por dia, Faça um programa que solicite
o número de dias trabalhados pelo encanador e imprima a quantia liquida que deverá ser paga,
sabendo-se que são descontados 8% para imposto de renda.
'''

# RESPOSTA

dt = int(input('Informe a quantidade de dias trabalhados: '))
vliq = dt * 30.00
totalcd = 8 / 100 * vliq
print(f'O valor a ser pago com desconto de imposto de renda é {vliq - totalcd:.2f} R$')
