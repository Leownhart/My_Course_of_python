pessoas = list()
aluno = list()
cont = 0
while True:
    nome = str(input('Nome: '))
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
print('No. NOME     MÉDIA')
for n in range(0, cont):
    print(f'{n} {pessoas[n][0]} {(pessoas[n][1] + pessoas[n][2]) / 2:.2f}')
