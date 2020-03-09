'''
22 - Leia a idade e o tempo de serviço de um trabalhador e
escreva se ele pode ou não se aposentar.
As condições para aponsentadoria são

* Ter pelo menos 65 anos,
* Ou ter trabalhado pelo menos 30 anos,
* Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
'''

idade  = int(input('Informe a Idade: '))
temc = int(input('Informe o tempo de contribuição: '))

if idade > 65:
    print('Aposentadoria Concedida.')
elif temc >= 30:
    print('Aposentadoria Concedida.')
elif idade >= 60 and temc >= temc:
    print('Aponsentadoria Concedida.')
else:
    print('Aposentadoria Negada.')

