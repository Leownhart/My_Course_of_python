print('\033[31m{:=^40}\033[m'.format('\033[33m LOJAS FRANCISCO \033[m'))
price = float(input('Preço das compras: R$ '))
print(''' [ 1 ] á vista dinheiro/cheque
 [ 2 ] á vista cartão
 [ 3 ] 2x no cartão
 [ 4 ] 3x ou mais no cartão''')
option = int(input('Qual é a opção? '))
if option == 1:
    desconto = price * 10 / 100
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(price, price - desconto))
elif option == 2:
    desconto = price * 5 / 100
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(price, price - desconto))
elif option == 3:
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS '.format(price / 2))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(price, price))
elif option == 4:
    juros = price * 20 / 100
    parcela = int(input('Informe a quantidade de parcelas: '))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(price, price + juros))
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(parcela, (price + juros) / parcela))
else:
    print('DADOS INVALIDOS!')
