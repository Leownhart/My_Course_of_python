'''
50 - Implemente um programa que calcule o ano de nascimento de uma pessoa a parti de sua idade e do ano atual.
'''

# RESPOSTA

from datetime import datetime
nasc = int(input('Informe sua idade: '))
anosnasc = datetime.now().year - nasc
print(f'O ano de nascimento desta pessoa é {anosnasc}')
