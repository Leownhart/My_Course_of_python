totf = 0
maisv = 0
maior = 0
med = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).title().strip()
    idade = int(input('Idade: '))
    Sexo = str(input('[M/F]: ')).strip().title()
    med += idade
    if maior < idade:
        maior = idade
        maisv = nome
    if Sexo == 'F' and idade < 20:
        totf += 1
med = med / 4
print('A média de idade do grupo é de {} anos'.format(med))
print('O homen mais velho tem {} anos e se chama {}'.format(maior, maisv))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totf))
