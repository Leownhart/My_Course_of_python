cont = soma = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Quantidade de números digitados [{cont}]!.')
print(f'Soma total dos números digitados [{soma}]!.')
