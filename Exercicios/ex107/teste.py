'''
107 - Crie um módulo chamado moeda.py que tenha as funções incorporadas

* aumentar()
* diminuir()
* dobrar()
* metade()

Faça tabém um programa que importe esse módulo e use
algumas dessas funções.'''

import m7

p = float(input("Digite o preço: R$ "))
print(f'A metade de R${p} é {m7.metade(p)}')
print(f'O dobro de R${p} é {m7.dobro(p)}')
print(f'Aumentando 10%, temos {m7.aumentar(p, 10)}')