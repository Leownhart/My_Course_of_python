nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome em {} letras'.format(nome.find(' ')))

# Nome1 = str(input('Digite seu nome completo: ')) # Strip é uma melhor opção.
# Nome2 = len(''.join(Nome1.split()))
# Nome3 = Nome1.split()
# Nome4 = Nome3[0]
# print('Analisando seu nome...')
# print('Seu nome em maiúsculo é {}'.format(Nome1.upper()))
# print('Seu nome em miúsculo é {}.'.format(Nome1.lower()))
# print('Seu nome tem ao todo {} letras'.format(Nome2))
# print('Seu primeiro nome é {} e ele tem {} letras'.format(Nome4, len(Nome4)))





