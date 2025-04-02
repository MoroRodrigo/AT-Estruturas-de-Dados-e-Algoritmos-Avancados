import heapq

def dijkstra(grafo, origem, destino):
    distancias = {no: float('inf') for no in grafo}
    distancias[origem] = 0
    caminho = {no: None for no in grafo}
    fila_prioridade = [(0, origem)]
    
    while fila_prioridade:
        dist_atual, no_atual = heapq.heappop(fila_prioridade)
        
        if no_atual == destino:
            break
        
        for vizinho, peso in grafo[no_atual].items():
            nova_dist = dist_atual + peso
            if nova_dist < distancias[vizinho]:
                distancias[vizinho] = nova_dist
                caminho[vizinho] = no_atual
                heapq.heappush(fila_prioridade, (nova_dist, vizinho))
    
    rota = []
    no = destino
    while no is not None:
        rota.append(no)
        no = caminho[no]
    rota.reverse()
    
    return rota, distancias[destino]

grafo = {
    "CD": {"A": 4, "B": 2},
    "A": {"C": 5, "D": 10},
    "B": {"A": 3, "D": 8},
    "C": {"D": 2, "E": 4},
    "D": {"E": 6, "F": 5},
    "E": {"F": 3},
    "F": {}
}

rota_otima, custo_total = dijkstra(grafo, "CD", "F")
print(f"Ótima rota: {' -> '.join(rota_otima)}")
print(f"Custo total (distância mínima): {custo_total} km")
