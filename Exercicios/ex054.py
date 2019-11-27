from datetime import  date
atual = date.today().year
tot = 0
totm = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        tot += 1
    else:
        totm += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(tot))
print('E também tivemos {} pessoas manores de idade'.format(totm))
