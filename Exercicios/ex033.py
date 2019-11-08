a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceira valor: '))
# Verificar o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O menor valor digitado foi {}'.format(menor))
# Verificar o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior valor valor digitado foi {}'.format(maior))

# n1 = float(input('Primeiro valor: '))
# n2 = float(input('Segundo valor: '))
# n3 = float(input('Terceiro valor: '))
# if n1 > n2 and n1 > n3:
#    print('O maior valor digitado foi {:.0f}'.format(n1))
# if n2 > n1 and n2 > n3:
#    print('O maior valor digitado foi {:.0f}'.format(n2))
# if n3 > n1 and n3 > n2:
#    print('O maior valor digitado foi {:.0f}'.format(n3))
# if n1 < n2 and n1 < n3:
#    print('O menor valor digitado foi {:.0f}'.format(n1))
# if n2 < n1 and n2 < n3:
#    print('O menor valor digitado foi {:.0f}'.format(n2))
# if n3 > n1 and n3 > n2:
#     print('O menor valor digitado foi {:.0f}'.format(n3))


