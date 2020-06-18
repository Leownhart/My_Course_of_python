"""
Loop for
Loop -> Estrutura de repetição
For -> Uma dessas estruturas

C ou Java

for(int i = 0; i < limitador; i++)
{
    Execução do Loop
}

# Python

for item in interavel:
  //Execução do loop


Utilizamos loops par iterar sobre sequênciais ou sobra valores iteráveis

Exemplos de iteráveis:

- String
   nome = 'Geek University'
- Listas
    lista = [1, 2, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)
"""
nome = 'Geek University'
lista = [1, 2, 3, 4, 5]
numeros = range(1, 10) # Temos que transformar em uma lista

# Exemplo de for 1
for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

'''
range(valor_inicial, valor_final)
'''
# Exemplo de for 3 (Iterando sobre um range)
for numero in range(1, 10):
    print(numero)

# '_' descarta
for i, v in enumerate(nome):
    print(nome[i])

'''
Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode

# Original: U+1F60D
# Modificado: U0001F60D

for num in range(1, 11):
    print('/U0001F60D' * num)

Exemplo
nome = 'Geek'
nome + 'University'
'''


