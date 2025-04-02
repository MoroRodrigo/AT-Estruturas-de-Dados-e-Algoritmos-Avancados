import time

class Metro:
    def __init__(self):
        self.grafo = {}
    
    def adicionar_conexao(self, estacao1, estacao2):
        if estacao1 not in self.grafo:
            self.grafo[estacao1] = []
        if estacao2 not in self.grafo:
            self.grafo[estacao2] = []
        self.grafo[estacao1].append(estacao2)
        self.grafo[estacao2].append(estacao1)
    
    def dfs(self, inicio, visitado=None):
        if visitado is None:
            visitado = set()
        visitado.add(inicio)
        for vizinho in self.grafo[inicio]:
            if vizinho not in visitado:
                self.dfs(vizinho, visitado)
        return visitado
    
    def bfs(self, inicio):
        visitado = set()
        fila = [inicio]
        while fila:
            estacao = fila.pop(0)
            if estacao not in visitado:
                visitado.add(estacao)
                fila.extend(self.grafo[estacao])
        return visitado

# Criando a rede de metrô
rede_metro = Metro()
conexoes = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('D', 'E'), ('E', 'F')]
for estacao1, estacao2 in conexoes:
    rede_metro.adicionar_conexao(estacao1, estacao2)

# Medindo tempo do DFS
inicio = 'A'
tempo_inicio = time.time()
dfs_resultado = rede_metro.dfs(inicio)
tempo_fim = time.time()
print(f"DFS percorreu: {dfs_resultado} em {tempo_fim - tempo_inicio:.6f} segundos")

# Medindo tempo do BFS
tempo_inicio = time.time()
bfs_resultado = rede_metro.bfs(inicio)
tempo_fim = time.time()
print(f"BFS percorreu: {bfs_resultado} em {tempo_fim - tempo_inicio:.6f} segundos")