"""
Exercício 4
Escreva um programa que funcione como uma calculadora básica. 
Ele deve pedir ao usuário dois números e uma operação ( + ,  - ,  * ,  / ).
Com base na operação escolhida, o programa deve executar a operação e exibir o resultado.
Salve como "exercicio4.py"
"""

# Pede atenção ao formato dos números
print('Lembre-se de usar "." em vez de "," para as casas decimais dos números!!!\n')

# Recebe o primeiro valor, converte para inteiro e armazena na variável
varNumero1 = int(input('Digite o primeiro número: '))

# Recebe a operação como uma string e armazena na variável
varOperador = str(input("Digite o operador (+, -, *, ou /): "))

# Recebe o segundo valor, converte para inteiro e armazena na variável
varNumero2 = int(input('Digite o segundo número: '))

# Testa o operador '+'
if varOperador == '+':
    # Se for '+' realiza a soma e exibe
    print(f'A soma entre {varNumero1} e {varNumero2} é {varNumero1 + varNumero2}!')

# Testar o operador '-'
elif varOperador == '-':
    # Se for '-' realiza a subtração e exibe
    print(f'A subtração entre {varNumero1} e {varNumero2} é {varNumero1 - varNumero2}!')

# Testar o operador '*'
elif varOperador == '*':
    # Se for '*' realiza a multiplicação e exibe
    print(f'A multiplicação entre {varNumero1} e {varNumero2} é {varNumero1 * varNumero2}!')

# Testar o operador '/'
elif varOperador == '/':
    # Testa se o divisor (varNumero2) não é zero
    if varNumero2 != 0:
        # Se é diferente de 0, realiza a divisão e exibe com duas casas decimais
        print(f'A divisão entre {varNumero1} e {varNumero2} é {varNumero1 / varNumero2:.2f}!')
    else:
        # Se digitou zero, exibe mensagem de erro
        print('Oooops! Você está tentando dividir por ZERO.')    

# Se a operação digitada não é suportada
else:
    # Exibe a operação como inválida!
    print('Oooops! Não entendi o que você quer calcular!')    
