import random
import math
from src.operadoresgeneticos.crossover.CrossOver import CrossOver
from src.util import RepairSolution


class CrossOverSBX(CrossOver):
    EPS = 1.0e-14

    probability = 0.0
    distributionindex = 0.0

    def __init__(self):
        self.CrossOverSBX(0.9, 20.0)

    def CrossOverSBX(self, probability, distributionindex):
        self.probability = probability
        self.distributionindex = distributionindex

    def getOffSpring(self, vars1, vars2, lowerbounds, upperbounds):
        ret = [None, None]

        f1 = [None, None]
        f2 = [None, None]

        for i in range(len(f1)):
            f1[i] = vars1[i]

        for i in range(len(f2)):
            f2[i] = vars2[i]

        if random.random() <= self.probability:
            for i in range(len(vars1)):
                valuex1 = vars1[i]
                valuex2 = vars1[i]
                if random.random() <= 0.5:
                    if abs(valuex1 - valuex2) > self.EPS:
                        if valuex1 < valuex2:
                            y1 = valuex1
                            y2 = valuex2
                        else:
                            y1 = valuex2
                            y2 = valuex1

                        lowerbound = lowerbounds[i]
                        upperbound = upperbounds[i]

                        rand = random.random()
                        beta = 1.0 + (2.0 * (y1 - lowerbound) / (y2 - y1))
                        alpha = 2.0 - math.pow(beta, -(self.distributionindex + 1.0))

                        if rand <= (1.0 / alpha):
                            betaq = math.pow(rand * alpha, (1.0 / (self.distributionindex + 1.0)))
                        else:
                            betaq = math.pow(1.0 / (2.0 - rand * alpha), 1.0 / (self.distributionindex + 1.0))

                        c1 = 0.5 * (y1 + y2 - betaq * (y2 - y1))
                        beta = 1.0 + (2.0 * (upperbound - y2) / (y2 - y1))
                        alpha = 2.0 - math.pow(beta, -(self.distributionindex + 1.0))

                        if rand <= (1.0 / alpha):
                            betaq = math.pow((rand * alpha), (1.0 / (self.distributionindex + 1.0)))
                        else:
                            betaq = math.pow(1.0 / (2.0 - rand * alpha), 1.0 / (self.distributionindex + 1.0))

                        c2 = 0.5 * (y1 + y2 + betaq * (y2 - y1))

                        c1 = RepairSolution.repairSolutionVariableValue(c1, lowerbound, upperbound)
                        c2 = RepairSolution.repairSolutionVariableValue(c2, lowerbound, upperbound)

                        if random.random() <= 0.5:
                            f1[i] = c2
                            f2[i] = c1
                        else:
                            f1[i] = c1
                            f2[i] = c2
                    else:
                        f1[i] = valuex1
                        f2[i] = valuex2
                else:
                    f1[i] = valuex2
                    f2[i] = valuex1

        ret[0] = f1
        ret[1] = f2

        return ret
