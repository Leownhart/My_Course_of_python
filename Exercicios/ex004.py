a = input('Informe Algo: ')
print('O tipo primitivo desse valor é: {0}'.format(type(a)))
print('Só tem espaços: {0}'.format(a.isspace()))
print('É um número? {0}'.format(a.isnumeric()))
print('É alfabético? {0}'.format(a.isalpha()))
print('É alfanumérico? {0}'.format(a.isascii()))
print('Está em maiúsculo? {0}'.format(a.isupper()))
print('Está em minúsculo? {0}'.format(a.islower()))
print('Está capitalizada? {0}'.format(a.istitle()))
