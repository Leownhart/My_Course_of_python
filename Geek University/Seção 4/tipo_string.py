"""
Tipo String

Em Python, um dado considerado um tipo string sempre que:

- Estiver entre qualquer tipo de áspas -> 'um strig', '334', 'True', '4.2'

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angeline \n Jolie'
print(nome)
print(type(nome))
"""

nome = 'Angeline Jolie'
print(nome)
print(type(nome))
print(nome.upper())


n = 'Geek University'
print(f'{n.split()}')
print(f'{n.split()[0]}')
print(f'{n.split()[1]}')

"""
 Comece do primeiro elemento, vá até o último elemento e inverta
"""
print(nome[::-1]) ##  Inversão da String Pythônico

print(nome.replace('G', 'P')) ## Realizar substuição do elemento.
