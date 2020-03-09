'''
23 - Determine se um ano lido é bissexto. Sendo que ano é bissexto se for divisivel por 400
ou se for divisivel por 4 e não for divisivel por 100. Por xemplo: 1988, 1992, 1996
'''

year = int(input('Year: '))
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print('O ano é Bissexto')
else:
    print('O ano não é Bissexto')
