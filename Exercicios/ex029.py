import math
km = float(input('Qual é a velocidade atual do carro? '))
if km <= 80:
    print('Tenha um bom dia! Dirija com segurança')
else:
    multa = (km - 80) * 7
    print('MULTADO! Você execedeu o limite permitido que é 80km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
    print('Tenha um bom dia! Dirija com segurança!')
