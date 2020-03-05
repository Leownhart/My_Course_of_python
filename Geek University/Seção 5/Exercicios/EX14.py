'''
14 - A nota final de um estudante é calculado a parti de três notas atribuidas entre o intervalo
de 0 até 10. respectivamente, a um trabalho de laboratório, a uma avialiação semestral e a um exame
final. A média das três notas mencionadas anteriormente obedece aos pesos. Trbalho de Laboratório: 2;
Avaliação Semestral: 3; Exame Final: 5. De acordo com resultado, mostre na tela se o aluno está aprovado
(média entre 0 e 2,9) de recuperação (entre 3 e 4,9) ou se foi reprovado. Faça todas as verificações
necessárias.
'''


Labo = float(input('Trabalho de Laboratório: '))  # Peso 2
semes = float(input('Avaliação Semestral: '))  # Peso 3
final = float(input('Exame Final: '))  # Peso 5

med = ((2 * Labo) + (3 * semes) + (5 * final)) / 10

if med <= 5:
    print(f' Média {med:.2f}, Reprovado')
elif med <= 6:
    print(f' Média {med:.2f}, Recuperação')
elif med >= 7:
    print(f' Média {med:.2f},Aprovado')
