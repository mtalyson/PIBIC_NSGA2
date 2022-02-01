import numpy as np

from src.problema.Problema import Problema


class ProblemaExemplo(Problema):

    def avaliar(self, variaveis):
        if not variaveis[0]:
            return np.array([1, 5])
        elif variaveis[0] == 1:
            return np.array([2, 3])
        elif variaveis[0] == 2:
            return np.array([4, 1])
        elif variaveis[0] == 3:
            return np.array([3, 4])
        elif variaveis[0] == 4:
            return np.array([4, 3])
        elif variaveis[0] == 5:
            return np.array([5, 5])
        elif variaveis[0] == 6:
            return np.array([1, 5])
        elif variaveis[0] == 7:
            return np.array([1.5, 4])
        elif variaveis[0] == 8:
            return np.array([2, 3])
        elif variaveis[0] == 9:
            return np.array([4, 1])

        return None

    def getNumeroDeVariaveis(self):
        return 1
