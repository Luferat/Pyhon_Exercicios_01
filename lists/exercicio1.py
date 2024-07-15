"""
Exercício 1: Criando e Acessando Elementos de uma Lista

 - Crie uma lista chamada `listFrutas` que armazene os nomes de 4 frutas diferentes.
 - Exiba na tela o nome da fruta que está na segunda posição da lista.
 - Adicione um novo item à lista, inserindo o nome de outra fruta no final.
 - Mostre na tela a quantidade de frutas na lista.
 - Remova a última fruta da lista.
"""

listFrutas = ["banana", "maçã", "laranja", "uva"]

print(listFrutas[1])  # Acessando o segundo elemento (maçã)

listFrutas.append("morango")  # Adicionando "morango" no final

print(len(listFrutas))  # Mostrando a quantidade de frutas (5)

listFrutas.remove("uva")  # Removendo a última fruta ("uva")

print(listFrutas)  # Exibe o resultado final
