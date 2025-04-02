import heapq

class Escalonador:
    def __init__(self):
        self.heap = []
        self.processos = {}  # Dicionário para armazenar processos por ID

    def adicionar_processo(self, id_processo, tempo_execucao, prioridade):
        processo = (prioridade, id_processo, tempo_execucao)
        heapq.heappush(self.heap, processo)
        self.processos[id_processo] = processo
        print(f"Processo {id_processo} adicionado com prioridade {prioridade}")

    def executar_proximo(self):
        if not self.heap:
            print("Nenhum processo na fila!")
            return None
        prioridade, id_processo, tempo_execucao = heapq.heappop(self.heap)
        del self.processos[id_processo]
        print(f"Executando processo {id_processo} (Prioridade: {prioridade}, Tempo de Execução: {tempo_execucao})")

    def modificar_prioridade(self, id_processo, nova_prioridade):
        if id_processo not in self.processos:
            print("Processo não encontrado!")
            return
        
        # Removemos o processo antigo e adicionamos novamente com nova prioridade
        _, id_antigo, tempo_execucao = self.processos[id_processo]
        self.heap.remove(self.processos[id_processo])
        heapq.heapify(self.heap)  # Reorganiza a heap

        novo_processo = (nova_prioridade, id_antigo, tempo_execucao)
        heapq.heappush(self.heap, novo_processo)
        self.processos[id_processo] = novo_processo
        print(f"Prioridade do processo {id_processo} alterada para {nova_prioridade}")

# Demonstração do funcionamento
escalonador = Escalonador()
escalonador.adicionar_processo(1, 5, 3)
escalonador.adicionar_processo(2, 3, 1)
escalonador.adicionar_processo(3, 8, 2)

escalonador.executar_proximo()  # Executa o de maior prioridade (menor número)
escalonador.modificar_prioridade(3, 0)  # Muda a prioridade do processo 3
escalonador.executar_proximo()
