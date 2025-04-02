def cobertura_gulosa(lojas, armazens):
    cobertura = set()  # Conjunto de lojas já cobertas
    selecao = []       # Lista de armazéns escolhidos

    while cobertura != lojas:
        melhor_armazem = None
        lojas_cobertas = set()

        # Encontrar o armazém que cobre mais lojas ainda não cobertas
        for armazem, atende in armazens.items():
            novas_lojas = atende - cobertura
            if len(novas_lojas) > len(lojas_cobertas):
                melhor_armazem = armazem
                lojas_cobertas = novas_lojas

        if melhor_armazem:
            selecao.append(melhor_armazem)
            cobertura.update(lojas_cobertas)

    return selecao

# Exemplo de lojas e armazéns
lojas = {"L1", "L2", "L3", "L4", "L5", "L6"}
armazens = {
    "A1": {"L1", "L2", "L4"},
    "A2": {"L2", "L3", "L5"},
    "A3": {"L3", "L6"},
    "A4": {"L4", "L5", "L6"}
}

resultado = cobertura_gulosa(lojas, armazens)
print("Armazéns escolhidos:", resultado)
