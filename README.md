```
Programador Python
Lógica e Algoritmos
```

# Python - Exercicios 01

Pacote 1 de exercícios de lógica e algoritmos com Python.

## Dicas

Use a função `input()` para receber dados do teclado pelo terminal. Exemplo:

`ex1input.py`
```python
print('Digite seu nome e tecle [Enter]: ')
varNome = input()
print('Olá, ' + varNome)
```

A função `input()` aceita uma string como parâmetro. Exemplo:

`ex2input.py`
```python
varNome = input("Digite seu nome e tecle [Enter]: ")
print("Seu nome é", varNome)
```
 - Referências: [Python input() Function (w3schools.com)](https://www.w3schools.com/python/ref_func_input.asp)

### Mais referências

 - [Python Variables (w3schools.com)](https://www.w3schools.com/python/python_variables.asp)
 - [Python Conditions (w3schools.com)](https://www.w3schools.com/python/python_conditions.asp)
 - [Python Operators (w3schools.com)](https://www.w3schools.com/python/python_operators.asp)
 - [Python print() Function (w3schools.com)](https://www.w3schools.com/python/ref_func_print.asp)
 - [Python Strings (w3schools.com)](https://www.w3schools.com/python/python_strings.asp)
 - [Python String Formatting (w3schools.com)](https://www.w3schools.com/python/python_string_formatting.asp)
 - [Python Numbers (w3schools.com)](https://www.w3schools.com/python/python_numbers.asp)

---
### Exercício 1: Verificação de Idade para Votação
Dica:
 - *funções `int()` e `input()`*
 - *instrução `if…else`*
 - *operador lógico `>=`*

Escreva um programa Python que peça ao usuário a sua idade e verifique se ele é elegível para votar. No Brasil, a idade mínima para votar é 16 anos. Salve como `exercicio1.py`.

---
### Exercício 2: Par ou Ímpar
Dica: 
 - *operador aritmético `%` (módulo)*
 - *operador lógico `==`*
 - *interpolação `f'{var}'`*

Crie um programa Python que peça ao usuário um número inteiro e determine se ele é par ou ímpar. Salve como `exercicio2.py`.

---
### Exercício 3: Conversão de Temperatura
Dica:
 - *função `float()`*
 - *formatação de floats `f'{var:.#f}'`*

Desenvolva um programa python que converta a temperatura de Celsius para Fahrenheit. O usuário deve fornecer a temperatura em Celsius e o programa deve calcular e exibir a temperatura em Fahrenheit. A fórmula para conversão é  F = C * 9/5 + 32.  Salve como `exercicio3.py`.

---
### Exercício 4 - DESAFIO: Calculadora Básica
Dica:
 - *operadores aritméticos `+`, `-`, `*` e `/`
 - *operador lógico `==`
 - instrução `if…elif…else` 

Escreva um programa que funcione como uma calculadora básica. Ele deve pedir ao usuário dois números e uma operação ( + ,  - ,  * ,  / ). Com base na operação escolhida, o programa deve executar a operação e exibir o resultado. Salve como `exercicio4.py`.

---
### Exercício 5: Conversão de Tipos
Dica: 
 - *funções `int()`, `float()` e `str()`*

Escreva um programa que peça ao usuário três informações: um número inteiro, um número decimal e uma palavra. O programa deve converter essas entradas para os tipos corretos e exibir as informações formatadas em uma frase.  Salve como `exercicio5.py`.

---
### Exercício 6: Calculadora de Média
Dica:
 - *funções `int()`, `float()` e `str()`*
 - *formatação de floats `f'{var:.#f}'`*
 - *operador aritmético `+`*

Crie um programa que peça ao usuário três números (pode ser decimal ou inteiro) e calcule a média desses números. O programa deve exibir a média com duas casas decimais. Salve como `exercicio6.py`.
