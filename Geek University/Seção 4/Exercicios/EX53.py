'''
53 - Faça um programa para ler as dimensões de um terreno (comprimento c e largura l),
bem como o preço do metro de tela  p, Imprima o custo para cercar este  mesmo terreno com tela.
'''

# RESPOSTA


ptela = float(input('Preço por (MT): R$ '))

comp = float(input('Comprimento (MT): '))
larg = float(input('Largura (MT): '))

tt = comp * larg
precot = comp * larg * ptela

print(f'Tamanho do Terreno {tt:.0f}m²')
print(f'Valor para cercalo R${precot:.2f}')
