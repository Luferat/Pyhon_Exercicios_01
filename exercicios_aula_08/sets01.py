"""
Exercício 3: Criando e Manipulando Conjuntos
Crie um conjunto chamado letras contendo as vogais do alfabeto: "a", "e", "i", "o", "u".
Exiba na tela o tamanho do conjunto letras.
Adicione a consoante "b" ao conjunto letras.
Verifique se a vogal "i" está presente no conjunto letras.
Remova a consoante "b" do conjunto letras.
Crie um novo conjunto chamado consoantes contendo as consoantes: "b", "d", "f".
Verifique se o conjunto consoantes está contido no conjunto letras.
Exiba na tela a união dos conjuntos letras e consoantes (todos os elementos sem repetições).
"""

# Crie um conjunto chamado letras contendo as vogais do alfabeto
letras = {"a", "e", "i", "o", "u"}

# Exiba na tela o tamanho do conjunto letras usando a função `len()`
print("Tamanho do conjunto letras:", len(letras))

# Adicione a consoante "b" ao conjunto letras usando o método `set.add()`
letras.add("b")

# Verifique se a vogal "i" está presente no conjunto letras usando a estrutura `in`
print("A vogal 'i' está presente no conjunto letras:", "i" in letras)

# Remova a consoante "b" do conjunto letras usando o método `set.remove()`
letras.remove("b")

# Crie um novo conjunto chamado consoantes contendo as consoantes: "b", "d", "f"
consoantes = {"b", "d", "f"}

# Verifique se o conjunto consoantes está contido no conjunto letras usando o método `set.issubset()`
print("O conjunto consoantes está contido no conjunto letras:", consoantes.issubset(letras))

# Exiba na tela a união dos conjuntos letras e consoantes (todos os elementos sem repetições), usando o método `set.union()`
uniao = letras.union(consoantes)
print("União dos conjuntos letras e consoantes:", uniao)
