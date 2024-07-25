"""
Exercício 2: Combinando Tuplas e Verificando Elementos
Crie duas tuplas: frutas contendo ("banana", "maçã", "laranja") e legumes contendo ("tomate", "cenoura", "batata").
Crie uma nova tupla chamada mercado que combine as tuplas frutas e legumes.
Verifique se a fruta "laranja" está presente na tupla mercado.
Verifique se o legume "alface" está presente na tupla mercado.
Exiba na tela o último item da tupla mercado.
"""

# Crie duas tuplas: frutas contendo ("banana", "maçã", "laranja") e legumes contendo ("tomate", "cenoura", "batata").
frutas = ("banana", "maçã", "laranja") 
legumes = ("tomate", "cenoura", "batata")

# Crie uma nova tupla chamada mercado que combine as tuplas frutas e legumes usando `+`.
mercado = frutas + legumes

# Verifique se a fruta "laranja" está presente na tupla mercado usando as estruturas `if` e `ìn`.
if "laranja" in mercado:
    print("Sim, 'laranja' está na lista de compras.")
else:
    print("'laranja' não está na lista de compras.")

# Verifique se o legume "alface" está presente na tupla mercado usando as estruturas `if` e `ìn`.
if "alface" in mercado:
    print("Sim, 'alface' está na lista de compras.")
else:
    print("'Alface' não está na lista de compras.")

# Exiba na tela o último item da tupla mercado usando posicionamento relativo (`[-1]`).
print(f"O último item da lista de compras é: {mercado[-1]}")