'''
43 - Escreva um programa de ajuda para vendedores. A parti de um valor total lido, mostre:

    * o total a  pagar com desconto de 10% OK;
    * o valor de cada parcela, no parcelamento de 3x sem juros OK;
    * a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
    * a comissão do  vendedor, no caso da venda  ser parcelada (5% sobre o valor total)
'''

# RESPOSTA

val = float(input('Informe um valor em (R$): '))
dez = 10 / 100 * val
parc = val / 3
avdes = 5 / 100 * dez
cinco = 5 / 100 * val

print(f'Valor com desconto de 10% {val - dez:.2f}')
print(f'O valor da parcela em 3x é: {parc:.2f}')
print(f'Comissão se parcelado em 3x {cinco:.2f} ')
print(f'Comissão 5% no valor do desconto {avdes + dez:.2f}')



