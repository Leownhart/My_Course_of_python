aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

print('-='*26)

if aluno['média'] < 5:
    aluno['situação'] = 'Reprovado'
elif aluno['média'] < 6:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'

print(f'- nome é igual a {aluno["nome"]}')
print(f'- média é igual a {aluno["média"]}')
print(f'- situação é igual a {aluno["situação"]}')
