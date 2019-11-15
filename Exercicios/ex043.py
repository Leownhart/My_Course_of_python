from math import pow
Peso = float(input('Digite o Peso (Kg): '))
Altura = float(input('Digite a altura (Mt): '))
imc = Peso / pow(Altura, 2)
if imc <= 18.5:
    print('Imc = \033[34m{:.1f}\033[m , o mesmo está abaixo do peso: '
          .format(imc))
elif imc < 25:
    print('Imc = \033[34m{:.1f}\033[m , o mesmo está no peso ideal'
          .format(imc))
elif imc < 30:
    print('Imc = \033[34m{:.1f}\033[m , o mesmo está em Sobrepeso'
          .format(imc))
elif imc < 40:
    print('Imc = \033[34m{:.1f}\033[m , o mesmo está em obsidade'
          .format(imc))
else:
    print('Imc = \033[34m{:.1f}\033[m , o mesmo está em obsidade mórbida'
          .format(imc))

