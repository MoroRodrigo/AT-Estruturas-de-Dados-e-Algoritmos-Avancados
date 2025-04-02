import itertools
import random
import time
import numpy as np
from functools import lru_cache

# Gera uma matriz de distâncias aleatória
def gerar_matriz_distancias(n):
    matriz = np.random.randint(10, 100, size=(n, n))
    np.fill_diagonal(matriz, 0)  # Distância de uma cidade para ela mesma é zero
    return matriz

# 1. Algoritmo Held-Karp (Programação Dinâmica)
@lru_cache(None)
def held_karp(visitados, ultima_cidade, n, distancias):
    if visitados == (1 << n) - 1:  # Todas as cidades foram visitadas
        return distancias[ultima_cidade][0]
    
    melhor_custo = float('inf')
    for prox_cidade in range(n):
        if (visitados >> prox_cidade) & 1 == 0:  # Se ainda não foi visitada
            novo_visitados = visitados | (1 << prox_cidade)
            custo = distancias[ultima_cidade][prox_cidade] + held_karp(novo_visitados, prox_cidade, n, distancias)
            melhor_custo = min(melhor_custo, custo)
    
    return melhor_custo

def tsp_held_karp(distancias):
    n = len(distancias)
    return held_karp(1, 0, n, tuple(map(tuple, distancias)))

# 2. Algoritmo Guloso (Vizinho Mais Próximo)
def tsp_vizinho_mais_proximo(distancias):
    n = len(distancias)
    visitados = [False] * n
    caminho = [0]
    visitados[0] = True
    
    for _ in range(n - 1):
        ultima_cidade = caminho[-1]
        prox_cidade = min([(i, distancias[ultima_cidade][i]) for i in range(n) if not visitados[i]], key=lambda x: x[1])[0]
        caminho.append(prox_cidade)
        visitados[prox_cidade] = True
    
    caminho.append(0)  # Retorno à cidade inicial
    return sum(distancias[caminho[i]][caminho[i+1]] for i in range(n))

# 3. Algoritmo Genético
def tsp_algoritmo_genetico(distancias, num_geracoes=500, tam_populacao=100, taxa_mutacao=0.1):
    n = len(distancias)
    def fitness(percurso):
        return sum(distancias[percurso[i]][percurso[i+1]] for i in range(n-1)) + distancias[percurso[-1]][percurso[0]]
    
    def cruzamento(pai1, pai2):
        corte = random.randint(1, n-2)
        filho = pai1[:corte] + [c for c in pai2 if c not in pai1[:corte]]
        return filho
    
    def mutacao(percurso):
        if random.random() < taxa_mutacao:
            i, j = random.sample(range(n), 2)
            percurso[i], percurso[j] = percurso[j], percurso[i]
    
    populacao = [random.sample(range(n), n) for _ in range(tam_populacao)]
    for _ in range(num_geracoes):
        populacao.sort(key=fitness)
        nova_geracao = populacao[:tam_populacao//2]
        while len(nova_geracao) < tam_populacao:
            pai1, pai2 = random.sample(nova_geracao[:10], 2)
            filho = cruzamento(pai1, pai2)
            mutacao(filho)
            nova_geracao.append(filho)
        populacao = nova_geracao
    
    melhor_rota = populacao[0]
    return fitness(melhor_rota)

# Comparação de Tempo
cidades = [4, 6, 10]
for n in cidades:
    print(f"\nNúmero de Cidades: {n}")
    matriz_distancias = gerar_matriz_distancias(n)
    
    inicio = time.time()
    resultado_held_karp = tsp_held_karp(matriz_distancias)
    tempo_held_karp = time.time() - inicio
    print(f"Held-Karp (Exato): {resultado_held_karp} - Tempo: {tempo_held_karp:.5f}s")
    
    inicio = time.time()
    resultado_vizinho = tsp_vizinho_mais_proximo(matriz_distancias)
    tempo_vizinho = time.time() - inicio
    print(f"Vizinho Mais Próximo: {resultado_vizinho} - Tempo: {tempo_vizinho:.5f}s")
    
    inicio = time.time()
    resultado_genetico = tsp_algoritmo_genetico(matriz_distancias)
    tempo_genetico = time.time() - inicio
    print(f"Algoritmo Genético: {resultado_genetico} - Tempo: {tempo_genetico:.5f}s")