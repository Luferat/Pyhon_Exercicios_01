"""
Exercício 1
Escreva um programa Python que peça ao usuário a sua idade e verifique se ele é elegível para votar. 
No Brasil, a idade mínima para votar é 16 anos. 
Salve como "exercicio1.py".
"""

# Receber a idade do usuário como inteiro em uma variável
var_idade = int(input('Digite sua idade: '))

# Testa se a idade é maior ou igual a 16 anos
if var_idade >= 16:
    # Se é maior ou igual (verdade → true)
    # Mostre a mensagem abaixo no terminal
    print('Oba! você já pode votar...')
else:
    # Se é menor (mentira → false)
    # Mostre a mensagem abaixo no terminal
    print('Oooops! Você ainda não pode votar...')

"""
Teste assim!
Versão super compacta.
"""
# if int(input("Digite sua idade: ")) >= 16: print("Oba! Você pode votar!")
# else: print("Opa! Você ainda não pode votar!")
