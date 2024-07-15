"""
Exercício 6
Crie um programa que peça ao usuário três números (pode ser decimal ou inteiro) e calcule a média desses números.
O programa deve exibir a média com duas casas decimais.
Salve como "exercicio6.py"
"""

# Recebe do usuário um número e armazena
varNumero1 = float(input("Digite um número: "))

# Recebe do usuário um número e armazena
varNumero2 = float(input("Digite um número: "))

# Recebe do usuário um número e armazena
varNumero3 = float(input("Digite um número: "))

# Calcula a média entre os números
varMedia = (varNumero1 + varNumero2 + varNumero3) / 3

# Exibe o resultado com duas casas decimais
print(f'A média é {varMedia:.2f}.')
