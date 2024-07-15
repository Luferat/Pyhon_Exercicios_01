"""
Exercício 5
Escreva um programa que peça ao usuário três informações:
 - um número inteiro
 - um número decimal
 - uma palavra
O programa deve converter essas entradas para os tipos corretos e exibir as informações formatadas em uma frase.
Salve como "exercicio5.py"
"""

# Solicita ao usuário um número inteiro e armazena em uma variável
varInteiro = int(input("Digite um número inteiro: "))

# Solicita ao usuário um número decimal e armazena em uma variável
varDecimal = float(input("Digite um número decimal usando '.': "))

# Solicita ao usuário uma palavra e armazena em uma variável
varPalavra = str(input("Digite uma palavra: "))

# Exibe as informações digitadas formatadas
print(f'Você digitou o inteiro "{varInteiro}", o decimal "{varDecimal}" e a palavra "{varPalavra}".')
