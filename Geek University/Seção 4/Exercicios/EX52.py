'''
52 - três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido
proporcionalmente ao valor que cada deu para a realização da aposta. Faça um programa
que leia quanto  cada apostador investiu, o valor do prêmio, e imprima quanto  cada um
ganharia do prêmio com base no valor investido.

'''

# RESPOSTA
def reais(um, dois, tres):
        """
        -> Formata as apostas em real
        :param um: Primeira aposta
        :param doism: Segunda aposta
        :param tres: Terceira aposta
        """
        print(f'Aposta 1 -> R${um:.2f}, Aposta 2 -> '
              f'R${dois:.2f}, Aposta 3 -> R${tres:.2f}')


Premio = float(input('Informe o valor do prêmio: R$ '))

JogadorOne = int(input('Jogador One: '))
JogadorTwo = int(input('Jogador Two: '))
JogadorThree = int(input('Jogador Three: '))

TotalJogado = JogadorOne + JogadorTwo + JogadorThree

ResOne = (JogadorOne / TotalJogado) * Premio
ResTwo = (JogadorTwo / TotalJogado) * Premio
ResThree = (JogadorThree / TotalJogado) * Premio

reais(ResOne, ResTwo, ResThree)