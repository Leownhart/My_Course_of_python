Number = int(input('Digite um Número: '))
Dobro = Number * 2
Triplo = Number * 3
RaizQ = pow(Number, (1/2))  # ou Number ** (1/2)
print('O dobro de {} vale {}.'.format(Number, Dobro))
print('O triplo de {} vale {}.'.format(Number, Triplo))
print('A raiz quadrada de {} vale {:.2f}.'.format(Number, RaizQ))
