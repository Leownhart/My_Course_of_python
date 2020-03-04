'''
49 - Faça um programa que leia um horário (hora, minuto, segundo) de inicio e a duração, em
segundos, de uma experiência biológica. O  programa de resultar com o novo horário
(hora, minuto, segundo) do termino da  mesma.

from datetime import datetime
now = datetime.now()
print now.year
print now.month
print now.day
print now.hour
print now.minute
print now.second
'''

# RESPOSTAS

from datetime import datetime

Hora = int(input('Informe a Hora: '))
Minuto = int(input('Informe os Minutos: '))
Segundos = int(input('Informe os Segundos: '))

print(f'Passaram-se {Hora * 3600 + Minuto * 60 + Segundos} Segundos')
print(f'{datetime.now()}')
