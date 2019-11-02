from math import pow, sqrt
oposto = float(input('Comprimento do cateto oposto: '))
ajacente = float(input('Comprimento do cateto adjacente: '))
hipot = sqrt(pow(oposto, 2) + pow(ajacente, 2))
print('A hipotenusa vai medir {:.2f}'.format(hipot))
