import numpy as np

def floyd_warshall(grafo):
    n = len(grafo)
    dist = np.copy(grafo)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i, k] + dist[k, j] < dist[i, j]:
                    dist[i, j] = dist[i, k] + dist[k, j]
    
    return dist

# Definição dos bairros e matriz de adjacência
INF = float('inf')
bairros = ['A', 'B', 'C', 'D', 'E', 'F']
n = len(bairros)

matriz_adj = np.array([
    [0,  5, 10, INF, INF, INF],
    [5,  0,  3,  8, INF, INF],
    [10, 3,  0,  2,  7, INF],
    [INF, 8,  2,  0,  4,  6],
    [INF, INF, 7,  4,  0,  5],
    [INF, INF, INF, 6,  5,  0]
])

menores_tempos = floyd_warshall(matriz_adj)

# Exibe matriz final
def exibir_matriz(matriz, bairros):
    print("\nMatriz de Menores Tempos:")
    print("   " + "  ".join(bairros))
    for i, row in enumerate(matriz):
        print(bairros[i], [f"{x:3}" if x != INF else "INF" for x in row])

exibir_matriz(menores_tempos, bairros)

# Tempo mínimo do Bairro A até F
tempo_min_A_F = menores_tempos[0][-1]
print(f"\nTempo mínimo de A até F: {tempo_min_A_F} minutos")
