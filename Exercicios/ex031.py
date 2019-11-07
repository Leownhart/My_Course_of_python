Via = int(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}km.'.format(Via))
if Via <= 200:
    Via = Via * 0.50
    print('O preço da sua passagem será {:.2f}'.format(Via))
else:
    Via = Via * 0.45
    print('O preco da sua passagem será {:.2f}'.format(Via))

# Mneira Simplificada
# 