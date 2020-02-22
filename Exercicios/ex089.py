ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')

'''pessoas = list()   <___Possivel Alternativa__>
aluno = list()
cont = 0
while True:
    nome = str(input('Nome: ')).title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    pessoas.append(aluno[:])
    aluno.clear()
    cont += 1
    opt = str(input('Quer continuar? [S/N] ')).upper().strip()
    if opt == 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*25)
for n in range(0, cont):
    print(f'{n:<3} {pessoas[n][0]:9} {(pessoas[n][1] + pessoas[n][2]) / 2:>8.1f}')
print('-'*25)
while True:
    opt2 = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    print(f'Notas de {pessoas[opt2][0]} são {pessoas[opt2][1], pessoas[opt2][2]}')
    if opt2 == 999:
        print('FINALIZANDO...')
        break
print('<---VOLTE SEMPRE--->')'''
