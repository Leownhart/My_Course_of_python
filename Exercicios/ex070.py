print('-' * 30), print('Loja Magazine'.center(30)), print('-' * 30)
precos = []
preco_mil = menor_preco = 0
menor_preco_nome = ''
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço - R$: '))
    precos.append(preco)
    if preco <= min(precos):
        menor_preco_nome = nome
        menor_preco = preco
    if preco > 1000:
        preco_mil += 1
    condicao_1 = str(input('Deseja continuar SIM[S] ou NÃO[N]: '))[0].strip().upper()
    while condicao_1 not in 'SN':
        condicao_1 = str(input('Deseja continuar SIM[S] ou NÃO[N]: '))[0].strip().upper()
    if condicao_1 == 'N':
        break
print('{:-^30}'.format(' CAIXA ENCERRADO '))
print('O total da compra é de R${}'.format(sum(precos)))
print('Total de produtos acima de R$1000: {}'.format(preco_mil))
print('Produto mais barato: {} >> Preço R${:.2f}'.format(menor_preco_nome, menor_preco))