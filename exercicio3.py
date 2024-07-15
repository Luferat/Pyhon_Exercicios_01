"""
Exercício 3
Desenvolva um programa python que converta a temperatura de Celsius para Fahrenheit.
O usuário deve fornecer a temperatura em Celsius e o programa deve calcular e exibir a temperatura em Fahrenheit.
A fórmula para conversão é `F = C * 9/5 + 32`. 
Salve como "exercicio3.py"
"""

# Receber a temperatura em celsius do usuário como decimal (float) em uma variável
print("Lembre-se de usar '.' no lugar da ','!")
var_celsius = float(input('Digite a temperatura em °C: '))

# Executa a fórmula e armazena em uma variável
var_fahrenheit = var_celsius * 9 / 5 + 32

# Exibe no terminal com duas casas decimais
print(f"{var_celsius:.2f}°C e o mesmo que {var_fahrenheit:.2f}°F")
