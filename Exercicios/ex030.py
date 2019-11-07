Number = int(input('\033[0;33mInforme um número: \033[m'))
if Number % 2 == 0.0:
    print('O número \033[0;33;44m{}\033[m é \033'
          '[0:33mPar\033[m'.format(Number))
else:
    print('O número \033[0;33;44m{}\033[m é \033'
          '[0:33mImpar\033[m'.format(Number))
