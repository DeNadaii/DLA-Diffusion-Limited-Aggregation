import random
import numpy as np

matrix = np.zeros((10, 10))

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
            return LinhaAtual, PosicaoAtual
        else:
            matrix[LinhaAtual + 1][PosicaoAtual] = 1
            print("moveu pra baixo")
            return PosicaoAtual, LinhaAtual + 1

    # Função que move a partícula para a esquerda
    def moverParaEsquerda(LinhaAtual, PosicaoAtual):
        matrix[LinhaAtual][PosicaoAtual] = 0
        if PosicaoAtual - 1 < 0:
            print("Atravessou pela esquerda")
            matrix[LinhaAtual][len(matrix[LinhaAtual]) - 1] = 1
            return len(matrix[LinhaAtual]) - 1, LinhaAtual
        if matrix[LinhaAtual][PosicaoAtual - 1] == 1:
            matrix[LinhaAtual][PosicaoAtual] = 1
            print("colidiu")
            return PosicaoAtual, LinhaAtual
        else:
            matrix[LinhaAtual][PosicaoAtual - 1] = 1
            print("moveu pra esquerda")
            return PosicaoAtual - 1, LinhaAtual

    # Função que move a partícula para a direita
    def moverParaDireita(LinhaAtual, PosicaoAtual):
        matrix[LinhaAtual][PosicaoAtual] = 0
        if PosicaoAtual + 1 == len(matrix[LinhaAtual]):
            matrix[LinhaAtual][0] = 1
            print("Atravessou pela direita")
            return 0, LinhaAtual
        if matrix[LinhaAtual][PosicaoAtual + 1] == 1:
            matrix[LinhaAtual][PosicaoAtual] = 1
            print("colidiu")
            return PosicaoAtual, LinhaAtual
        else:
            matrix[LinhaAtual][PosicaoAtual + 1] = 1
            print("moveu pra direita")
            return PosicaoAtual + 1, LinhaAtual

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
            PosicaoAtual, LinhaAtual = moverParaBaixo(LinhaAtual, PosicaoAtual)
        else:
            PosicaoAtual, LinhaAtual = decidirDirecao(direcaoDaParticula)

    print(matrix)

# Executar a simulação


# while matrix[0][3] != 1:
#     simulacaoDLA()

i = 0
while  i < 11:
    simulacaoDLA()
    print("fim da simulacao")
    i += 1
 