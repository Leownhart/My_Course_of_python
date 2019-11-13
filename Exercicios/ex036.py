valorcasa = float(input('Informe o valor da imovel: R$ '))
salcom = float(input('Informe o sálario do comprador: R$ '))
anos = int(input('Informe o tempo de financiamento em anos: '))
valpresta = (valorcasa / anos) / 12
porcent = salcom * 30.0 / 100
print('Para pagar uma casa de R${:.2f} em {} anos a '
      'prestação será de R${:.2f} mensais'.format(valorcasa, anos, valpresta))
if valpresta > porcent:
    print('\033[31mEmpréstimo NEGADO!\033[m')
else:
    print('\033[32mEmpréstimo APROVADO!\033[m')
