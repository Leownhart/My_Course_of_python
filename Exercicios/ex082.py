a = []
b = []
c = []
while True:
    elemento = int(input(f'Informe um valor: '))
    a.append(elemento)
    opcao = str(input(f'Deseja continuar? [S/N] '))
    if opcao.upper() == 'N':
        break
for n in range(0, len(a)):
    if a[n] % 2 == 0:
        b.append(a[n])
    else:
        c.append(a[n])
print('-='*30)
print(f'A lista completa é {a}')
print(f'A lista de pares é {b}')
print(f'A lista de impares é {c}')


