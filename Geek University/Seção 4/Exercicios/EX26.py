'''
26 - Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares.
A fómula de conversão é H = M * 0.0001, sendo M a área em metros quadrados e H a área em
hectares.
'''

metros = int(input('Informe um valor em metros quadrados: '))
h = metros * 0.0001
print(f'O valor informado convertido em hectares é {h:.2f}')
