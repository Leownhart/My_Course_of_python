dias =  int(input('Informe a quantidades de dias alugado? : '))
kmrod = float(input('Informe a quantidade de quilômetros percorrido: Km '))
precokm = kmrod * 0.15
precodia  = dias * 60.0
print('O valor final a pagar e: R${:.2f}'.format(precokm + precodia))

