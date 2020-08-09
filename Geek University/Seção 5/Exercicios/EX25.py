'''
25 - Calcule as raizes da equação de 2º grau....

Lembrando que:

x = -b +- raiz delta / 2a
        Onde
delta = B² - 4ac

E ax² + bX + C = 0 REPRESENTA UMA EQUAÇÃO DE 2º GRAU.

A variável a tem que ser diferente de Zero. Caso seja igual, imprima a mensagem
"Não é uma equação de segundo Grau".

* Se delta < 0, não existe real, Imprima a mensagem Não existe raiz
* Se delta = 0, existe uma raiz real, Imprima a raiz e a mesagem Raiz única
* Se >- 0, imprima as duas raizes reais.
'''

from math import pow, sqrt

a = float(input('Primeiro valor: '))
b = float(input('Segundo Valor: '))
c = float(input('Terceiro Valor: '))

delta = pow(b, 2) - (4 * a * c)
print(f'Delta: ', {delta})

if delta > 0:
    x1 = ((-b + pow(delta, 0.5)) / 2.0 * a)
    x2 = ((-b - pow(delta, 0.5)) / 2.0 * a)
    print(f' x1 = {x1:.0f} , x2 = {x2:.0f}')
else:
    print('Não pode ser calculado')