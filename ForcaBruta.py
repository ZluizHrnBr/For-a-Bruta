import pandas as pd
import time



# Definir parâmetros


alunos = pd.read_csv('matriz_habilidades.csv')
alunos_dict = alunos.to_dict(orient='records')
tamanho_equipe = 5
def combinar(lista, k):
  
    if k == 0:
        return [[]]
    if not lista:
        return []
    return combinar(lista[1:], k) + [[lista[0]] + resto for resto in combinar(lista[1:], k - 1)]

# Gerar todas as combinações de equipes
inicio = time.time()

melhor_equipe = None
melhor_fitness = 0
total_combinacoes = 0

habilidades_prioridade = {
    3: ['DW', 'DM', 'DB'],  # Alta prioridade
    2: ['AS', 'TS'],  # Média prioridade
    1: ['DF']  # Baixa prioridade
}

pesos_prioridade = {
    3: 3,  # Alta prioridade tem peso 3
    2: 2,  # Média prioridade tem peso 2
    1: 1   # Baixa prioridade tem peso 1
}

combinacoes = combinar(alunos_dict, tamanho_equipe)

for equipe in combinacoes:
    total_combinacoes += 1
    fitness = 0
    habilidades = set()
    

    for aluno in equipe:
        for habilidade in habilidades_prioridade[3] + habilidades_prioridade[2] + habilidades_prioridade[1]:
            if aluno[habilidade] > 0:  
                habilidades.add(habilidade)
   
    for prioridade, habilidades_prioritarias in habilidades_prioridade.items():
        for habilidade in habilidades_prioritarias:
            if habilidade in habilidades:
                fitness += pesos_prioridade[prioridade]
    
    if fitness > melhor_fitness:
        melhor_fitness = fitness
        melhor_equipe = equipe


fim = time.time()
tempo_total = fim - inicio
minutos = int(tempo_total // 60)
segundos = tempo_total % 60

horas = minutos / 60

# Resultados
print(f"Tempo total: {horas}:{minutos}:{segundos}")
print(f"Melhor fitness: {melhor_fitness}")
print(f"total de combinações realizadas: {total_combinacoes}")
print("\nMelhor equipe:")
for membro in melhor_equipe:
    print(membro)
