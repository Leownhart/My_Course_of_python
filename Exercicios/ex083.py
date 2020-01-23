expr = str(input('Digite a expressão: '))  # Lendo a expressão
pilha = list()  # Declaração da lista
for símb in expr:  # Verificando se existe parêntese abrindo na leitura da expressão
    if símb == '(':  # Se o símbolo for igual a um parêntese abrindo.
        pilha.append('(')  # o elemendo será adicionado na pilha
    elif símb == ')':  # Se não se o elemento for um parêntese fechando.
        if len(pilha) > 0:  # verifica se o tamnaho da pilha e mais que zero.
            pilha.pop()  # retira um elemento do final da pilha
        else:  # se não
            pilha.append(')')  # adicionando um elemento ao final da lista
            break  # parando
if len(pilha) == 0: # ao final se o tamanho  da pilha for igual a 0.
    print('Sua expressão está válida')
else:  # se não
    print('Sua expressão está erra!')
