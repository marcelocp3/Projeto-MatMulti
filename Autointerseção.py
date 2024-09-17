import numpy as np

# Definindo os parâmetros
passo = 0.001
inicial = -6 * np.pi + passo
final = 0 - passo

intervalo = np.arange(inicial, final, passo)

B = []

# Função auxiliar para checar mudança de sinal
def sinal_troca(a, b):
    return a * b <= 0

# Loop para verificar as condições
for b in intervalo:
    if passo + b <= final:
        # Calculando os dois valores para verificar mudança de sinal
        valor_1 = 8 * np.sin((b+passo)/2) + 5 * np.sin(8*(b+passo)/6)
        valor_2 = 8 * np.sin(b/2) + 5 * np.sin(8*b/6)
        
        if sinal_troca(valor_1, valor_2):  # Verificando mudança de sinal
            B.append(b)

# Exibindo os valores obtidos para B
print('Valores obtidos de B:')
for i in B:
    b_abs = abs(i)
    print(f'{b_abs:.3f}')
    
    v = (((30 * np.pi) / 5) - b_abs) / 2
    u = ((30 * np.pi) / 5) - v
    
    print(f'u = {u}')
    print(f'v = {v}')
    
    # Calculando os pontos
    pontos = [v, u]
    for p in pontos:
        x_p = 8 * np.cos(p) - 5 * np.cos(8 * p / 3)
        y_p = 8 * np.sin(p) - 5 * np.sin(8 * p / 3)
        print(f'Pontos: {x_p}, {y_p}')
