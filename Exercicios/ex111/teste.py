'''
111 - Crie um pacote chamado utulidadesCeV
que tenha dois módulos internos chamados moeda e dado.

trnafira todas as funções utilizadas nos desafios 107, 108 e 109
para o primeiro pacote e mantenha tudo funcionando.
'''

'''
110 - Adicione ao módulo moeda.py criado nos desafios anteriores,
uma função chamada resumo(), que mostre na tela algumas informações
que ja temos no módulo criado ate aqui.
'''
from ex111.utilidadescev import moeda

p = float(input('Digite o preço: '))
moeda.resumo(p, 20, 12)
