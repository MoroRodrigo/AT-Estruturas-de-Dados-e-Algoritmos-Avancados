import numpy as np

# Movimentos possíveis do cavalo no tabuleiro
MOVIMENTOS = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def eh_valido(x, y, tabuleiro, n):
    return 0 <= x < n and 0 <= y < n and tabuleiro[x][y] == -1

def resolver_tour(x, y, move, tabuleiro, n):
    if move == n * n:  # Se todas as casas foram visitadas, solução encontrada
        return True

    for dx, dy in MOVIMENTOS:
        novo_x, novo_y = x + dx, y + dy
        if eh_valido(novo_x, novo_y, tabuleiro, n):
            tabuleiro[novo_x][novo_y] = move
            if resolver_tour(novo_x, novo_y, move + 1, tabuleiro, n):
                return True
            tabuleiro[novo_x][novo_y] = -1  # Backtracking

    return False

def iniciar_tour(n):
    tabuleiro = np.full((n, n), -1)  # Inicializa tabuleiro com -1
    tabuleiro[0][0] = 0  # Começa na posição (0,0)

    if not resolver_tour(0, 0, 1, tabuleiro, n):
        print("Nenhuma solução encontrada.")
    else:
        print(tabuleiro)

# Testando para um tabuleiro 8x8
iniciar_tour(8)
