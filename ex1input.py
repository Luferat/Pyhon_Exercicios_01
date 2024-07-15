"""
Exemplo simples do uso de `input()` para receber dados do terminal.

Lembre-se!
 	┌─ Terminal ou console → Dispositivo de interface padrão do Python
  ├──── Dispositivo de entrada padrão → Teclado → Função `input()`
  └──── Dispositivo de saída padrão → Monitor → Função `print()`
"""

# Solicita a informação no terminal usando a saída padrão.
print('Digite seu nome e tecle [Enter]: ')

# Recebe os dados do terminal usando a entrada padrão e armazena na variável.
varNome = input()

# Exibe o resultado na saída padrão usando concatenação → +.
print('Olá, ' + varNome)
