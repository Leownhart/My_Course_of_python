'''
46 - Faça um programa que leia um número inteiro positivo de três digitos (100 a 999).
Gere outro número pelos digitos invertidos do número lido. Exemplo:

 NúmeroLido = 123
 NúmeroGerado = 321.
'''

# RESPOSTA
'''
Utilizei uma string em vez de um número inteiro.

'''
num = str(input('NúmeroLido = '))
print(f'NúmeroGerado = {num[::-1]}')
