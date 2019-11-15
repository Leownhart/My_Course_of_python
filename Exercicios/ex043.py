from math import pow
Altura = float(input('Digite a altura (Mt): '))
Peso = float(input('Digite o Peso (Kg): '))
imc = Peso / pow(Altura, 2)
if imc <= 18.5:
    print('Imc = \033[34m{:.2f}\033[m , o mesmo está abaixo do peso: '
          .format(imc))
elif imc < 25:
    print('Imc = \033[34m{:.2f}\033[m , o mesmo está no peso ideal'
          .format(imc))
elif imc < 30:
    print('Imc = \033[34m{:.2f}\033[m , o mesmo está em Sobrepeso'
          .format(imc))
else:
    print('Imc = \033[34m{:.2f}\033[m , o mesmo está em obsidade mórbida'
          .format(imc))
