import numpy as np

class GrafoMatrizAdjacencia:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz = np.full((num_vertices, num_vertices), float('inf'))  # Inf para indicar ausência de conexão
        np.fill_diagonal(self.matriz, 0)  # Distância de um vértice para ele mesmo é 0
        self.vertices = {}
        self.indice = 0

    def adicionar_vertice(self, nome):
        if nome not in self.vertices:
            self.vertices[nome] = self.indice
            self.indice += 1

    def adicionar_aresta(self, origem, destino, peso):
        i, j = self.vertices[origem], self.vertices[destino]
        self.matriz[i][j] = peso
        self.matriz[j][i] = peso  # Grafo não direcionado

    def mostrar_matriz(self):
        print("\nMatriz de Adjacência:")
        print(self.matriz)


class GrafoListaAdjacencia:
    def __init__(self):
        self.lista = {}

    def adicionar_vertice(self, nome):
        if nome not in self.lista:
            self.lista[nome] = []

    def adicionar_aresta(self, origem, destino, peso):
        self.lista[origem].append((destino, peso))
        self.lista[destino].append((origem, peso))  # Grafo não direcionado

    def mostrar_lista(self):
        print("\nLista de Adjacência:")
        for vertice in self.lista:
            print(f"{vertice} -> {self.lista[vertice]}")

# Definição dos bairros e conexões
bairros = ['A', 'B', 'C', 'D', 'E', 'F']
conexoes = [('A', 'B', 4), ('A', 'C', 2), ('B', 'D', 5), ('C', 'D', 8), ('C', 'E', 3), ('D', 'F', 6), ('E', 'F', 1)]

# Criando e populando a matriz de adjacência
grafo_matriz = GrafoMatrizAdjacencia(len(bairros))
for bairro in bairros:
    grafo_matriz.adicionar_vertice(bairro)
for origem, destino, peso in conexoes:
    grafo_matriz.adicionar_aresta(origem, destino, peso)
grafo_matriz.mostrar_matriz()

# Criando e populando a lista de adjacência
grafo_lista = GrafoListaAdjacencia()
for bairro in bairros:
    grafo_lista.adicionar_vertice(bairro)
for origem, destino, peso in conexoes:
    grafo_lista.adicionar_aresta(origem, destino, peso)
grafo_lista.mostrar_lista()