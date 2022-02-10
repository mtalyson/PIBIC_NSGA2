from src.operadoresgeneticos.crossover.CrossOver import CrossOver
from src.operadoresgeneticos.crossover.implementacao.CrossOverBLXAlfa import CrossOverBLXAlfa
from src.operadoresgeneticos.mutation.Mutation import Mutation
from src.operadoresgeneticos.mutation.implementacao.MutationNone import MutationNone
from src.problema.Problema import Problema


class Individuo:
    variaveis = []
    objetivos = []

    crowdingdistance = 0.0

    problema = Problema
    crossover = CrossOver
    mutation = Mutation

    def __init__(self, problema, variaveis):
        self.Individuo(problema, variaveis, CrossOverBLXAlfa(0.1), MutationNone())

    def Individuo(self, problema, variaveis, crossover, mutation):
        self.problema = problema
        self.variaveis = variaveis
        self.crossover = crossover
        self.mutation = mutation

    def getObjetivos(self):
        if not self.objetivos:
            self.objetivos = self.problema.avaliar(self.variaveis)

        return self.objetivos

    def recombinar(self, pai2):
        filhos = []

        matrizfilhos = self.crossover.getOffSpring(self.variaveis, pai2.variaveis, [-10, -10], [10, 10])

        filho1 = Individuo(self.problema, matrizfilhos[0])
        filho2 = Individuo(self.problema, matrizfilhos[1])

        filhos.append(filho1)
        filhos.append(filho2)

        return filhos

    def mutar(self):
        self.variaveis = self.mutation.getMutation(self.variaveis, [-10, -10], [10, 10])

