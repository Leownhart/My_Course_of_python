numberlist = []
mai = 0
men = 0
for n in range(0, 5):
    numberlist.append(int(input(f'Digite um valor para a Posição {n}: ')))
    if n == 0:
        mai = men = numberlist[n]
    else:
        if numberlist[n] > mai:
            mai = numberlist[n]
        if numberlist[n] < men:
            men = numberlist[n]
print(f'Você digitou os valores {numberlist}')
print('-='*25)
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(numberlist):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(numberlist):
    if v == men:
        print(f'{i}... ', end='')
print()












