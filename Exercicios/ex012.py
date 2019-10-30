Preco =  float(input('Qual é o preco do produto R$: '))
Percent = 5.0
Descont = Preco * Percent / 100.00
NewPreco = Preco - Descont
print('O produto que custava R${:.2f},'
      ' na promoção com desconto de '
      '{:.0f}% vai custar R${:.2f}'.format(Preco, Percent, NewPreco))
#