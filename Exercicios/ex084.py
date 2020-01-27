pes = []
mail = []
menl = []
cont = mai = men = 0
while True:
    nome = str(input('Nome: ')).strip()
    peso = float(input('Peso: '))
    pes.append(nome)
    pes.append(peso)
    option = str(input('Quer continuar? ')).strip().upper()
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
print(f'O menor peso foi de {men}Kg. Peso de {menl}')



