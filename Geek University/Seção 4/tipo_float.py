"""
Tipo Float -> Váriaveis com ponto flutuante

"""
# Errado
valor = 1, 44
print(valor)

# Certo so ponto de viata float
valor = 1.44
print(valor)
print(type(valor))

# É possivel realizar dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(valor2)
print(type(valor1))
print(type(valor2))

# Podemos converter um float para um int
res = int(valor)
print(res)
print(type(res))

