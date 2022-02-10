import random

from src.individuo.Individuo import Individuo
from src.individuo.IndividuoFactory import IndividuoFactory
from src.problema.Problema import Problema
from src.problema.ProblemaShaffe2 import ProblemaShaffe2


class IndividuoShaffeFactory(IndividuoFactory):
    problema = Problema

    def __init__(self):
        self.problema = ProblemaShaffe2()

    def getIndividuo(self):
        variaveis = [None, None]

        for i in range(len(variaveis)):
            variaveis[i] = random.random()*20-10

        ret = Individuo(self.problema, variaveis)
        return ret
