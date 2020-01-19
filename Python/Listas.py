# lista =[], criando uma lista
# .append(''), adiciona um elemento no final da lista
# .insert(0,'elemento'), adiciona um elemento em lugar dsignado.
# .pop(3), elemina um elemento.
# .remove('elemento'), remove pela posição.
# valores.sort(), Ordena
# valores.sort(reverse=true), Ordena de modo reverso.
# valores = list(range(4,11)), declaração de lista utilizando range
# b = a[:] = cópia a lista.

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')
print(valores)
