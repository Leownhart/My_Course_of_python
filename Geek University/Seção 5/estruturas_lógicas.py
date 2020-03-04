'''
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not
Operadores binários:
    - and, or, is

Regras de Funcionamento:
Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, o perador nega o estado atual da váriavel.
Para o 'is', o valor é comparado com um segundo.
'''

# Ex:
ativo = True
logado = False

if ativo:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

# Ativo é True?
print(ativo is True)
