aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

print('-='*26)

if aluno['média'] < 5:
    aluno['situação'] = 'Reprovado'
elif aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'

for k, v in aluno.items():
    print(f' - {k} é igual a {v}')

print(aluno)
