'''
106 - Faça um mini-sistema que utilize o interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer .
quando o usuário digitar a palavra 'FIM', o programa se encerrará.

OBS: Use cores.
'''


def sistem():
    while True:
        option = str(input('Informe o manual que deseja ver: '))
        print('\033[0:31:43m-=\033[m' * 7)
        print(f'\033[0:31:43mManual {option} \033[m')
        print('\033[0:31:43m-=\033[m' * 7)
        print(help(option))
        esc = str(input('\033[0:34:43Deseja continuar? [S/N]: \033[m'))
        if esc in 'nN':
            break


# Programa principal
print('\033[0:31:42m-=\033[m' * 12)
print('\033[0:31:42m MINI-SISTEMA DE MANUAIS\033[m')
print('\033[0:31:42m-=\033[m' * 12)
sistem()
