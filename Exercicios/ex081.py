lista = []
while True:
    number = int(input(f'Informe um valor: '))
    lista.append(number)
    opcao = str(input(f'Deseja continuar? [S/N] '))
    if opcao.upper() == 'N':
        break
print('-='*30)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 not in lista:
    print(f'O valor 5 não foi encontrado na lista')
else:
    print(f'O valor cinco consta na lista')