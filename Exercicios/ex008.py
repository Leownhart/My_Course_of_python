Dis = float(input('Uma distância em metros: '))
Qui = Dis / 1000
Hec = Dis / 100
Dec = Dis / 10
Deci = Dis * 10
Cen = Dis * 100
Mil = Dis * 1000
print('A medida:{:.1f}m corresponde a'.format(Dis))
print('Quilômetro:{:.3f}km'.format(Qui))
print('Hectômetro:{:.2f}hm'.format(Hec))
print('Decâmetro:{:.1f}dam'.format(Dec))
print('Decimetro:{:.0f}dm'.format(Deci))
print('Centimetro:{:.0f}cm'.format(Cen))
print('Milimetro:{:.0f}mm'.format(Mil))
