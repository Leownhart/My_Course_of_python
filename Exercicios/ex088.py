from random import randint
from time import sleep
lista = list()
jogos = list()
print('-'*30)
print('      JOGA NA MEGA SENA     ')
print('-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
print('-=' * 3, f'SORTEANDO {quant} JOGOS',  '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1} : {l}')
    sleep(0.3)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)

'''from random import randint  (Solução Incompleta)
from time import sleep
jogo = []

print('-'*25)
print(f'JOGA NA MEGA SENA'.center(25))
print('-'*25)
jogos = int(input('Quantos jogos deseja sortear? '))
print(f'-=-=-= SORTEANDO {jogos} JOGOS -=-=-=')
for j in range(0, jogos):
    for n in range(0, 6):
        jogo.append(randint(1, 60))
        sleep(0.1)
    print(f'Jogo {j+1}: {jogo}')
    jogo.clear()
    sleep(0.1)
print('-=-=-=-= < BOA SORTE! > -=-=-=-=-=')'''


