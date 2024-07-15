"""
Exercício 2
Crie um programa Python que peça ao usuário um número inteiro e determine se ele é par ou ímpar.
Salve como "exercicio2.py"
"""

# Recebe o número do usuário, converte para inteiro e armazena na variável
var_numero = int(input("Digite um número inteiro: "))

# Testa se o número é par obtendo o resto da divisão (modulus) por 2
if var_numero % 2 == 0:
    # Se o resto é 0, o número é par, então exibe a mensagem abaixo
    print(f"{var_numero} é par!")
else:
    # Senão, o resto não é 0, o número não é par, então exibe a mensagem abaixo
    print(f'{var_numero} é ímpar!')

"""
Teste a versão compacta!
""""

# if int(input("Digite um número inteiro: ")) % 2 == 0: print(f"É par.")
# else: print(f"É ímpar.")
