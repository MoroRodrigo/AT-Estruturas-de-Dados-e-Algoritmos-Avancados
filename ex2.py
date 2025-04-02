import heapq

class GerenciadorPacotes:
    def __init__(self):
        self.heap = []
        self.pacotes = {} 

    def inserir_pacote(self, id_pacote, prioridade, tempo_transmissao):
        pacote = (prioridade, id_pacote, tempo_transmissao)
        heapq.heappush(self.heap, pacote)
        self.pacotes[id_pacote] = pacote
        print(f"Pacote {id_pacote} adicionado com prioridade {prioridade}")

    def remover_pacote_prioritario(self):
        if not self.heap:
            print("Nenhum pacote na fila!")
            return None
        prioridade, id_pacote, tempo_transmissao = heapq.heappop(self.heap)
        del self.pacotes[id_pacote]
        print(f"Transmitindo pacote {id_pacote} (Prioridade: {prioridade}, Tempo: {tempo_transmissao}ms)")

    def atualizar_prioridade(self, id_pacote, nova_prioridade):
        if id_pacote not in self.pacotes:
            print("Pacote não encontrado!")
            return
        
        # Remove o pacote da heap e reinsere com a nova prioridade
        _, id_antigo, tempo_transmissao = self.pacotes[id_pacote]
        self.heap.remove(self.pacotes[id_pacote])
        heapq.heapify(self.heap)  # Reorganiza a heap após a remoção

        novo_pacote = (nova_prioridade, id_antigo, tempo_transmissao)
        heapq.heappush(self.heap, novo_pacote)
        self.pacotes[id_pacote] = novo_pacote
        print(f"Prioridade do pacote {id_pacote} atualizada para {nova_prioridade}")

# Demonstração do funcionamento
roteador = GerenciadorPacotes()
roteador.inserir_pacote(101, 3, 200)
roteador.inserir_pacote(102, 1, 50)
roteador.inserir_pacote(103, 2, 100)

roteador.remover_pacote_prioritario()  # Transmite o de maior prioridade (menor número)
roteador.atualizar_prioridade(103, 0)  # Aumenta a prioridade do pacote 103
roteador.remover_pacote_prioritario()
