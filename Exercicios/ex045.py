from time import sleep
from random import randint
list = ['1', '2', '3']
escolhido = randint(1,3)
print('Suas opções: ')
print('''[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jogada = int(input('Qual é sua jogada? '))
print('JO'), sleep(1), print('KEN'), sleep(1), print('POO!!'), sleep(1)
print('-='*15)
if escolhido == 1:
    print('Computador jogou Pedra')
elif escolhido == 2:
    print('Computador jogou Papel')
elif escolhido == 3:
    print('Computador jogou Tesoura')
if jogada == 1:
    print('Jogador jogou Pedra')
elif jogada == 2:
    print('Jogador jogou Papel')
elif jogada == 3:
    print('Jogador jogou Tesoura')
print('-='*15)
if escolhido == jogada:
    print('JOGADOR EMPATOU COM O COMPUTADOR')
elif escolhido == 1 and jogada == 2:
    print('JOGADOR VENCE')
elif escolhido == 1 and jogada == 3:
    print('COMPUTADOR VENCE')
elif escolhido == 2 and jogada == 1:
    print('COMPUTADOR VENCE')
elif escolhido == 2 and jogada == 3:
    print('JOGADOR VENCE')
elif escolhido == 3 and jogada == 1:
    print('JOGADOR VENCE')
elif escolhido == 3 and jogada == 2:
    print('COMPUTADOR VENCE')




