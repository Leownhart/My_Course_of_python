real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 4.00  # Conversor de Moedas
euro = real / 4.44
iene = real / 0.037
pesoarg = real / 0.067
print('Com R${:.2f} você pode comprar US$ {:.2f}'.format(real, dolar))
print('Com R${:.2F} você pode comprar € {:.2f}'.format(real, euro))
print('Com R${:.2F} você pode comprar ¥ {:.2f}'.format(real, iene))
print('Com R${:.2F} você pode comprar ₱ {:.2f}'.format(real, pesoarg))



