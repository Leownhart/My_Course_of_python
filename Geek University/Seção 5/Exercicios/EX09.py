'''
09 - Leia o sálario de um trabalhador e o valor da prestação de um empréstimo. Se a prestação
for maior que 20% do salário imprima: Emprestimo não concedido, caso contrário imprima: Emprestimo Concedido;
'''

sal = float(input('Sálario: '))
parc = float(input('Parcela: '))

porcent = sal * 20 / 100

print(f'20% do salário informado é R$ {porcent:.0f}')

if porcent == parc or porcent > parc:
    print('Emprestimo Concedido')
else:
    print('Emprestimo Negado')