import numpy as np
import matplotlib.pyplot as plt

# Configurações iniciais
ntotal = 400   # Número de partículas para agregar
rp = 0.5       # Raio da partícula
R_Simulation = 5.0 # Raio da simulação
max_cycles = 250  # Máximo de ciclos para tentativa de movimento antes de reiniciar
rkill = 10 * R_Simulation  # Limite máximo de distância a partir do centro antes de excluir a partícula

# Função para adicionar partículas
def add_particle():
    rlan = np.random.uniform(R_Simulation, 2.5 * R_Simulation)  # Raio de lançamento aleatório
    theta = np.random.uniform(0, 2 * np.pi)
    return rlan * np.cos(theta), rlan * np.sin(theta) # Coordenada x e ya partir do centro

# Função para tentar agregar uma partícula
def attempt_to_aggregate(x, y, xdep, ydep, rp, n_aggregated):
    for i in range(n_aggregated):
        if np.sqrt((x - xdep[i])**2 + (y - ydep[i])**2) <= rp:
            return True
    return False

# Inicialização
xdep = np.zeros(ntotal)  # Coordenada x das partículas depositadas
ydep = np.zeros(ntotal)  # Coordenada y das partículas depositadas
xdep[0], ydep[0] = 0, 0  # A primeira partícula no centro

# Processo de agregação
n_aggregated = 1
while n_aggregated < ntotal:
    print(n_aggregated)
    x, y = add_particle()
    for i in range(max_cycles):
        x += np.random.uniform(-rp, rp)
        y += np.random.uniform(-rp, rp)
        if attempt_to_aggregate(x, y, xdep, ydep, rp, n_aggregated):
            xdep[n_aggregated], ydep[n_aggregated] = x, y
            n_aggregated += 1
            break
        if np.sqrt(x**2 + y**2) >= rkill:
            break
# Plotagem do resultado
plt.figure(figsize=(10, 10))
plt.scatter(xdep, ydep, s=100)
plt.axis('equal')
plt.grid(True)
plt.title('Diffusion-Limited Aggregation (DLA) Radial')
plt.savefig("./dla_Radial/resultado DLA.png")
