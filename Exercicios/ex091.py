from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador 1': '', 'jogador 2': '', 'jogador 3': '', 'jogador 4': ''}
print('Valores Sorteados: ')
for k in jogadores.keys():
    jogadores['jogador 1'] = randint(1, 6)
    jogadores['jogador 2'] = randint(1, 6)
    jogadores['jogador 3'] = randint(1, 6)
    jogadores['jogador 4'] = randint(1, 6)
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
ranking = list()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}ª lugar: {v[0]} com {v[1]}.')
    sleep(1)


