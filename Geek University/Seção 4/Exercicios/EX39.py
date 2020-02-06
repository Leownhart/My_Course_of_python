'''
39 - A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso.
Sendo que da quantia total.

 * O primeiro ganhador receberá 46%;
 * O segundo receberá 32%;
 * O terceiro receberá o restante;

 Calcule e imprima a quantia ganha por cada um  dos ganhadores.
'''

# RESPOSTA

premiação = 780.00000
primeiro = (46 / 100) * premiação
segundo = (32 / 100) * premiação
terceiro = (22 / 100) * premiação
print(f'Primeiro {primeiro:.5f} \nSegundo {segundo:.5f}'
      f' \nTerceiro {terceiro:.5f}\n')
total = primeiro + segundo + terceiro
print(f'Total da premiação {total:.5f}')

