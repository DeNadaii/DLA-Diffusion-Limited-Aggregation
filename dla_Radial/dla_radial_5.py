import numpy as np
import matplotlib.pyplot as plt

# Configurações iniciais
ntotal = 1000  # Número de partículas para agregar
rp = 0.5      # Raio da partícula
R_Simulation = 100.0 #Raio da simulação
max_cycles = 500  # Máximo de ciclos para tentativa de movimento antes de reiniciar

# Inicialização
xdep = np.zeros(ntotal)  # Coordenada x das partículas depositadas
ydep = np.zeros(ntotal)  # Coordenada y das partículas depositadas
xdep[0], ydep[0] = 0, 0  # A primeira partícula no centro

# Funções auxiliares
def add_particle():
    rlan = R_Simulation  # Raio de lançamento aleatório
    theta = np.random.uniform(0, 2 * np.pi)
    return rlan * np.cos(theta), rlan * np.sin(theta)

def move_particle():
    r_move = rp  
    theta = np.random.uniform(0, 2 * np.pi)
    return r_move * np.cos(theta), r_move * np.sin(theta)

def attempt_to_aggregate(x, y, xdep, ydep, rp, n_aggregated):
    for i in range(n_aggregated):
        if np.sqrt((x - xdep[i])**2 + (y - ydep[i])**2) <= rp:
            return True
    return False

# Processo de agregação
n_aggregated = 1
while n_aggregated < ntotal:
    x, y = add_particle()
    #print("add particle", x, y)
    for i in range(max_cycles):
        x_linha, y_linha = move_particle()
        #print('move particle', x_linha, y_linha)
        x += x_linha
        y += y_linha
        #print('particle moved', x, y)
        print(i)
        if attempt_to_aggregate(x, y, xdep, ydep, rp, n_aggregated):
            xdep[n_aggregated], ydep[n_aggregated] = x, y
            n_aggregated += 1
            print('agregated')
            break

# Plotagem do resultado
plt.figure(figsize=(8, 8))
plt.scatter(xdep, ydep)
plt.axis('equal')
plt.grid(True)
plt.title('Diffusion-Limited Aggregation (DLA) Radial')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
