"""
Escopo de variáveis

/    Escopo    /

Dois casos de escopo:

1 - Variáveis globais:
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa

2 - Vriáveis locais:
    - Variáveis locais são reconheceidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco  onde foi declarada.

Para declarar variáveis em Python fazemos:

nome_da_variável = valor_da_variavel

Python é uma linguagem de tipagem dinãmica. Isso significa que ao
declararmos uma variável, nós não colocamos o tipo de dado dela.
Esse tipo é inferido ao atribuirmos o valor á mesma.

Exemplo em C:
int numero - 42;

Exemplo em Java:
int numero = 42;
"""
numero = 42
print(numero)
print(type(numero))