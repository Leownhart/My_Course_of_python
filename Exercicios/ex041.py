from datetime import date
nasc = int(input('Ano de Nascimento: '))
anoat = date.today().year
idade = anoat - nasc
if idade <= 9:
    print('Atleta tem {} anos e está na categoria Mirim'.format(idade))
elif 9 < idade <= 14:
    print('Atleta tem {} anos e está na categoria Infantil'.format(idade))
elif 14 < idade <= 19:
    print('Atleta tem {} anos e está na categoria Junior'.format(idade))
elif 19 < idade <= 25:
    print('Atleta tem {} anos e está na categoria Sênior'.format(idade))
else:
    print('Atleta tem {} anos e está na categoria Master, Blaster, Flaster'.format(idade))

