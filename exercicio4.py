print('Lembre-se de usar "." em vez de "," para as casas decimais dos números!!!\n')

varNum1 = float(input("Primeiro número: "))
varNum2 = float(input("Segundo número: "))
varOperacao = input("Operação (+, -, *, /): ")

if varOperacao == '+':
    varResultado = varNum1 + varNum2
    print(f"A soma entre '{varNum1}' e '{varNum2}' é '{varResultado}'")
elif varOperacao == '-':
    varResultado = varNum1 - varNum2
    print(f"A subtração entre '{varNum1}' e '{varNum2}' é '{varResultado}'")
elif varOperacao == '*':
    varResultado = varNum1 * varNum2
    print(f"A multiplicação entre '{varNum1}' e '{varNum2}' é '{varResultado}'")
elif varOperacao == '/':
    if varNum2 != 0:
        varResultado = varNum1 / varNum2
        print(f"A divisão de '{varNum1}' por '{varNum2}' e '{varResultado}'")
    else:
        print("Erro! Tentativa de divisão por zero.")
else:
    print("Oooops! Operação inválida.")
