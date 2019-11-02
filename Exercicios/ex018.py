from math import sin, cos, tan, radians
ang = float(input('Informe o ângulo desejado: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O ângulo de {:.1f} tem o SENO de {:.2f}'.format(ang, sen))
print('O ângulo de {:.1f} tem o COSSENO de {:.2f}'.format(ang, cos))
print('O ângulo de {:.1f} tem o TANGENTE de {:.2f}'.format(ang, tan))





