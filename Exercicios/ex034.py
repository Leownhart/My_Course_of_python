Sal = float(input('Infome o Sálario: R$ '))
if Sal >= 1250.00:
    Percent = Sal * 10 / 100
    print('Quem ganhava R${:.2f} passa a ganhar '
          'R${:.2f}'.format(Sal, Sal + Percent))
else:
    Percent = Sal * 15 / 100
    print('Quem ganhava R${:.2f} passa a ganhar '
          'R${:.2f}'.format(Sal, Sal + Percent))