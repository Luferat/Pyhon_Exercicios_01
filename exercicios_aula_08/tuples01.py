"""
Exercício 1: Criando e Acessando Elementos de uma Tupla
Crie uma tupla chamada minha_tupla que armazene as cores do arco-íris: "vermelho", "laranja", "amarelo", "verde", "azul", "anil" e "violeta".
Exiba na tela a cor que está na quarta posição da tupla.
Tente modificar o valor da cor na quinta posição da tupla. (Isso deve gerar um erro, pois tuplas são imutáveis).
Crie uma nova tupla chamada cores_invertidas que seja a reversa da minha_tupla.
Mostre na tela a cores_invertidas.
"""
 
# Crie uma tupla chamada minha_tupla que armazene as cores do arco-íris: "vermelho", "laranja", "amarelo", "verde", "azul", "anil" e "violeta". 
minha_tupla = ("vermelho", "laranja", "amarelo", "verde", "azul", "anil", "violeta")

# Exiba na tela a cor que está na quarta posição da tupla.
print(minha_tupla[3])

# Tente modificar o valor da cor na quinta posição da tupla. (Isso deve gerar um erro, pois tuplas são imutáveis).
# minha_tupla[4] = "roxo"

# Crie uma nova tupla chamada cores_invertidas que seja a reversa da minha_tupla usando fatiamento.
cores_invertidas = minha_tupla[::-1]

# Mostre na tela a cores_invertidas.
print(cores_invertidas)
