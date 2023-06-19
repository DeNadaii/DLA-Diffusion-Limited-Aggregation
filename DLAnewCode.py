import random
import numpy as np

def simulacaoDLA():
# Função para criar uma matriz 5x5 inicializada com zeros
    matrix = np.zeros((5, 5))
    LinhaAtual = 0
    print(len(matrix))

# Função para gerar uma particula aleatoria
    def gerarParticula():
        posicaoInicialDaParticula = np.random.randint(0,len(matrix[0]))
        matrix[0][posicaoInicialDaParticula] = 1
        return posicaoInicialDaParticula

    PosicaoAtual = gerarParticula()

# Função que move a particula 
    def moverParaBaixo(LinhaAtual,PosicaoAtual):
        matrix[LinhaAtual][PosicaoAtual] = 0
        if(LinhaAtual + 1 > len(matrix)-1):
            matrix[LinhaAtual][PosicaoAtual] = 0
            print("ultima linha")
        else:
            matrix[LinhaAtual+1][PosicaoAtual] = 1
            return PosicaoAtual
            print("para baixo")
# -------------------------------------------------------------
    def moverParaEsquerda(LinhaAtual,PosicaoAtual):
        matrix[LinhaAtual][PosicaoAtual] = 0
        if(PosicaoAtual-1 < 0):
            matrix[LinhaAtual][len(matrix[LinhaAtual])-1] = 1
            print("atravesou pela esquerda")
        else:
            matrix[LinhaAtual][PosicaoAtual-1] = 1
            return PosicaoAtual
            print("move para esquerda")
# -------------------------------------------------------------
    def moverParaDireita(LinhaAtual,PosicaoAtual):
        matrix[LinhaAtual][PosicaoAtual] = 0
        if(PosicaoAtual+1 == len(matrix[LinhaAtual])):
            matrix[LinhaAtual][0] = 1
            print("atravesou pela direita")
        else:
            matrix[LinhaAtual][PosicaoAtual+1] = 1
            return PosicaoAtual
            print("move para direita")
# -------------------------------------------------------------
    

# Função que decide pra onde a particula vai se mover
    def decidirDirecao(direcaoDaParticula):
        if(direcaoDaParticula == 0):
            indexAposMover = moverParaBaixo(LinhaAtual,PosicaoAtual)
            return indexAposMover
        if(direcaoDaParticula == 1):
            indexAposMover = moverParaDireita(LinhaAtual,PosicaoAtual)
            return indexAposMover
        if(direcaoDaParticula == 2):
            indexAposMover = moverParaEsquerda(LinhaAtual,PosicaoAtual)
            return indexAposMover
    

    while LinhaAtual != len(matrix)-1:
        print(matrix)
        direcaoDaParticula = np.random.randint(0, 3)
        if (direcaoDaParticula == 0):
            LinhaAtual +=1
        else:
            PosicaoAtual = decidirDirecao(direcaoDaParticula)
            print(PosicaoAtual)
    

        
    
# Executar a simulação
simulacaoDLA()