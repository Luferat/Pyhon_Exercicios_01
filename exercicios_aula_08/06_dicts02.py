"""
Exercício 6: Trabalhando com Dicionários Aninhados e Funções
Crie uma função chamada calcula_media() que recebe um dicionário de notas como argumento e retorna a média das notas.
Crie um dicionário chamado alunos que armazene as notas de 3 alunos em 3 disciplinas: matemática, português e história.
Utilize dicionários aninhados para armazenar as notas de cada aluno em cada disciplina.
Utilize a função calcula_media() para calcular a média das notas de cada aluno em todas as disciplinas.
Exiba na tela o nome de cada aluno e sua média final.
"""

# Crie uma função chamada calcula_media() que recebe um dicionário de notas como argumento e retorna a média das notas.
def calcula_media(notas):
    total = sum(notas.values())
    quantidade = len(notas)
    media = total / quantidade
    return media

# Crie um dicionário chamado alunos que armazene as notas de 3 alunos em 3 disciplinas: matemática, português e história.
# Utilize dicionários aninhados para armazenar as notas de cada aluno em cada disciplina.
alunos = {
    "Joca": {
        "matematica": 85,
        "portugues": 78, 
        "historia": 92
    },
    "Setembrino": {
        "matematica": 90, 
        "portugues": 88, 
        "historia": 80
    },
    "Hermenilda": {
        "matematica": 70, 
        "portugues": 75, 
        "historia": 85
    }
}

# Utilize a função calcula_media() para calcular a média das notas de cada aluno em todas as disciplinas.
for aluno, notas in alunos.items():
    media = calcula_media(notas)
    
    # Exiba na tela o nome de cada aluno e sua média final.
    print(f" • {aluno} → {media:.2f}")
