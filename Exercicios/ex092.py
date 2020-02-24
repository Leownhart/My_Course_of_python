from datetime import datetime
cadastro = {'nome': str(input('Nome: ').capitalize()), 'idade': int(input('Ano de Nascimento: ')),
            'ctps': int(input('Carteira de Trabalho (0 não tem): '))}
if cadastro['ctps'] == 0:
    print('-=' * 30)
    cadastro['idade'] = datetime.now().year - cadastro['idade']
    for k, v in cadastro.items():
        print(f' - {k} tem o valor {v}')
else:
    cadastro['idade'] = datetime.now().year - cadastro['idade']
    cadastro['contratação'] = int(input('Ano de Contratação: '))
    cadastro['salário'] = int(input('Sálario: R$ '))
    cadastro['aposentadoria'] = cadastro['idade'] + (cadastro['contratação'] + 35) - datetime.now().year
    print('-=' * 30)
    for k, v in cadastro.items():
        print(f' - {k} tem o valor {v}')

''' Solução Altenativa

from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (o não tem): '))
if dados['ctps'] !==0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - datetime.now().year
print('-=' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')


'''
