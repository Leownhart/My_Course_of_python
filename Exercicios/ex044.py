price = float(input('Preço das compras: R$'))
print('''
  [ 1 ] á vista dinheiro/cheque
  [ 2 ] á vista cartão
  [ 3 ] 2x no cartão
  [ 4 ] 3x ou mais no cartão 
''')
option = int(input('Qual é a opção? '))
desconto1 = price * 10 / 100
desconto2 = price * 5 / 100
juros = price * 20 / 100
if option == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'
          .format(price, price - desconto1))
elif option == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'
          .format(price, price - desconto2))
elif option == 3:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'
          .format(price))
elif option == 4:
    parcela = int(input('Informe a quantidade de parcelas: '))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no fianl'
          .format(price, price + juros))
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'
          .format(parcela, (price + juros) / parcela))
