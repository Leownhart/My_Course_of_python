'''
26 - Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro
em um percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com os dados abaixo:


CONSUMO -  Km/L - MENSAGEM

menor que   - 8 - Vendo o carro!
entre -  8 e 14 - econômico!
maior que - 12 - Super econômico!
'''

d = float(input('Informe a distância percorrida [Km]: '))
l = float(input('Informe a quantidade de combústivel consumido [L]: '))
cons = d / l

if cons < 8:
    print(f'Consumo = {cons:.0f}Km/l, Venda o carro!')
elif 8 < cons <= 14:
    print(f'Consumo = {cons:.0f}Km/l, Econômico')
elif cons > 12:
    print(f'Consumo = {cons:.0f}Km/l, Super econômico')

