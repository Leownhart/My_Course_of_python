'''62 - Escreva  um programa que leia um número n inteiro
qualquer e mostre na tela os n primeiros elementos de uma sequência
de fionacci.

Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8.'''

print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} => '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))


