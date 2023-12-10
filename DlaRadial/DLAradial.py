import numpy as np
import math 

matrix = np.zeros((1000,1000))

matrix[500][500] = 1

R_agr = 1
deltaR = 10

R_lan = 2*R_agr + deltaR

#7 - defina a posição angular theta ( 0<=theta<2*pi)  para lançar a particular em um ponto do circulos de raio R_lan
theta = 2*math.pi

xi = int(R_lan*math.cos(theta))
yi = int(R_lan*math.sin(theta))

frentexi = xi+1
trásxi = xi-1
cimayi=yi+1
baixoyi=yi-1

R_kill= 20*R_lan