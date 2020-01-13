Clubes = (' ', 'Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo',
          'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco',
          'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA',
          'Chapecoense', 'Avai')

print('Lista de Clubes do Brasileirão')
print('-='*10)
for Clube in Clubes:
    if Clubes.index(Clube) != 0:
        print(f'{Clubes.index(Clube)}. {Clube}')
print('-='*10)
print(f'Os cinco primeiros são {Clubes[1:6]}')
print(f'Os quatro últimos são {Clubes[-4:]} ')
print(f'Times em ordem alfabética {sorted(Clubes)}')
print(f'O Chapecoense está na posição {Clubes.index("Chapecoense")}ª')







