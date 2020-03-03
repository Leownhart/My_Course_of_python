"""
109 = Modifique as funções que foram criadas no desafio 107
para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não
for,atado pela função moeda(), desenvolvida no desafio 108.
"""

import m9

p = float(input("Digite o preço: R$"))
print(f'A metade de {m9.moeda(p)} é {m9.metade(p, True)}')
print(f'O dobro de {m9.moeda(p)} é {m9.metade(p, True)}')
print(f'Aumentando 10%, temos {(m9.aumentar(p, 10, True))}')
print(f'Reduzindo 13%, temos {m9.diminuir(p, 13, True)}')
