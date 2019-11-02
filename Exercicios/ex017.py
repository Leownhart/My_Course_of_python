from math import pow, sqrt
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipot = sqrt(pow(oposto, 2) + pow(adjacente, 2))
# ou (oposto ** 2 + adjacente ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipot))
