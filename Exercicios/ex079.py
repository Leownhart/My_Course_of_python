lista = []
while True:
    v = (int(input(f'Digite um valor: ')))
    if v in lista:
        print(f'Valor duplicado! Não vou adicionar... ')
    else:
        lista.append(v)
        print(f'Valor adicionado com sucesso... ')
    c = str(input(f'Deseja continuar? [S/N]: ')).upper()
    if c == 'N':
        break
print('-='*25)
print(f'Você digitou os valores {lista}')



