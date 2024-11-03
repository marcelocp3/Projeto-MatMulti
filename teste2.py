import numpy as np

# Parâmetros e curva paramétrica
passo = 0.001
valor_a = (60 * np.pi) / 5
t = np.arange(0, valor_a, passo)

# Definindo a curva
x_t = 8 * np.cos(t) - 5 * np.cos(8 * t / 3)
y_t = 8 * np.sin(t) - 5 * np.sin(8 * t / 3)

# Derivadas analíticas fornecidas
dx_dt = -8 * np.sin(t) + (40 / 3) * np.sin(8 * t / 3)
dy_dt = 8 * np.cos(t) - (40 / 3) * np.cos(8 * t / 3)

# Tolerância para considerar dx/dt como zero
tolerancia = 1e-5

# Encontrando pontos onde a reta tangente é vertical
pontos_verticais = []
parametros_verticais = []

for i in range(len(t)):
    if abs(dx_dt[i]) > 0 and abs(dy_dt[i]) == 0:
        pontos_verticais.append((x_t[i], y_t[i]))
        parametros_verticais.append(t[i])

# Exibindo os pontos e os valores de parâmetro onde a reta tangente é vertical
print("Pontos onde a reta tangente é vertical:")
for ponto, param in zip(pontos_verticais, parametros_verticais):
    print(f"Ponto: ({ponto[0]:.3f}, {ponto[1]:.3f}), t = {param:.3f}")
