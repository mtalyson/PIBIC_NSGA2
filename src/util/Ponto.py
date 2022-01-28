import numpy as np


class Ponto:
    objetivos = np.array([])
    listaPontosDominados = []
    numeroDeVezesPontoDominado = 0
    rank = 0

    def __init__(self, individuo):
        self.individuo = individuo
        self.objetivos = individuo.getObjetivos()

    def getIndividuo(self):
        return self.individuo

