import numpy as np

# Movimentos possíveis do cavalo no tabuleiro
MOVIMENTOS = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def eh_valido(x, y, tabuleiro, n):
    return 0 <= x < n and 0 <= y < n and tabuleiro[x][y] == -1

def contar_movimentos_validos(x, y, tabuleiro, n):
    count = 0
    for dx, dy in MOVIMENTOS:
        novo_x, novo_y = x + dx, y + dy
        if eh_valido(novo_x, novo_y, tabuleiro, n):
            count += 1
    return count

def resolver_tour_heuristica(x, y, move, tabuleiro, n):
    if move == n * n:
        return True

    # Ordena os movimentos pela quantidade de opções futuras (menor grau primeiro)
    movimentos_ordenados = sorted(MOVIMENTOS, key=lambda m: contar_movimentos_validos(x + m[0], y + m[1], tabuleiro, n))

    for dx, dy in movimentos_ordenados:
        novo_x, novo_y = x + dx, y + dy
        if eh_valido(novo_x, novo_y, tabuleiro, n):
            tabuleiro[novo_x][novo_y] = move
            if resolver_tour_heuristica(novo_x, novo_y, move + 1, tabuleiro, n):
                return True
            tabuleiro[novo_x][novo_y] = -1  # Backtracking

    return False

def iniciar_tour_heuristica(n):
    tabuleiro = np.full((n, n), -1)
    tabuleiro[0][0] = 0

    if not resolver_tour_heuristica(0, 0, 1, tabuleiro, n):
        print("Nenhuma solução encontrada.")
    else:
        print(tabuleiro)

# Testando para um tabuleiro 8x8
iniciar_tour_heuristica(8)
