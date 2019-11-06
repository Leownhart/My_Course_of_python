from random import randint
from time import sleep
com = randint(0, 5) # Faz o computador "Pensar" um número
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei ? '))
print('Processando...')
sleep(2)
if com == jogador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(com, jogador))






