'''
24 - Leia um valor de área em metros quadrados m² e apresente-o convertido em acres. A
fórmula de conversão é: A = M * 0.000247, sendo M a área em metros quadrados e A a área
em acres.
'''
q = int(input('Informe um valor de área em metros quadrados: '))
a = q * 0.000247
print(f'O valor da área em metros quadrados convertido em acres é {a:.9f}')
