import numpy as np
from scipy.spatial import KDTree

# Parâmetros e curva paramétrica
passo = 0.001
valor_a = (30 * np.pi) / 5
t = np.arange(0, valor_a, passo)

# Definindo a curva
x_t = 8 * np.cos(t) - 5 * np.cos(8 * t / 3)
y_t = 8 * np.sin(t) - 5 * np.sin(8 * t / 3)

# Tolerância para considerar dois pontos coincidentes
tolerancia = 0.01

# Lista para armazenar pontos de interseção
pontos_intersecao = []

# Construindo a árvore de busca espacial com os pontos (x_t, y_t)
pontos = np.vstack((x_t, y_t)).T
tree = KDTree(pontos)

# Encontrando pares de pontos próximos usando a tolerância
for i, ponto in enumerate(pontos):
    indices = tree.query_ball_point(ponto, tolerancia)
    for j in indices:
        if i < j and abs(i - j) > 1:  # Ignora pontos adjacentes
            ponto_intersecao = ((ponto[0] + pontos[j][0]) / 2, (ponto[1] + pontos[j][1]) / 2)
            if ponto_intersecao not in pontos_intersecao:  # Evita duplicatas
                pontos_intersecao.append(ponto_intersecao)

# Exibindo os pontos de auto-interseção encontrados

print(f"Valor de u + v = {valor_a}")
print("Pontos de auto-interseção:")
for ponto in pontos_intersecao:
    print(f"({ponto[0]:.3f}, {ponto[1]:.3f})")
