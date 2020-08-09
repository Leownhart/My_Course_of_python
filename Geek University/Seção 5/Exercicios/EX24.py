'''
Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado
possui uma taxa deferente de imposto sobre o produto (MG:7%; SP:12%; RJ:15%; MS:8%).
Faça um programa em que o usuário entre com valor e o estado destino do produto
e o Programa retorne o preço final do produto acrescido do imposto do estado em que ele será vendido.
Se o estado digitado não for válido, mostrar uma mensagem de erro.
'''

vprod = float(input('Valor do produto: R$ '))
estado = str(input('Estado de destino: ')).strip()[0:1].upper()

if estado in 'MG':
    imposto = vprod * 7 / 100
    print(f'Preço final = R$ {vprod + imposto}')
elif estado in 'SP':
    imposto = vprod * 12 / 100
    print(f'Preço final = R$ {vprod + imposto}')
elif estado in 'RJ':
    imposto = vprod * 15 / 100
    print(f'Preço final = R$ {vprod + imposto}')
elif estado in 'MS':
    imposto = vprod * 8 / 100
    print(f'Preço final = R$ {vprod + imposto}')
else:
    print('Erro!')
