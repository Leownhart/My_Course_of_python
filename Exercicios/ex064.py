'''64 - Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar  quando o usáuario digitar o valor 999, que é a
condição da parada. no final, mostre quantos números foram
digitados e qual foi  a soma entre eles (descondirando o flag).'''

n = 0
cont = 0
soma = 0

while n != 999:
    n = int(input('Informe um número: '))
    if n != 999:
        cont += 1
        soma += n
print('Numeros digitados {}, Soma en'
      'tre os números digitados {}.'.format(cont, soma))
