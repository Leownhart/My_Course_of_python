n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
med = (n1 + n2) / 2
if med < 5.0:
    print('Aluno está \033[1:31mREROVADO!\033[m, A Média e {}'.format(med))
elif 5.0 <= med <= 6.9:
    print('Aluno está em \033[1:33mRECUPERAÇÃO!\033[m A Média e {}'.format(med))
else:
    print('Aluno \033[1:36mAPROVADO!\033[m A Média e {}'.format(med))
