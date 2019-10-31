Sal = float(input('Qual é o salário do Funcionário?  R$ '))
Percent = 15.0
Acrescimo = Sal * Percent / 100
NewSal = Sal + Acrescimo
print('Um funcionário que ganhava R${:.2f}, com {:.0f}% de aumento, '
      'passa a receber R${:.2f}'.format(Sal, Percent, NewSal))
