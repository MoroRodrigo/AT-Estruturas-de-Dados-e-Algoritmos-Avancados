class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def inserir(self, palavra):
        node = self.root
        for char in palavra:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def buscar_prefixo(self, prefixo):
        """Retorna o nó final do prefixo, se existir na Trie"""
        node = self.root
        for char in prefixo:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node

    def sugerir_palavras(self, prefixo):
        """Sugere palavras que começam com o prefixo"""
        node = self.buscar_prefixo(prefixo)
        palavras = []
        if node:
            self._coletar_palavras(node, prefixo, palavras)
        return palavras

    def _coletar_palavras(self, node, prefixo, palavras):
        """Coleta as palavras armazenadas na Trie a partir de um prefixo"""
        if node.is_end_of_word:
            palavras.append(prefixo)
        for char, child_node in node.children.items():
            self._coletar_palavras(child_node, prefixo + char, palavras)

    def distancia_levenshtein(self, palavra1, palavra2):
        """Calcula a distância Levenshtein entre duas palavras"""
        m, n = len(palavra1), len(palavra2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif palavra1[i - 1] == palavra2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return dp[m][n]

    def sugestoes_correcao(self, palavra):
        """Sugere palavras semelhantes com base na distância Levenshtein"""
        palavras = []
        self._coletar_palavras(self.root, "", palavras)
        palavras_similares = sorted(palavras, key=lambda p: self.distancia_levenshtein(palavra, p))
        return palavras_similares[:3]  # Retorna 3 palavras mais próximas

# Demonstração do funcionamento
livraria = Trie()
titulos = ["Python", "Programação", "Estruturas", "Algoritmos", "Banco de Dados", "Computação"]
for titulo in titulos:
    livraria.inserir(titulo.lower())

# Testando Autocompletar
print("Sugestões para 'pro':", livraria.sugerir_palavras("pro"))

# Testando Correção Automática
print("Sugestões para 'algortmos':", livraria.sugestoes_correcao("algortmos"))
