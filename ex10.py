import time
import random

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.arestas = []

    def adicionar_aresta(self, u, v, peso):
        self.arestas.append((peso, u, v))

    def encontrar(self, parent, i):
        if parent[i] == i:
            return i
        return self.encontrar(parent, parent[i])

    def unir(self, parent, rank, x, y):
        raiz_x = self.encontrar(parent, x)
        raiz_y = self.encontrar(parent, y)

        if rank[raiz_x] < rank[raiz_y]:
            parent[raiz_x] = raiz_y
        elif rank[raiz_x] > rank[raiz_y]:
            parent[raiz_y] = raiz_x
        else:
            parent[raiz_y] = raiz_x
            rank[raiz_x] += 1

    def kruskal(self):
        self.arestas.sort()
        parent = {v: v for v in self.vertices}
        rank = {v: 0 for v in self.vertices}
        mst = []

        for peso, u, v in self.arestas:
            raiz_u = self.encontrar(parent, u)
            raiz_v = self.encontrar(parent, v)

            if raiz_u != raiz_v:
                mst.append((u, v, peso))
                self.unir(parent, rank, raiz_u, raiz_v)

        return mst

# Criando um grafo pequeno
grafo_pequeno = Grafo(["A", "B", "C", "D"])
grafo_pequeno.adicionar_aresta("A", "B", 2)
grafo_pequeno.adicionar_aresta("A", "C", 6)
grafo_pequeno.adicionar_aresta("A", "D", 3)
grafo_pequeno.adicionar_aresta("B", "D", 5)
grafo_pequeno.adicionar_aresta("B", "C", 8)
grafo_pequeno.adicionar_aresta("C", "D", 7)

# Medindo o tempo para o grafo pequeno
start = time.time()
mst_pequena = grafo_pequeno.kruskal()
end = time.time()

tempo_pequeno = end - start
print("Árvore Geradora Mínima (Grafo Pequeno):", mst_pequena)
print(f"Tempo de execução: {tempo_pequeno:.6f} segundos\n")

# Criando um grafo grande com 100 vértices e 500 arestas
grafo_grande = Grafo([f"V{i}" for i in range(100)])
for _ in range(500):
    u, v = random.sample(grafo_grande.vertices, 2)
    peso = random.randint(1, 100)
    grafo_grande.adicionar_aresta(u, v, peso)

# Medindo o tempo para o grafo grande
start = time.time()
mst_grande = grafo_grande.kruskal()
end = time.time()

tempo_grande = end - start
print("Árvore Geradora Mínima (Grafo Grande) - apenas 5 primeiras conexões:")
print(mst_grande[:5])  # Exibindo apenas as primeiras 5 conexões para não poluir a saída
print(f"Tempo de execução: {tempo_grande:.6f} segundos")
