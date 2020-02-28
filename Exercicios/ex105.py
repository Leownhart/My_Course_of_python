'''
105 - Faça um programa que tenha uma função notas() que pode receber várias
notas de alunos e vai retornar um dicionário com seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação(Opcional)

Adicione também as docstrins da função.
'''


def notas(*resp, sit=False):
    geral = dict()
    geral['Total'] = len(resp)
    geral['Maior Nota'] = max(resp)
    geral['Menor Nota'] = min(resp)
    geral['Média'] = sum(resp)/len(resp)
    if sit:
        if geral['Média'] >= 7:
            geral['Situação'] = 'BOA'
        elif geral['Média'] >= 5:
            geral['Situação'] = 'Razóavel'
        else:
            geral['Situação'] = 'Ruim'
    return geral


# Programa Principal
resp = notas(5.5, 2.5, 10, 6.5, sit=False)
print(resp)
