Nome1 = str(input('Digite seu nome completo: '))
Nome2 = len(''.join(Nome1.split()))
Nome3 = Nome1.split()
Nome4 = Nome3[0]
print('Analisando seu nome...')
print('Seu nome em maiúsculo é {}'.format(Nome1.upper()))
print('Seu nome em miúsculo é {}.'.format(Nome1.lower()))
print('Seu nome tem ao todo {} letras'.format(Nome2))
print('Seu primeiro nome é {} e ele tem {} letras'.format(Nome4, len(Nome4)))





