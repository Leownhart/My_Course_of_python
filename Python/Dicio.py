estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')




'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])'''


'''pessoas = {'nome': 'Gustavo', 'Sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

del pessoas['Sexo']
pessoas['nome'] = 'Leandro'

for k in pessoas.keys():
    print(k)

for k in pessoas.values():
    print(k)'''

'''for k, v in pessoas.items():
    print(f'{k} = {v}')
    
    
                               <---DICIONÁRIO--->

dados = dict()
dados = {'nome:'Pedro', 'idade:25'}

Adicionando Elemento:

dados['sexo']='M'
filme {'titulo':'Star Wars', 'ano':1977, 'diretor':'George Lucas'}

Remover Elemento:

del dados['idade']

Mostrar seguementos:

print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(f'0{k} é {v}') 
    '''
