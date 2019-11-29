'''64 - Crie um programa que leia vários números inteiros pelo teclado.
no final da execução, mostre a média entre todos os valores e qual  foi o maior
e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar os valores.'''

perguntar = ''
cont = soma = maior = menor = 0
while perguntar != 'Não'.title():
    number = int(input('Informe um número: '))
    perguntar = input('Deseja continuar [Sim/Não]? ')
    soma += number
    cont += 1
    if number > maior:
        maior = number
    else:
        menor = number
média = soma / cont
print('Você digitou {} números, Média {:.1f},'
      ' Maior {}, Menor {}'.format(cont, média, maior, menor))


