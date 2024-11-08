import numpy as np
import itertools

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

# Verificando pares de pontos na curva para encontrar interseções
for i, j in itertools.combinations(range(len(t)), 2):
    if abs(i - j) > 1:  # Ignora pontos adjacentes
        distancia = np.sqrt((x_t[i] - x_t[j])**2 + (y_t[i] - y_t[j])**2)
        if distancia < tolerancia:
            ponto_intersecao = ((x_t[i] + x_t[j]) / 2, (y_t[i] + y_t[j]) / 2)
            if ponto_intersecao not in pontos_intersecao:  # Evita duplicatas
                pontos_intersecao.append(ponto_intersecao)

# Exibindo os pontos de auto-interseção encontrados
print(f"Valor de u + v = {valor_a}")
print("Pontos de auto-interseção:")
for ponto in pontos_intersecao:
    print(f"({ponto[0]:.3f}, {ponto[1]:.3f})")
