'''
108 - Adapte o código do desafio 107, Criando uma função adicional chamada moeda()
que consiga mostrar os valores como um valor monetário formatado.
'''

import m8

p = float(input("Digite o preço: R$"))
print(f'A metade de {m8.moeda(p)} é {m8.moeda(m8.metade(p))}')
print(f'O dobro de {m8.moeda(p)} é {m8.moeda(m8.metade(p))}')
print(f'Aumentando 10%, temos {m8.moeda(m8.aumentar(p, 10))}')