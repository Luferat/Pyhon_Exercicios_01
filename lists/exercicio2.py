"""
Exercício 2: Criando uma Lista a partir de um Range e Fatiamento

 - Crie uma lista chamada `listNumeros` utilizando a função `range()` para gerar uma sequência de números de 1 a 10 (inclusivo).
 - Exiba na tela os números pares da lista.
 - Crie uma nova lista chamada pares que contenha apenas os números pares da lista numeros.
 - Mostre na tela a lista pares.
 - Insira o número 15 na lista pares na terceira posição.
"""

listNumeros = list(range(1, 11))  # Criando lista de 1 a 10 com range()

for varNumero in listNumeros:
    if varNumero % 2 == 0:
        print(varNumero)  # Exibindo números pares

pares = listNumeros[1::2]  # Fatiando para obter pares (começa no segundo índice, pula de 2 em 2)

print(pares) # Mostrando a lista de pares

pares[2] = 15  # Inserindo 15 na terceira posição
