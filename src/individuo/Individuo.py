import numpy as np
from src.problema.Problema import Problema


class Individuo:
    variaveis = np.array([])
    objetivos = np.array([])
    problema = Problema

    def __init__(self, problema, variaveis):
        self.problema = problema
        self.variaveis = variaveis

    def getObjetivos(self):
        if not self.objetivos:
            self.objetivos = self.problema.avaliar(self.variaveis)

        return self.objetivos
