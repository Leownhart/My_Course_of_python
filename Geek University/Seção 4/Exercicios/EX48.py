'''
 48 - Leia um valor inteiro e segundos, e imprima-o em horas, minutos e segundos.
'''

segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

segundos_rest = segundos % 86400
horas = segundos_rest // 3600
segundos_rest = segundos_rest % 3600
minutos = segundos_rest // 60
segundos_rest = segundos_rest % 60

print(f'{horas}, horas, {minutos}, minutos, {segundos_rest} segundos.')




