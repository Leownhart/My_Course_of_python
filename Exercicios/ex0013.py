#Sal = float(input('Qual é o salário do Funcionário?  R$'))
#Acrescimo = Sal * 15.0 / 100
#NewSal = Sal + Acrescimo
#print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, '
# 'passa a receber R${:.2f}'.format(Sal, NewSal))

Preco = float(input('Informe o o preço do produto: R$'))
PrecoDesc =  Preco - (Preco * 10 / 100)
PrecoAcres = Preco + (Preco * 8 / 100)
print('{}R$ com desconto de 10% é igual a {:.2f}R$'.format(Preco, PrecoDesc))
print('{}R$ com acrescimo de 8% é igual a {:.2f}R$'.format(Preco, PrecoAcres))




