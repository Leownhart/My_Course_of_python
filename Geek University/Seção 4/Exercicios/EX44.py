'''
44 - Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir
seu objetivo.
'''

# RESPOSTA

cont = 0
altd = degrau = float(input('Informe a altura do degrau: '))
altura = float(input('Informe a altura que deseja alcançar: '))

while True:
    if degrau < altura:
        cont = cont + 1
        degrau = (degrau + altd)
    else:
        break
print(f'A quantidade de degraus necessários para subir a escada é {cont:.0f}')





