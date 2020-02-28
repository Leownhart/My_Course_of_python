'''
104 - Crie um programa que tenha a função leiaint(), que vai
funcionar de forma semelhante á função input() do Python, só
que fazendo a validação para aceitar apenas um valor numérico.


Ex:
n = leiaint('Digite um número')
'''


def leiaInt(msg):
    """
    --> Válida um tipo númerico
    :param msg: recebe os dados lidos na chamada da função
    :return: retorna o resultado depois do teste lógico
    """
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(' \033[0:31mERRO! Digite um número inteiro válido. \033[m')
        if ok:
            break
    return valor


n = leiaInt('Informe um número: ')
print(f'Você acabou de digitar o número {n}')
