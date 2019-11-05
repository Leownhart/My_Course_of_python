# nome = str(input('Qual é seu nome? '))
# if nome == 'Francisco':
#     print('Que nome lindo você tem!')
# else:
#     print('Seu nome é tão Simples')
# print('Bom dia, {}!'.format(nome))

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! Parabéns')
else:
    print('Sua média foi ruim! Estude mais!')

# print('PARABÉNS' if m >=6 else 'ESTUDE MAIS!')