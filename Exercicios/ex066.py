cont = soma = n = 0
while n != 999:
    n = int(input('Digite um número (999 para parar): '))
    if n != 999:
        cont += 1
        soma += n
    if n == 999:
        break
print(f'Quantidade de números digitados {cont}!.')
print(f'Soma total dos números digitados {soma}!.')
