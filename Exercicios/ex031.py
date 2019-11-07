Via = int(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}km.'.format(Via))
if Via <= 200:
    preco = Via * 0.50
else:
    preco = Via * 0.45
print('O preco da sua passagem será {:.2f}'.format(preco))
# Maneira Simplificada
# preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45