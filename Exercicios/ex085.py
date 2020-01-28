núm = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}ª valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-='*30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores pares digitados foram: {núm[1]}')

"""Solução Válida"""

'''pares = []
impares = []
principal = []
for number in range(0, 8):
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
print(f'Os valores impares digitados foram: {principal[1]}')'''
