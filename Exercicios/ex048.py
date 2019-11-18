# 48 - Faça um programa que cálcule a soma entre todos os números impares que
# são múltiplos de três e que se encontram no intervalo de 1 até 500.(Realizado)

soma = 0
cont = 0
for c in range(0, 501, 1):
    if c % 2 != 0 and c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))

# soma = 0
# cont = 0
# for c in range(1, 501, 2)
#    if c % 3 == 0:
#       print(c, end=' ')
# print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
