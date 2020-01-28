temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Ao todo, voçê cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()

'''(Solução Incorreta)'''

'''pes = []  
mail = []
menl = []
cont = mai = men = 0
while True:
    nome = str(input('Nome: ')).strip()
    peso = float(input('Peso: '))
    pes.append(nome)
    pes.append(peso)
    option = str(input('Quer continuar [S/N]? ')).strip().upper()
    if option == 'N':
        break
for i, v in enumerate(pes):
    if i % 2 == 0:
        cont += 1
    else:
        men = v
        if v > mai:
            mai = v
        elif v < men:
            men = v
for i, v in enumerate(pes):
    if v == mai:
        mail.append(pes[i-1])
    elif v == men:
        menl.append(pes[i-1])
print('-=' * 30)
print(f'Ao todo, você cadastrou {cont} pessoas')
print(f'O maior peso foi de {mai}Kg. Peso de {mail}')
print(f'O menor peso foi de {men}Kg. Peso de {menl}')'''




