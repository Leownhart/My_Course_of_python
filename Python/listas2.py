'''
Lista Composta

teste = ['Gustavo', 40]
galera = [teste[:]]
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['João', 34], ['Mariazinha', 23], ['Ana', 23], ['Joaquim', 13]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
'''

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')




