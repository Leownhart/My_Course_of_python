# Ocorrência de 'A'

frase = str(input('Digite uma frase: ')).strip()
a = frase.lower().count('a')
print('A letra A apareceu {} vezes na frase'.format(a))
b = frase.upper().find('A') + 1
print('A primeira letra A apareceu na posição {}'.format(b))
c = frase.upper().rfind('A') + 1
print('A última letra A apareceu na posição {}'.format(c))
