from datetime import date
nasc = int(input('Informe o ano de nascimento: '))
anoatual = date.today().year
saldo = anoatual - nasc
if anoatual - nasc < 18:
    print('Canditado ainda não está na idade de alistamento')
    print('Faltou {} anos para idade ideal para alistamento'.format(18 - saldo))
    print('Seu alistamento será em {}'.format(anoatual + 18 - saldo))
elif anoatual - nasc == 18:
    print('Canditato está na idade ideal para alistamento')
else:
    print('Candidato passou do tempo de alistamento')
    print('Passou {} anos da idade ideal para alistamento'.format(saldo - 18))
    print('Seu alismento deveria ser em {}'.format(anoatual - (saldo - 18)))
