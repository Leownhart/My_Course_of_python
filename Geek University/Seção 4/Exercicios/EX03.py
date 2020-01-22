'''
3 - Peça ao usuário para digitar três valores inteiros e imprima a soma deles
'''

# RESPOSTA

soma = 0
for n in range(0, 3):
    number = int(input('Informe um valor: '))
    soma = soma + number
print(f'A soma do valores é {soma}')