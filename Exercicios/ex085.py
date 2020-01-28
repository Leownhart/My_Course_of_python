pares = []
impares = []
principal = []
for number in range(0, 7):
    number = int(input('Informe um valor: '))
    if number % 2 == 0:
        pares.append(number)
    else:
        impares.append(number)
principal.append(pares)
principal.append(impares)
principal[0].sort()
principal[1].sort()
print(f'Os valores pares digitados foram: {principal[0]}')
print(f'Os valores impares digitados foram: {principal[1]}')
