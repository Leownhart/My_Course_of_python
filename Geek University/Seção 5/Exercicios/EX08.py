'''
08 - Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba
na tela a méadia destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0,
onde caso a nota não possua um valor válido, este fato deve ser informado ao usuário e o programa termina.
'''

med = 0
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

if  nota1 == 0.0 or nota1 > 10.0:
    print('Nota 1, Inválida.')
elif nota2 == 0.0 or nota2 > 10.0:
    print('Nota 2, Inválida.')
else:
    med = (nota1 + nota2) / 2
print(f'A média do aluno é {med:.2f}')