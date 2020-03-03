'''
114 - Crie um código em python que teste se o site Pudim
está acessivel pelo computador usado.
'''

import urllib
import urllib.request

try: 
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim  não está acessivel no momento.')
else:
    print('Tudo Ok')