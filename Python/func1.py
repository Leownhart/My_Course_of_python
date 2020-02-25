'''

* Exemplos de Funções

print(), len(), input(), float(), int()   <= existentes dentro do python.


Criação da função para exibir linha na tela

Ex: mostraLinha()

def mostrarLinha():
      print('----------------')


def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

* Funçãoes estão ligadas a palavra rotina.
'''

'''a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)'''


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa Principal
soma(34, 23)


'''def contador(*núm): <= Empacotamento'''
