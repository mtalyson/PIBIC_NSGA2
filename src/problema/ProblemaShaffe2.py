import numpy as np
import math

from src.problema.Problema import Problema


class ProblemaShaffe2(Problema):
    numeroVariaveis = 2

    def avaliar(self, variaveis):
        objs = np.array([])
        objs[0] = math.pow(variaveis[0], 2) + math.pow(variaveis[1], 2)
        objs[1] = math.pow(variaveis[0], 2) + math.pow(variaveis[1] - 1, 2)
        return objs

    def getNumeroDeVariaveis(self):
        return self.numeroVariaveis
