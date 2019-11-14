#  se a soma das medidas de dois deles é
#  sempre maior que a medida do terceiro,
#  então, eles podem formar um triângulo

print('\033[4;35m-=\033[m' * 20)
print('\033[32mAnalisador de Triângulos\033[m')
print('\033[4;36m-=\033[m' * 20)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[33mOs segmentos acima podem formar um triângulo!\033[m')
if r1 == r2 and r1 == r3:
    print('O triângulo é EQUILÁTERO')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('O triângulo é ISÓSCELES')
elif r1 != r2 and r1 != r3 and r2 != 3:
    print('O triângulo é ESCALENO')
else:
    print('\033[31mOs segmentos acima não podem formar um triângulo\033[m')






