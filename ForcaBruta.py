from itertools import combinations
import pandas as pd
import time

alunos_habilidades = pd.read_csv("alunos_habilidades.csv")
Lista_alunos_habilidades = alunos_habilidades.to_dict(orient="records")



habilidades_prioridade_projeto = {
    3: ['DW', 'DM', 'DB'],  # Alta prioridade
    2: ['AS', 'TS'],  # Média prioridade
    1: ['DF']  # Baixa prioridade
}

pesos_prioridade = {
    3: 3,  # Alta prioridade tem peso 3
    2: 2,  # Média prioridade tem peso 2
    1: 1   # Baixa prioridade tem peso 1
}


tamanho_equipe_estudantes = 5
equipes_estudantes_habilidades = list(combinations(Lista_alunos_habilidades, tamanho_equipe_estudantes))
melhor_equipe_projeto = None
melhor_fitness = 0
total_combinacoes = 0

inicio = time.time()

for equipes_estudantes in equipes_estudantes_habilidades:
    total_combinacoes += 1
    fitness = 0
    habilidades_equipe_necessarias = set()

    for equipes_alunos in equipes_estudantes:
        #Iterando sobre as chaves do dicionário das habilidades por prioridades para os projetos de software.
        for habilidades_prioridades in habilidades_prioridade_projeto[3] + habilidades_prioridade_projeto[2] + habilidades_prioridade_projeto[1]:
            if equipes_alunos[habilidades_prioridades] > 0:
                habilidades_equipe_necessarias.add(habilidades_prioridades)

    for prioridade, habilidades_prioritarias in habilidades_prioridade_projeto.items():
        for habilidades_essenciais in habilidades_prioritarias:
            if habilidades_essenciais in habilidades_equipe_necessarias:
               fitness +=  pesos_prioridade[prioridade] 

    if fitness > melhor_fitness:
        melhor_fitness = fitness
        melhor_equipe_projeto = equipes_estudantes

fim = time.time()
tempo_total = fim - inicio
minutos = int(tempo_total // 60)
segundos = tempo_total % 60

horas = minutos / 60

# Resultados
print(f"Tempo total: {minutos}:{segundos:.1f}")
print(f"Melhor fitness: {melhor_fitness}")
print(f"total de combinações realizadas:{total_combinacoes}")
print("\nMelhor equipe:")

for equipe_alunos_habilidades in melhor_equipe_projeto:
    print(equipe_alunos_habilidades)