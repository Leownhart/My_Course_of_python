jogador = dict()
gols = list()
quant = 0
jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
cont = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for n in range(0, cont):
    gol = int(input(f'Quantos gols na partida {n}? '))
    gols.append(gol)
    jogador['gols'] = gols[:]
    quant += gols[n]
jogador['total'] = quant
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {cont} partidas.')
for n in range(0, len(gols)):
    print(f' => Na partida {n}, fez {gols[n]}')
print(f'Foi um total de {quant} gols')