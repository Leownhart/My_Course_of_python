'''
47 - Leia um número inteiro de 4 digitos (de 1000 a 9999) e imprima 1 digito por linha.
'''

# RESPOSTA

núm = str(input('Informe um número de quatro digitos: '))
núm.strip()
print(f'{núm[0]}')
print(f'{núm[1]}')
print(f'{núm[2]}')
print(f'{núm[3]}')


