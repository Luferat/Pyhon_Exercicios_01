"""
Exercício 5: Criando e Acessando Elementos de um Dicionário
Crie um dicionário chamado agenda para armazenar informações de contato de seus amigos:
    Chave: nome do amigo (string)
    Valor: dicionário com informações de contato (telefone, email)
Adicione 3 amigos à sua agenda, cada um com nome, telefone e email.
Exiba na tela o telefone do primeiro amigo da agenda.
Modifique o email do segundo amigo para um novo endereço.
Adicione uma nova chave "cidade" ao dicionário de informações do terceiro amigo, com o valor correspondente à sua cidade natal.
Exiba na tela todas as chaves e valores do dicionário do terceiro amigo.
"""

# Crie um dicionário chamado agenda para armazenar informações de contato de seus amigos
agenda = {}

# Adicione 3 amigos à sua agenda, cada um com nome, telefone e email
#   Chave: nome do amigo (string)
#   Valor: dicionário com informações de contato (telefone, email)
agenda["Joca"] = {
    "telefone": "1234-5678",
    "email": "joca@email.com"
}
agenda["Setembrino"] = {
    "telefone": "2345-6789", 
    "email": "set@email.com"
}
agenda["Hermenilda"] = {
    "telefone": "3456-7890", 
    "email": "herme@email.com"
}

# Exiba na tela o telefone do primeiro amigo da agenda.
primeiro_amigo = list(agenda.keys())[0] # Obtém os nomes do amigos, extraindo as chaves usando o método `dict.keys()` para uma lista e exibindo o item [0] da lista para o primeiro amigo.
print(f"Telefone do primeiro amigo ({primeiro_amigo}):", agenda[primeiro_amigo]["telefone"])

# Modifique o email do segundo amigo para um novo endereço
agenda["Setembrino"]["email"] = "setembrino@email.com"

# Adicione uma nova chave "cidade" ao dicionário de informações do terceiro amigo, com o valor correspondente à sua cidade natal
agenda["Hermenilda"]["cidade"] = "Curva do Vento"

# Exiba na tela todas as chaves e valores do dicionário do terceiro amigo
print("Informações do terceiro amigo:")
for chave, valor in agenda["Hermenilda"].items():
    print(f"{chave}: {valor}")

# Dica: imprimindo do dicionário completo e formatado usando a biblioteca `pprint`.
import pprint
pprint.pprint(agenda)

# Dica: imprimindo do dicionário completo e formatado usando a biblioteca `json`.
import json
print(json.dumps(agenda, indent=4, ensure_ascii=False))