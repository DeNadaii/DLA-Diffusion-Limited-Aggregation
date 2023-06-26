import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


matrix = np.zeros((50, 50))

def conferirPrimeiraLinha():
    for i in matrix[0]:
        if i == 1:
            print("particula na primeira linha")
            return True

def simulacaoDLA():
    # Função para criar uma matriz 5x5 inicializada com zeros
    
    LinhaAtual = 0

    # Função para gerar uma partícula aleatória
    def gerarParticula():
        posicaoInicialDaParticula = np.random.randint(0, len(matrix[0]))
        matrix[0][posicaoInicialDaParticula] = 1
        print("particula gerada", matrix[0][posicaoInicialDaParticula])
        return posicaoInicialDaParticula

    PosicaoAtual = gerarParticula()

    # Função que move a partícula para baixo
    def moverParaBaixo(LinhaAtual, PosicaoAtual):
        matrix[LinhaAtual][PosicaoAtual] = 0
        if LinhaAtual + 1 > len(matrix) - 1:
            print("Partícula atingiu a última linha!")
            return PosicaoAtual, LinhaAtual
        if  matrix[LinhaAtual + 1][PosicaoAtual] == 1:
            matrix[LinhaAtual][PosicaoAtual] = 1
            print("colidiu")
            return LinhaAtual, PosicaoAtual, True  # Colisão ocorreu, encerra a simulação
        else:
            matrix[LinhaAtual + 1][PosicaoAtual] = 1
            print("moveu pra baixo")
            return PosicaoAtual, LinhaAtual + 1, False

    # Função que move a partícula para a esquerda
    def moverParaEsquerda(LinhaAtual, PosicaoAtual):
        matrix[LinhaAtual][PosicaoAtual] = 0
        if PosicaoAtual - 1 < 0:
            print("Atravessou pela esquerda")
            matrix[LinhaAtual][len(matrix[LinhaAtual]) - 1] = 1
            return len(matrix[LinhaAtual]) - 1, LinhaAtual, False
        if matrix[LinhaAtual][PosicaoAtual - 1] == 1:
            matrix[LinhaAtual][PosicaoAtual] = 1
            print("colidiu")
            return PosicaoAtual, LinhaAtual, True  # Colisão ocorreu, encerra a simulação
        else:
            matrix[LinhaAtual][PosicaoAtual - 1] = 1
            print("moveu pra esquerda")
            return PosicaoAtual - 1, LinhaAtual, False

    # Função que move a partícula para a direita
    def moverParaDireita(LinhaAtual, PosicaoAtual):
        matrix[LinhaAtual][PosicaoAtual] = 0
        if PosicaoAtual + 1 == len(matrix[LinhaAtual]):
            matrix[LinhaAtual][0] = 1
            print("Atravessou pela direita")
            return 0, LinhaAtual, False
        if matrix[LinhaAtual][PosicaoAtual + 1] == 1:
            matrix[LinhaAtual][PosicaoAtual] = 1
            print("colidiu")
            return PosicaoAtual, LinhaAtual, True  # Colisão ocorreu, encerra a simulação
        else:
            matrix[LinhaAtual][PosicaoAtual + 1] = 1
            print("moveu pra direita")
            return PosicaoAtual + 1, LinhaAtual, False

    # Função que decide para onde a partícula vai se mover
    def decidirDirecao(direcaoDaParticula):
        if direcaoDaParticula == 0:
            return moverParaBaixo(LinhaAtual, PosicaoAtual)
        if direcaoDaParticula == 1:
            return moverParaDireita(LinhaAtual, PosicaoAtual)
        if direcaoDaParticula == 2:
            return moverParaEsquerda(LinhaAtual, PosicaoAtual)

    while LinhaAtual < len(matrix) - 1:
        print(matrix)
        direcaoDaParticula = np.random.randint(0, 3)
        if direcaoDaParticula == 0:
            PosicaoAtual, LinhaAtual, colisao = moverParaBaixo(LinhaAtual, PosicaoAtual)
        else:
            PosicaoAtual, LinhaAtual, colisao = decidirDirecao(direcaoDaParticula)

        if colisao:
            print(matrix)
            return True  # Colisão ocorreu, encerra a simulação

    print(matrix)
    return False  # Simulação concluída sem colisão

#Executar a simulação
i = 0
while i < 11:
    if simulacaoDLA():
        print("Simulação encerrada devido à colisão.")
        if conferirPrimeiraLinha():
            break
        else:
            i = 0
    else:
        print("Simulação concluída sem colisão.")
    i += 1

cmapmine = ListedColormap(['w', 'b'], N=2)

plt.matshow(matrix, cmap=cmapmine, vmin=0, vmax=1)

plt.show()