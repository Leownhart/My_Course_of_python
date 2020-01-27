'''
34 - Leia o valor do raio de um circulo e calcule e imprima a área do circulo correspondente.
A área do circulo é PI * RAIO², considere PI = 3.14592.
'''
rai = float(input('Informe o valor do raio: '))
area = 3.14592 * pow(rai, 2)
print(f'A área do circulo correspondente é {area:.2f}')
