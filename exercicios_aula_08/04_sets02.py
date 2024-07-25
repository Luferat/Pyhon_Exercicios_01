"""
Exercício 4: Combinando e Comparando Conjuntos
Crie um conjunto chamado numeros1 contendo os números pares de 1 a 10: {2, 4, 6, 8, 10}.
Crie um conjunto chamado numeros2 contendo os números ímpares de 1 a 9: {1, 3, 5, 7, 9}.
Exiba na tela a união dos conjuntos numeros1 e numeros2 (todos os números de 1 a 10, sem repetições).
Mostre na tela a intersecção dos conjuntos numeros1 e numeros2 (apenas os números pares ímpares: {2, 8}).
Exiba na tela a diferença do conjunto numeros1 em relação ao conjunto numeros2 (todos os números pares que não são ímpares: {4, 6, 10}).
Verifique se os conjuntos numeros1 e numeros2 são iguais.
Crie um conjunto chamado primos contendo os números primos menores que 10: {2, 3, 5, 7}.
Verifique se o conjunto primos é um subconjunto do conjunto numeros1 (todos os primos presentes nos pares de 1 a 10).
"""

# Crie um conjunto chamado numeros1 contendo os números pares de 1 a 10: {2, 4, 6, 8, 10}.
numeros1 = {2, 4, 6, 8, 10}

# Crie um conjunto chamado numeros2 contendo os números ímpares de 1 a 9: {1, 3, 5, 7, 9}.
numeros2 = {1, 3, 5, 7, 9}

# Exiba na tela a união dos conjuntos numeros1 e numeros2 (todos os números de 1 a 10, sem repetições) usando o método `set.union()`.
print("União dos conjuntos numeros1 e numeros2:", numeros1.union(numeros2))

# Mostre na tela a intersecção dos conjuntos numeros1 e numeros2 (apenas os números pares ímpares: {2, 8}) usando o método `set.intersection()`.
print("Intersecção dos conjuntos numeros1 e numeros2:", numeros1.intersection(numeros2))

# Exiba na tela a diferença do conjunto numeros1 em relação ao conjunto numeros2 (todos os números pares que não são ímpares: {4, 6, 10}) usando o método `set.difference()`.
print("Diferença do conjunto numeros1 em relação ao conjunto numeros2:", numeros1.difference(numeros2))

# Verifique se os conjuntos numeros1 e numeros2 são iguais usando comparação lógica `==`.
print("Os conjuntos numeros1 e numeros2 são iguais:", numeros1 == numeros2)

# Crie um conjunto chamado primos contendo os números primos menores que 10
primos = {2, 3, 5, 7}

# Verifique se o conjunto primos é um subconjunto do conjunto numeros1 (todos os primos presentes nos pares de 1 a 10) usando o método `set.issubset()`.
print("O conjunto primos é um subconjunto do conjunto numeros1:", primos.issubset(numeros1))
