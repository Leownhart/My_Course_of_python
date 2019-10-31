#(54 °C × 9 / 5) + 32 = 129, 2 °F
Celsius = float(input('Informe a temperatura em ºC: '))
fahrenheit = (Celsius * 9 / 5) + 32
print('A temperatura em Fahrenheit e {:.1f}F'.format(fahrenheit))

# (32 °F − 32) × 5/9 = 0 °C
fahrenheit = float(input('Informe a temperatura em ºF: '))
Celsius = (fahrenheit - 32) * 5 / 9
print('A temperatura em Fahrenheit e {:.1f}ºC'.format(Celsius))